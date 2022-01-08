from brownie import SimpleCollectible, network
from scripts.helpers import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy_and_create import deploy_and_create
import pytest


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Test only runs on local blockchain")
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
