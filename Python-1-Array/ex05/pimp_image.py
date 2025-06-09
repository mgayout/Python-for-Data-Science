import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:

    """Inverts the color of the image received."""

    image = 255 - array
    invert_image = Image.fromarray(image)

    return invert_image


def ft_red(array) -> np.ndarray:

    """Apply a red filter to the received image"""

    red_channel = array[:, :, 0]
    image = array.copy()
    image[:, :, 0] = red_channel
    image[:, :, 1] = 0
    image[:, :, 2] = 0
    red_image = Image.fromarray(image)

    return red_image


def ft_green(array) -> np.ndarray:

    """Apply a green filter to the received image"""

    green_channel = array[:, :, 1]
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 1] = green_channel
    image[:, :, 2] = 0
    green_image = Image.fromarray(image)

    return green_image


def ft_blue(array) -> np.ndarray:

    """Apply a blue filter to the received image"""

    blue_channel = array[:, :, 1]
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 1] = 0
    image[:, :, 2] = blue_channel
    blue_image = Image.fromarray(image)

    return blue_image


def ft_grey(array) -> np.ndarray:

    """Apply a grey filter to the received image"""

    grey_channel = np.sum(array, axis=2) / 3
    grey_image = np.repeat(grey_channel[:, :, np.newaxis], 3, axis=2)
    return grey_image
