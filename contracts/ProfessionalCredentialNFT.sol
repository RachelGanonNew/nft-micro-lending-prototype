// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ProfessionalCredentialNFT is ERC721URIStorage, Ownable {
    uint256 public nextTokenId;
    mapping(address => bool) public whitelistedClients;

    event CredentialMinted(address indexed to, uint256 indexed tokenId, string tokenURI);
    event ClientWhitelisted(address indexed client, bool status);

    constructor() ERC721("ProfessionalCredential", "PCNFT") {}

    modifier onlyWhitelisted() {
        require(whitelistedClients[msg.sender], "Not a whitelisted client");
        _;
    }

    function setWhitelistedClient(address client, bool status) external onlyOwner {
        whitelistedClients[client] = status;
        emit ClientWhitelisted(client, status);
    }

    function mintCredential(
        address to,
        string memory tokenURI
    ) external onlyWhitelisted returns (uint256) {
        uint256 tokenId = nextTokenId;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        nextTokenId++;
        emit CredentialMinted(to, tokenId, tokenURI);
        return tokenId;
    }
} 