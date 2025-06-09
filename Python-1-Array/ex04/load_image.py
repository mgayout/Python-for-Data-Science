from PIL import Image
import os


def ft_load(path: str) -> Image:

    """

    """

    try:
        if not isinstance(path, str):
            raise AssertionError("Image path is not a string")
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Image format is not a 'jpg' or 'jpeg'")
        if not os.path.exists(path):
            raise AssertionError("Image path does not exist")
        i = Image.open(path)
        return i
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None
