import { HardhatUserConfig } from "hardhat/config";
import "@nomiclabs/hardhat-waffle";
import "@openzeppelin/hardhat-upgrades";
import "hardhat-gas-reporter";
import "solidity-coverage";
import "@nomiclabs/hardhat-ethers";
import * as dotenv from "dotenv";
import { NetworkUserConfig } from "hardhat/types";

dotenv.config();

// Placeholder Chainlink configuration for local development
const LINK_TOKEN_ADDRESS = process.env.LINK_TOKEN_ADDRESS || "0x779877A7B0D36585AE52fD9bcCc4Ff6Ff38E41E6"; // Goerli LINK Token (checksummed placeholder)
const ORACLE_ADDRESS = process.env.ORACLE_ADDRESS || "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0"; // Example Goerli Oracle Address, now checksummed
const JOB_ID = process.env.JOB_ID || "29fa9aa13ea1484687d5b02d4197e870"; // Example Job ID
const FEE = process.env.FEE || "100000000000000000"; // 0.1 LINK (wei)

declare module "hardhat/types/config" {
  interface HardhatNetworkUserConfig {
    linkToken?: string;
    oracle?: string;
    jobId?: string;
    fee?: string;
  }

  interface HttpNetworkUserConfig {
    linkToken?: string;
    oracle?: string;
    jobId?: string;
    fee?: string;
  }
}

// You need to export an object to set up your config
const config: HardhatUserConfig = {
  solidity: {
    version: "0.8.9",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  },
  defaultNetwork: "hardhat",
  networks: {
    hardhat: {
      chainId: 31337,
      allowUnlimitedContractSize: true,
    },
    localhost: {
      url: "http://127.0.0.1:8545",
      chainId: 31337,
      allowUnlimitedContractSize: true,
      // Chainlink specific settings for localhost (using Goerli placeholders - these will be hardcoded in deploy script for now)
      // linkToken: LINK_TOKEN_ADDRESS,
      // oracle: ORACLE_ADDRESS,
      // jobId: JOB_ID,
      // fee: FEE,
    },
    goerli: {
      url: process.env.GOERLI_RPC_URL || "",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 5,
      // Chainlink specific settings for Goerli (these will be hardcoded in deploy script for now)
      // linkToken: LINK_TOKEN_ADDRESS,
      // oracle: ORACLE_ADDRESS,
      // jobId: JOB_ID,
      // fee: FEE,
    }
  },
  // @ts-ignore
  gasReporter: {
    enabled: process.env.REPORT_GAS !== undefined,
    currency: "USD",
    // Optional: Add your CoinMarketCap API key for fiat price
    // coinmarketcap: process.env.COINMARKETCAP_API_KEY,
  },
  mocha: {
    timeout: 100000, // 100 seconds
  },
  // Optional: Add paths to artifacts and cache for better performance
  paths: {
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts"
  },
  // Optional: Add typechain support
  // typechain: {
  //   outDir: "typechain",
  //   target: "ethers-v5",
  // },
};

export default config;
