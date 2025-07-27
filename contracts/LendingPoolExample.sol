// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IReputationOracle {
    function getReputation(address user) external view returns (uint256);
}

contract LendingPoolExample {
    IReputationOracle public reputationOracle;

    constructor(address oracleAddress) {
        reputationOracle = IReputationOracle(oracleAddress);
    }

    // Example: max loan is 10x the reputation score (for demo purposes)
    function getMaxLoanAmount(address user) external view returns (uint256) {
        uint256 score = reputationOracle.getReputation(user);
        return score * 10;
    }
} 