const { ethers } = require("hardhat");

async function main() {
  // Get the list of accounts
  const [deployer] = await ethers.getSigners();
  
  console.log("Deployer account:", deployer.address);
  
  // Get the balance of the deployer account
  const balance = await deployer.getBalance();
  console.log("Account balance:", ethers.utils.formatEther(balance), "ETH");
  
  // Get the chain ID
  const chainId = await ethers.provider.getNetwork();
  console.log("Chain ID:", chainId.chainId);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
