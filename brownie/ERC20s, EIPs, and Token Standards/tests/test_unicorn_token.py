from brownie import network
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, fund_with_link
from scripts.deploy_unicorn_token import deploy_unicorn_token
import time


def test_token_transfer():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    unicorn_token = deploy_unicorn_token()
    account = get_account()
    unicorn_token.transfer(account, 100 * 10 ** 18, {"from": account})
    assert unicorn_token.balanceOf(account) == 100 * 10 ** 18
