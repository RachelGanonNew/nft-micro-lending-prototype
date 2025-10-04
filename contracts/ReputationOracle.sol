// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract ReputationOracle is Ownable {
    mapping(address => uint256) private _reputationScores;
    address public oracleUpdater;

    event ReputationUpdated(address indexed user, uint256 newScore);
    event OracleUpdaterChanged(address indexed newUpdater);

    constructor() Ownable() {
        oracleUpdater = msg.sender;
    }

    function setOracleUpdater(address updater) external {
        oracleUpdater = updater;
        emit OracleUpdaterChanged(updater);
    }

    function requestReputationUpdate(address user) external {
        // Simulate Chainlink request and fulfillment off-chain
        // In a real scenario, an off-chain Chainlink node would process this request
        // and call `fulfill` with the actual reputation score.
        // For this prototype, we'll directly set a simulated score.
        uint256 simulatedScore = 75; // Example simulated score
        this.setReputation(user, simulatedScore);
    }

    function setReputation(address user, uint256 score) external {
        _reputationScores[user] = score;
        emit ReputationUpdated(user, score);
    }

    function getReputation(address user) external view returns (uint256) {
        return _reputationScores[user];
    }
} 