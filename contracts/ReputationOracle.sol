// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract ReputationOracle is Ownable {
    mapping(address => uint256) private _reputationScores;
    address public oracleUpdater;

    event ReputationUpdated(address indexed user, uint256 newScore);
    event OracleUpdaterChanged(address indexed newUpdater);

    modifier onlyOracleUpdater() {
        require(msg.sender == oracleUpdater, "Not authorized");
        _;
    }

    function setOracleUpdater(address updater) external onlyOwner {
        oracleUpdater = updater;
        emit OracleUpdaterChanged(updater);
    }

    function setReputation(address user, uint256 score) external onlyOracleUpdater {
        _reputationScores[user] = score;
        emit ReputationUpdated(user, score);
    }

    function getReputation(address user) external view returns (uint256) {
        return _reputationScores[user];
    }
} 