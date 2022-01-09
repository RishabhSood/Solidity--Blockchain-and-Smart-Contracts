from brownie import config
from pathlib import Path
import requests
import os

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
# Change this filepath
filepath = "./img/Vision.png"
filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": config["pinata"]["api"]["key"],
    "pinata_secret_api_key": config["pinata"]["api"]["secret"],
}


def main():
    for f in os.listdir('./img'):
        with Path("./img/" + f).open("rb") as fp:
            image_binary = fp.read()
            response = requests.post(
                PINATA_BASE_URL + endpoint,
                files={"file": (f, image_binary)},
                headers=headers,
            )
            print(response.json())


if __name__ == "__main__":
    main()
