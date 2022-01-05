from brownie import UNICORNToken, config, network
from scripts.helpers import get_account
import time

initialSupply = 1000 * 10 ** 18


def deploy_unicorn_token():
    account = get_account()
    UnicornToken = UNICORNToken.deploy(initialSupply, {'from': account})
    print(f"Succesfully deployed Unicorn Token at {UnicornToken.address}")
    return UnicornToken


def main():
    deploy_unicorn_token()
