const hre = require("hardhat");
const fetch = require("node-fetch");

// Replace with your deployed contract addresses
const NFT_CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
const ORACLE_CONTRACT_ADDRESS = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";

// ABI fragments
const NFT_ABI = [
  "function balanceOf(address owner) view returns (uint256)",
  "function tokenOfOwnerByIndex(address owner, uint256 index) view returns (uint256)",
  "function tokenURI(uint256 tokenId) view returns (string)"
];

async function main() {
  const [deployer, oracleUpdater, user] = await hre.ethers.getSigners();
  const provider = hre.ethers.provider;

  const ORACLE_ABI = (await hre.artifacts.readArtifact("ReputationOracle")).abi;

  // Connect to deployed contracts
  const nft = new hre.ethers.Contract(NFT_CONTRACT_ADDRESS, NFT_ABI, provider);
  const oracle = new hre.ethers.Contract(ORACLE_CONTRACT_ADDRESS, ORACLE_ABI, provider);

  // Set the oracle updater if needed
  try {
    const tx = await oracle.connect(deployer).setOracleUpdater(oracleUpdater.address);
    await tx.wait();
    console.log("Oracle updater set to:", oracleUpdater.address);
  } catch (e) {
    // Already set, ignore
  }

  // Fetch all NFTs owned by the user
  const balance = await nft.balanceOf(user.address);
  let totalRating = 0, totalPayment = 0, latestDate = 0;
  let nfts = [];
  for (let i = 0; i < balance; i++) {
    const tokenId = await nft.tokenOfOwnerByIndex(user.address, i);
    const tokenURI = await nft.tokenURI(tokenId);
    let metadataUrl = tokenURI;
    if (tokenURI.startsWith("ipfs://")) {
      metadataUrl = tokenURI.replace("ipfs://", "https://ipfs.io/ipfs/");
    }
    try {
      const res = await fetch(metadataUrl);
      const meta = await res.json();
      nfts.push(meta);
      totalRating += meta.client_rating || 0;
      // Parse payment amount (e.g., "500 USDC")
      const payment = parseFloat((meta.payment_amount || "0").split(" ")[0]);
      totalPayment += isNaN(payment) ? 0 : payment;
      // Parse date (YYYY-MM-DD)
      const date = Date.parse(meta.completion_date);
      if (!isNaN(date) && date > latestDate) latestDate = date;
    } catch (e) {
      console.log(`Failed to fetch metadata for token ${tokenId}:`, e);
    }
  }

  // Calculate composite score
  const numProjects = nfts.length;
  const avgRating = numProjects ? totalRating / numProjects : 0;
  const recency = latestDate ? (Date.now() - latestDate) / (1000 * 60 * 60 * 24) : 9999; // days ago
  // Example formula: weighted sum
  let score = Math.round(
    numProjects * 10 +
    avgRating * 20 +
    totalPayment * 0.1 +
    Math.max(0, 100 - recency) // bonus for recent work
  );

  // Connect as oracle updater and set the score
  const oracleAsUpdater = oracle.connect(oracleUpdater);
  const tx2 = await oracleAsUpdater.setReputation(user.address, score);
  await tx2.wait();
  console.log(`Reputation for user ${user.address} set to:`, score);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
}); 