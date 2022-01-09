from scripts.helpers import get_account, OPENSEA_URL, get_contract, fund_with_link
from brownie import AvengerCollectible, config, network


def deploy_and_create():
    account = get_account()
    avenger_collectible = AvengerCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account}, publish_source=config["networks"][network.show_active()].get(
            "verify", False))
    fund_with_link(avenger_collectible.address)
    creating_tx = avenger_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    return avenger_collectible, creating_tx


def main():
    deploy_and_create()
