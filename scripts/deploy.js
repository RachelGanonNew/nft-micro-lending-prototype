const hre = require("hardhat");

async function main() {
  const ProfessionalCredentialNFT = await hre.ethers.getContractFactory("ProfessionalCredentialNFT");
  const contract = await ProfessionalCredentialNFT.deploy();
  await contract.deployed();
  console.log("ProfessionalCredentialNFT deployed to:", contract.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
}); 