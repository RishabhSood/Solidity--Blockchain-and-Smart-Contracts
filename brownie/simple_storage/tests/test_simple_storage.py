from brownie import SimpleStorage, accounts

# check pytest documentation
# testing tips:
# to test 1 function, run : brownie tests -k function_name
# brownie test --pdb : to run python debugger if a test fails
# brownie test -s : verbose output


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_store():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    transaction = simple_storage.store(expected, {"from": account})
    actual = simple_storage.retrieve()
    # Assert
    assert actual == expected
