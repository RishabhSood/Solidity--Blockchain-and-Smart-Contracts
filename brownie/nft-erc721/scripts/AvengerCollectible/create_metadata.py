from brownie import AvengerCollectible, network, config
from scripts.helpers import get_avenger
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json


def main():
    avenger_collectible = AvengerCollectible[-1]
    number_of_avenger_collectibles = avenger_collectible.tokenCounter()
    print(f"There are {number_of_avenger_collectibles} Avenger Collectibles")
    # for token_id in range(number_of_avenger_collectibles):
    for id in range(11):
        avenger = get_avenger(id)
        metadata_file_name = f"./metadata/{network.show_active()}/{avenger}.json"
        if Path(metadata_file_name).exists():
            print(f"Metadata file {metadata_file_name} already exists")
        else:
            print(f"Creating metadata file {metadata_file_name}")
            with open(metadata_file_name, "w") as f:
                metadata = metadata_template.copy()
                metadata["name"] = avenger
                metadata["description"] = f"The legendary Avenger {avenger}"
                image_file_name = "./img/" + avenger + ".png"
                image_uri = upload(filepath=image_file_name)
                metadata["image"] = image_uri
                json.dump(metadata, f)
            upload(metadata_file_name)


def upload(filepath):
    with Path(filepath).open("rb") as fp:
        # ipfs_url = "http://127.0.0.1:5001"
        PINATA_BASE_URL = "https://api.pinata.cloud/"
        endpoint = "pinning/pinFileToIPFS"
        headers = {
            "pinata_api_key": config["pinata"]["api"]["key"],
            "pinata_secret_api_key": config["pinata"]["api"]["secret"],
        }
        # endpoint = "/api/v0/add"
        filename = filepath.split("/")[-1:][0]
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        print(response.json())
        ipfs_hash = response.json()['IpfsHash']
        # image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}/?filename={filename}"
        image_uri = f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}"
        print(image_uri)
        return image_uri
