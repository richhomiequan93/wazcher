import json

# Define a function to create metadata JSON for each NFT
def create_nft_metadata(nft_number, image_url):
    metadata = {
        "name": f"NFT #{nft_number}",
        "description": f"This NFT represents the number {nft_number} out of 88.",
        "image": image_url,
        "attributes": [
            {
                "trait_type": "88/88",
                "value": f"{nft_number}/88"
            }
        ],
        "batch": 1,
        "level": 0
    }
    return metadata

# Create metadata for 88 individual NFTs
for nft_number in range(1, 89):
    image_url = input(f"Enter URL for #{nft_number}: ")
    metadata = create_nft_metadata(nft_number, image_url.strip())
    with open(f"nft_{nft_number}_metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)
