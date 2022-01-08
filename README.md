# NFT collection generator
Generates layered images, whole collections. Provides additional functionality.
## Repository includes three scripts
- [generate.py](#generate.py "generate.py")
- [resize.py](#resize.py "resize.py")
- [change_url.py](#change_url.py "change_url.py")

## Installation
```
pip install -r requirements.txt
```
## generate.py
Generates layered images.
### Set environment variables in .env file
```bash
# metadata files have field "image <URL_TO_IMAGE>/<file_number>
URL_TO_IMAGE=change_me_later
COLLECTION_SIZE=10
# metadata files have field "name": <NAME> #<file_number> like CryptoPunk #10
NAME=NAME
PATH_TO_JSON=./layers.json
PATH_TO_LAYERS=./layers
PATH_TO_IMAGES=./images
PATH_TO_METADATA=./metadata
```
### layers.json
```json
{
    "first-layer": [
        {
            "name": "name",
            "fileName": "filename.png",
            "weight": 100
		}
    ]
}
```
Main JSON objects like `first-layer` should equal folders inside `./layers` and objects names will equal attributes names in metadata files.
**Note**:  sum of wheights inside one main object should equal 100

### Run
```
python generate.py
```

## resize.py
This script scales your images. Marketplace doesn't display small images like 12 pixels images correctly.
### Set environment variables in .env file
```bash
PATH_TO_IMAGES=./images
# path for resized images
PATH_TO_RESIZED_IMAGES=./images-resized
# new sizes
OUTPUT_IMAGE_SIZE_X=576
OUTPUT_IMAGE_SIZE_Y=576
```
###Run
```
python resize.py
```
## change_url.py
This script change `image` field in metadata files.
### Set environment variables in .env file
```bash
URL_TO_IMAGE=change_me_later
NEW_URL_TO_IMAGE=ipfshash
PATH_TO_METADATA=./metadata
```
### Run
```bash
python change_url.py
```
## License

Usage is provided under the [MIT License](opensource.org/licenses/mit-license.php). See LICENSE for the full details.