const hre = require("hardhat");

async function main() {
  const [deployer, client, gigWorker] = await hre.ethers.getSigners();
  const ProfessionalCredentialNFT = await hre.ethers.getContractFactory("ProfessionalCredentialNFT");
  const contract = await ProfessionalCredentialNFT.deploy();
  await contract.deployed();
  console.log("Contract deployed to:", contract.address);

  // Owner whitelists the client
  let tx = await contract.setWhitelistedClient(client.address, true);
  await tx.wait();
  console.log("Client whitelisted:", client.address);

  // Client mints a credential NFT to the gig worker
  const sampleTokenURI = "ipfs://QmSampleHash/sample_metadata.json"; // Replace with actual IPFS hash or URL
  const contractAsClient = contract.connect(client);
  tx = await contractAsClient.mintCredential(gigWorker.address, sampleTokenURI);
  const receipt = await tx.wait();
  const tokenId = receipt.events.find(e => e.event === 'CredentialMinted').args.tokenId;
  console.log(`Minted NFT with tokenId ${tokenId} to gig worker:`, gigWorker.address);

  // Fetch and log the token URI
  const tokenURI = await contract.tokenURI(tokenId);
  console.log("Token URI:", tokenURI);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
}); 