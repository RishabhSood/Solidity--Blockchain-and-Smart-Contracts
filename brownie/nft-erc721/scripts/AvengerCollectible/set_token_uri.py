from brownie import network, AvengerCollectible
from scripts.helpers import get_avenger, get_account, OPENSEA_URL

avenger_metadata_dic = {
    "IronMan": "https://gateway.pinata.cloud/ipfs/QmNZiFbVc7iS4TYpvktkjnXSEGGSA45Dmhs5PoKCexxrj2",
    "CaptainAmerica": "https://gateway.pinata.cloud/ipfs/QmcpgbhfJKkBRnX5uNDZRdfqohSyrqQBW7DEhTLexVeGzq",
    "Hulk": "https://gateway.pinata.cloud/ipfs/Qmd6Wy7i9UFNzekMgcwHKrMh4A9EoNtQm9LYAhGSvukkXA",
    "BlackWidow": "https://gateway.pinata.cloud/ipfs/QmPMfTium9CZ1zDxTw649rn9UN2gq6kZG8ty7BYKwBgMFQ",
    "Thor": "https://gateway.pinata.cloud/ipfs/QmSh6eNiQazKAKCRgAZkxy5svWaA3yh4MpwUZMdjNSbuLw",
    "Wanda": "https://gateway.pinata.cloud/ipfs/QmQpbZmZjUMiEyi1DJXYyvQWLB9JuVcKGndPHk4SKTUj2i",
    "Vision": "https://gateway.pinata.cloud/ipfs/QmUyTV8x1EoiEC6aCmbK6CyXEEeiDw6wJRnETwZgJqu4rB",
    "BlackPanther": "https://gateway.pinata.cloud/ipfs/QmVFgWc128Ae5tuH9S81jNvtt93jHrBSaQuJgLuv9sugeD",
    "HawkEye": "https://gateway.pinata.cloud/ipfs/QmZzL858jW8HNpm6AiUTim1P2RDzMkWdvZrSugFwTzGmwo",
    "SpiderMan": "https://gateway.pinata.cloud/ipfs/QmVEryXgkWcMGVwsQWb2SAVZxspMTdM9FhUmSJ1SBmSajH",
    "DoctorStrange": "https://gateway.pinata.cloud/ipfs/QmPmu9WaosQueYSfktHyofA4WtywASN1yoqWQCCYAXw5ng"
}


def main():
    print(f"Working on {network.show_active()}")
    avenger_collectible = AvengerCollectible[-1]
    number_of_collectibles = avenger_collectible.tokenCounter()
    print(f"There are {number_of_collectibles} Avenger Collectibles")
    for token_id in range(number_of_collectibles):
        avenger = get_avenger(avenger_collectible.tokenIdToAvenger(token_id))
        if not avenger_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_token_uri(token_id, avenger_collectible,
                          avenger_metadata_dic[avenger])


def set_token_uri(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}")
    print("Please wait up to 20 mins and hit the refresh button")
