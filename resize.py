import os

from dotenv import load_dotenv
from PIL import Image


def main():
    # create necessary dirs
    if not os.path.exists(PATH_TO_RESIZED_IMAGES):
        os.mkdir(PATH_TO_RESIZED_IMAGES)

    # resize images
    for image in os.listdir(PATH_TO_IMAGES):
        resized_image = Image.open(PATH_TO_IMAGES+"/"+image).convert('RGBA')
        resized_image = resized_image.resize(OUTPUT_IMAGE_SIZE,
                                             resample=Image.NEAREST)
        resized_image.save(PATH_TO_RESIZED_IMAGES+"/"+image)


if __name__ == "__main__":
    # import values for constants from .env file
    load_dotenv(".env")

    PATH_TO_IMAGES = os.environ.get("PATH_TO_IMAGES")
    OUTPUT_IMAGE_SIZE = (int(os.environ.get("OUTPUT_IMAGE_SIZE_X")),
                         int(os.environ.get("OUTPUT_IMAGE_SIZE_Y")))
    # dir where save resized images
    PATH_TO_RESIZED_IMAGES = os.environ.get("PATH_TO_RESIZED_IMAGES")

    main()
