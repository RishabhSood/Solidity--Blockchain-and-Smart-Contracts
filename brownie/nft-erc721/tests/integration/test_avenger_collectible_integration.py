from brownie import network, AvengerCollectible
import time
import pytest
from scripts.helpers import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
)
from scripts.AvengerCollectible.deploy_and_create import deploy_and_create


def test_can_create_avenger_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # Act
    avenger_collectible, creation_transaction = deploy_and_create()
    time.sleep(60)
    # Assert
    assert avenger_collectible.tokenCounter() == 1
