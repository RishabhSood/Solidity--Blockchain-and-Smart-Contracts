// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AvengerCollectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;

    enum Avenger {
        IronMan,
        CaptainAmerica,
        Hulk,
        BlackWidow,
        Thor,
        Wanda,
        Vision,
        BlackPanther,
        Hawkeye,
        SpiderMan,
        DoctorStrange
    }
    mapping(uint256 => Avenger) public tokenIdToAvenger;
    mapping(bytes32 => address) public requestIdToSender;
    event requestedCollectible(bytes32 indexed requestId, address requester);
    event avengerAssigned(uint256 indexed tokenId, Avenger avenger);

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 _fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("Avenger", "<A>")
    {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible() public returns (bytes32) {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        requestedCollectible(requestId, msg.sender);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: Is not approved or owner!"
        );
        _setTokenURI(tokenId, _tokenURI);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Avenger avenger = Avenger(randomNumber % 11);
        uint256 newTokenId = tokenCounter;
        tokenIdToAvenger[newTokenId] = avenger;
        emit avengerAssigned(newTokenId, avenger);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        tokenCounter++;
    }
}
