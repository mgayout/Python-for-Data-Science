import numpy as np
from PIL import Image
import os


def printImgInfo(arr):

    """

    """

    length = arr.shape[0]
    print("[[", end="")
    for pixel in arr[0, :3]:
        print(pixel)
    print("  ...  ")
    for i, pixel in enumerate(arr[length - 1, -3:]):
        if i == len(arr[length - 1, -3:]) - 1:
            print(pixel, end="")
        else:
            print(pixel)
    print("]]")
    print("  ...  ")


def ft_load(path: str) -> np.ndarray:

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
        arr = np.array(i)
        print(f"The shape of Image is: ({i.size[1]},{i.size[0]}, {i.layers})")
        printImgInfo(arr)
        return arr
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return []
