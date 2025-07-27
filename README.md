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

