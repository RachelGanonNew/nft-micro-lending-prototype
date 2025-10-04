const hre = require("hardhat");

async function main() {
  // Get the deployer account
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);

  // Deploy ProfessionalCredentialNFT
  console.log("Deploying ProfessionalCredentialNFT...");
  const ProfessionalCredentialNFT = await hre.ethers.getContractFactory("ProfessionalCredentialNFT");
  const nftContract = await ProfessionalCredentialNFT.deploy();
  await nftContract.deployed();
  console.log("ProfessionalCredentialNFT deployed to:", nftContract.address);

  // Deploy ReputationOracle with Chainlink parameters
  console.log("Deploying ReputationOracle...");
  const ReputationOracle = await hre.ethers.getContractFactory("ReputationOracle");
  const oracle = await ReputationOracle.deploy();
  await oracle.deployed();
  console.log("ReputationOracle deployed to:", oracle.address);

  // Deploy LendingPoolExample
  console.log("Deploying LendingPoolExample...");
  const LendingPoolExample = await hre.ethers.getContractFactory("LendingPoolExample");
  const lendingPool = await LendingPoolExample.deploy(oracle.address);
  await lendingPool.deployed();
  console.log("LendingPoolExample deployed to:", lendingPool.address);

  // Set the oracle updater (using the deployer for demo purposes)
  console.log("Setting up oracle updater...");
  await oracle.setOracleUpdater(deployer.address);
  console.log("Oracle updater set to:", deployer.address);

  // Whitelist the deployer as a client for testing
  console.log("Whitelisting deployer as a client...");
  await nftContract.setWhitelistedClient(deployer.address, true);
  console.log("Deployer whitelisted as a client");

  console.log("\nDeployment Summary:");
  console.log("=================");
  console.log(`ProfessionalCredentialNFT: ${nftContract.address}`);
  console.log(`ReputationOracle: ${oracle.address}`);
  console.log(`LendingPoolExample: ${lendingPool.address}`);
  console.log(`Deployer/Client: ${deployer.address}`);
  console.log("\nTo test the contracts, you can now run:");
  console.log(`1. npx hardhat run scripts/test-mint.js --network localhost`);
  console.log(`2. npx hardhat run scripts/request-reputation.js --network localhost`); // Updated script name
  console.log(`3. npx hardhat run scripts/update-reputation.js --network localhost`);

  return {
    nftContract: nftContract.address,
    oracle: oracle.address,
    lendingPool: lendingPool.address,
    deployer: deployer.address
  };
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
