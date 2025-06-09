import numpy as np
from PIL import Image
import os

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
        print(f"The shape of Image is: {i.size[1]},{i.size[0]}, {i.layers}")
        return np.array(i)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return []
