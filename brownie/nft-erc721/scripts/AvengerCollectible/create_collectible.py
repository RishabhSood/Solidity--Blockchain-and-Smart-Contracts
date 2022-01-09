from brownie import AvengerCollectible
from scripts.helpers import fund_with_link, get_account
from web3 import Web3


def main():
    account = get_account()
    avenger_collectible = AvengerCollectible[-1]
    fund_with_link(avenger_collectible.address,
                   amount=Web3.toWei(0.1, "ether"))
    creation_tx = avenger_collectible.createCollectible({"from": account})
    creation_tx.wait(1)
    print("Collectible created !")
