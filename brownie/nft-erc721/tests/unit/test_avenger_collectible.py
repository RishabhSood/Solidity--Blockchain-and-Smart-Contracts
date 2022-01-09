from brownie import network, AvengerCollectible
import pytest
from scripts.helpers import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
    get_avenger,
)
from scripts.AvengerCollectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Act
    avenger_collectible, creation_transaction = deploy_and_create()
    requestId = creation_transaction.events["requestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, avenger_collectible.address, {
            "from": get_account()}
    )
    # Assert
    assert avenger_collectible.tokenCounter() == 1
    assert avenger_collectible.tokenIdToAvenger(0) == random_number % 11


def test_get_avenger():
    # Arrange / Act
    avenger = get_avenger(0)
    # Assert
    assert avenger == "IronMan"
