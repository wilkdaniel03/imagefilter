import requests
import pathlib
from PIL import Image
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


IMAGE_URL = "https://sipi.usc.edu/database/download.php?vol=misc&img=4.2.07"


def fetch() -> None:
    res = requests.get(IMAGE_URL)
    with open("image","wb") as file:
        file.write(res.content)


def save_images(im_path: pathlib.Path, dir_path: pathlib.Path) -> None:
    dir_path.mkdir()

    with Image.open(im_path) as img:
        img_gray = img.convert("L")
        img_gray.save(im_dir.joinpath("image_gray.png"))
        img_rgb = img.convert("RGB")
        img_rgb.save(im_dir.joinpath("image_color.png"))


def main():
    print("Hello from imagefilter!")


if __name__ == "__main__":
    im_path = pathlib.Path("./image")
    if not im_path.exists():
        logger.info("Fetching image from {}".format(IMAGE_URL))
        fetch()

    im_dir = pathlib.Path("./images")
    if not im_dir.exists():
        logger.info("saving images into {}".format(im_dir))
        save_images(im_path,im_dir)
