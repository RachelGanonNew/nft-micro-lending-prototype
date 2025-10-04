# AI-Driven NFT-backed Micro-Lending Pool for Gig Workers (Prototype 1)

## Overview
This prototype demonstrates the core of a decentralized micro-lending protocol for gig workers, focusing on **Professional Credential NFTs**. Clients can mint NFTs to gig workers as proof of completed projects, including metadata such as project details, payment, and client rating. This is the foundation for an AI-powered on-chain reputation system.

## Features
- **Professional Credential NFTs:** ERC-721 NFTs minted by whitelisted clients to gig workers.
- **Metadata:** Each NFT contains project details, completion date, payment amount, and client rating.

## Project Structure
- `contracts/ProfessionalCredentialNFT.sol` — The main smart contract.
- `contracts/sample_metadata.json` — Example NFT metadata.

## Setup
1. **Install dependencies:**
   ```bash
   npm install
   ```
2. **Compile contracts:**
   ```bash
   npx hardhat compile
   ```

## How to Deploy & Test
1. **Start a local Hardhat node:**
   ```bash
   npx hardhat node
   ```
2. **Deploy the contract:**
   (See `scripts/deploy.js` for a deployment script.)
   ```bash
   npx hardhat run scripts/deploy.js --network localhost
   ```
3. **Run the test script:**
   ```bash
   npx hardhat run scripts/test-mint.js --network localhost
   ```

## Example Metadata
See `contracts/sample_metadata.json` for an example of the metadata structure used for each credential NFT.

---

## Prototype 2: AI-Powered Reputation Oracle

### Overview
This prototype demonstrates an off-chain AI oracle that analyzes Professional Credential NFTs and updates a user's on-chain reputation score. The score can be queried by other smart contracts (e.g., lending pools) to determine loan terms.

### Components
- `contracts/ReputationOracle.sol`: On-chain contract for storing and exposing reputation scores.
- `scripts/update-reputation.js`: Simulates the AI updater, calculates and sets a user's reputation score.
- `contracts/LendingPoolExample.sol`: Example contract that queries the oracle for a user's score.

### How to Use
1. **Compile contracts:**
   ```bash
   npx hardhat compile
   ```
2. **Run the updater script:**
   ```bash
   npx hardhat run scripts/update-reputation.js --network localhost
   ```
   This will deploy the oracle, set the updater, and update a user's reputation score.
3. **Integrate in other contracts:**
   See `LendingPoolExample.sol` for how to query the reputation score on-chain.

### Customization
- Replace the simulated score in `update-reputation.js` with real AI logic as needed.
- Deploy the oracle contract separately and use its address in your dApps.

---

## Prototype 3: Decentralized AI Oracle Architecture (Chainlink Integration)

### Overview
This section outlines the architectural integration of a decentralized AI oracle using Chainlink, demonstrating how reputation scores can be fetched on-chain via oracle requests. For this prototype on a local Hardhat network, the Chainlink integration is simulated, showcasing the design pattern rather than a live Chainlink network interaction.

**NOTE:** For the purpose of this hackathon prototype and to simplify local testing, authorization modifiers (`onlyOwner`, `onlyOracleUpdater`) have been temporarily removed from `setOracleUpdater` and `setReputation` functions in `contracts/ReputationOracle.sol`. In a production environment, these modifiers would be crucial for security and access control, ensuring only authorized entities can update reputation scores.

### Components
- `contracts/ReputationOracle.sol`: Modified to include `requestReputationUpdate` for triggering oracle requests and `setReputation` to receive/store the reputation score.
- `scripts/deploy-all.js`: Deploys the `ReputationOracle` contract.
- `scripts/request-reputation.js`: Demonstrates triggering a simulated Chainlink request for a user's reputation score. The `requestReputationUpdate` function within `ReputationOracle.sol` now directly sets a simulated score (e.g., 75) for demonstration purposes, mimicking the fulfillment of an off-chain AI oracle.

### How to Use
1. **Start a local Hardhat node:**
   ```bash
   npx hardhat node
   ```
2. **Redeploy all contracts:**
   ```bash
   npx hardhat run scripts/deploy-all.js --network localhost
   ```
3. **Request a simulated reputation update:**
   ```bash
   npx hardhat run scripts/request-reputation.js --network localhost
   ```
   This script will call the `requestReputationUpdate` function on the deployed `ReputationOracle` contract, which will then set a simulated reputation score. The script will also fetch and display the updated score.

### Real-World Integration (Future Work)
For a live BlockDAG testnet/mainnet deployment, the placeholder Chainlink configurations in `hardhat.config.ts` would be replaced with actual Chainlink LINK token addresses, oracle contract addresses, and job IDs. The off-chain AI model would then integrate with a Chainlink node to fulfill `requestReputationUpdate` calls, providing actual reputation scores.

