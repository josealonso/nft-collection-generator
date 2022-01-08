import json
import os
import random

from dotenv import load_dotenv
from PIL import Image


def generate_image(data: dict) -> dict:
    """
    Generates image dict.
    Chooses random element from a layer in data and add it to image dictionary
    """
    image = {}
    for layer in data:
        image[layer] = random.choices([x["name"] for x in data[layer]], [
                                      x["weight"] for x in data[layer]])[0]
    return image


def save_image(data: dict, image: dict, image_id: int):
    """
    Сombines layers of the image to one image and saves the final image
    """
    paths = []
    for layer in image:
        for item in data[layer]:
            if item["name"] == image[layer]:
                path = PATH_TO_LAYERS+"/{}/{}".format(layer, item["fileName"])
                paths.append(path)
                break
    image_file = Image.open(paths[0]).convert("RGBA")
    for path in paths[1:]:
        image_file = Image.alpha_composite(
            image_file, Image.open(path).convert("RGBA"))
    image_file.save(PATH_TO_IMAGES+"/{}.png".format(image_id))


def save_metadata(image: dict, image_id: int):
    """
    Сombines layers of the image to one json metadata and saves the final file
    """
    metadata = {
        "image": URL_TO_IMAGE + "/" + str(image_id) + '.png',
        "name": NAME + ' #' + str(image_id),
        "attributes": []
    }
    for layer in image:
        metadata["attributes"].append({layer: image[layer]})
    with open(PATH_TO_METADATA + '/' + str(image_id) + ".json", 'w') as file:
        json.dump(metadata, file, indent=2)


def main():
    # create necessary dirs
    if not os.path.exists(PATH_TO_IMAGES):
        os.mkdir(PATH_TO_IMAGES)
    if not os.path.exists(PATH_TO_METADATA):
        os.mkdir(PATH_TO_METADATA)

    # check is enough files
    sum = 1
    for dir in os.listdir(PATH_TO_LAYERS):
        sum *= len(os.listdir(PATH_TO_LAYERS + "/" + dir))
    if sum < COLLECTION_SIZE:
        raise Exception(
            "Too small files quantity to create a collection with size "
            + str(COLLECTION_SIZE))

    # get data from layers.json
    with open(PATH_TO_JSON) as file:
        data = json.load(file)

    # generate whole image collection of your COLLECTION_SIZE
    images = []
    while True:
        new_image = generate_image(data)
        if new_image in images:
            continue
        images.append(new_image)
        if len(images) == COLLECTION_SIZE:
            break

    # save collection images and metadata
    image_id = 0
    for image in images:
        save_image(data, image, image_id)
        save_metadata(image, image_id)
        image_id += 1


if __name__ == "__main__":
    # import values for constants from .env file
    load_dotenv(".env")

    URL_TO_IMAGE = os.environ.get("URL_TO_IMAGE")
    COLLECTION_SIZE = int(os.environ.get("COLLECTION_SIZE"))
    # Put here your collection name.
    # Every image will have name <NAME #image_number> like CryptoPunks #10
    NAME = os.environ.get("NAME")

    PATH_TO_JSON = os.environ.get("PATH_TO_JSON")
    PATH_TO_LAYERS = os.environ.get("PATH_TO_LAYERS")
    PATH_TO_IMAGES = os.environ.get("PATH_TO_IMAGES")
    PATH_TO_METADATA = os.environ.get("PATH_TO_METADATA")

    main()
