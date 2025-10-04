const hre = require("hardhat");

async function main() {
  const [deployer, user] = await hre.ethers.getSigners();
  const networkConfig = hre.network.config;

  const oracleAddress = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"; // Updated to the actual deployed oracle address from last deployment
  const oracleABI = (await hre.artifacts.readArtifact("ReputationOracle")).abi;

  const oracle = new hre.ethers.Contract(oracleAddress, oracleABI, deployer);

  // Ensure the deployer is set as the oracle updater for this script's execution
  console.log("Ensuring deployer is set as oracle updater:", deployer.address);
  const setTx = await oracle.setOracleUpdater(deployer.address);
  await setTx.wait();

  console.log("Requesting reputation update for user:", user.address);

  try {
    const tx = await oracle.requestReputationUpdate(user.address);
    await tx.wait();
    console.log("Transaction sent to request reputation update.");

    // After the simulated update, fetch the new reputation score
    const newReputation = await oracle.getReputation(user.address);
    console.log(`User ${user.address} now has a reputation score of: ${newReputation}`);
  } catch (error) {
    console.error("Error requesting reputation update:", error);
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
