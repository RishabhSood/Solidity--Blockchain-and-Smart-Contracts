from brownie import accounts, config, SimpleStorage, network

# use accounts provided by ganache local blockchain
# account = accounts[0]
# method 2: attach your account by runnning : brownie accounts new accname
# account = accounts.load("rinkebyacc2")
# print(account)

# method 3: accounts.add(privatekey)
# account = accounts.add(os.getenv("PRIVATE_KEY"))
# or:
# account = accounts.add(config["wallets"]["from_key"])
# print(account)


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
