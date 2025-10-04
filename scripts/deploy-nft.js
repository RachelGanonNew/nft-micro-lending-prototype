const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);

  // Deploy ProfessionalCredentialNFT
  console.log("Deploying ProfessionalCredentialNFT...");
  const ProfessionalCredentialNFT = await hre.ethers.getContractFactory("ProfessionalCredentialNFT");
  const nftContract = await ProfessionalCredentialNFT.deploy();
  await nftContract.deployed();
  
  console.log("ProfessionalCredentialNFT deployed to:", nftContract.address);
  
  // Whitelist the deployer as a client for testing
  console.log("Whitelisting deployer as a client...");
  await nftContract.setWhitelistedClient(deployer.address, true);
  console.log("Deployer whitelisted as a client");
  
  return nftContract.address;
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
