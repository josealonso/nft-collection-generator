import json
import os

from dotenv import load_dotenv


def main():
    for path in os.listdir(PATH_TO_METADATA):
        with open(PATH_TO_METADATA + "/" + path, "r") as file:
            data = json.load(file)
        data["image"] = data["image"].replace(URL_TO_IMAGE,
                                              NEW_URL_TO_IMAGE)
        with open(PATH_TO_METADATA + "/" + path, "w") as file:
            json.dump(data, file, indent=2)


if __name__ == "__main__":
    # import values for constants from .env file
    load_dotenv(".env")

    PATH_TO_METADATA = os.environ.get("PATH_TO_METADATA")
    URL_TO_IMAGE = os.environ.get("URL_TO_IMAGE")
    NEW_URL_TO_IMAGE = os.environ.get("NEW_URL_TO_IMAGE")
    main()
