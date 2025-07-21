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

## Contact
For questions, contact the project owner. 