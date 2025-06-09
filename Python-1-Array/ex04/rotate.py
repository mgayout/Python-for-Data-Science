from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys


def printImgInfo(arr, type):

    """

    """

    length = arr.shape[0]
    if type == 0:
        print("[[", end="")
        for pixel in arr[0, :3]:
            print(pixel)
        print(" ... ")
        for i, pixel in enumerate(arr[length - 1, -3:]):
            if i == len(arr[length - 1, -3:]) - 1:
                print(pixel, end="")
            else:
                print(pixel)
        print("]]")
    elif type == 1:
        print("[[", end="")
        for pixel in arr[0, :3]:
            print(pixel, end=" ")
        print("...", end="")
        for pixel in arr[0, -3:]:
            print(f" {pixel}", end="")
        print("]\n  ...  ")
        print(" [", end="")
        for pixel in arr[length - 1, :3]:
            print(pixel, end=" ")
        print("...", end="")
        for pixel in arr[length - 1, -3:]:
            print(f" {pixel}", end="")
        print("]]")


def rotateImg(i):

    """

    """

    width, height = i.size
    ri = Image.new("L", (height, width))
    for y in range(height):
        for x in range(width):
            pixel = i.getpixel((x, y))
            ri.putpixel((y, x), pixel)
    return ri


def main():

    """

    """

    try:
        if len(sys.argv) != 2:
            raise AssertionError("bad argument")
        i = ft_load(sys.argv[1])
        if i is None:
            raise AssertionError("bad argument")
        arr = np.array(i)
        i = i.crop((450, 100, 850, 500))
        i = i.convert("L")
        arr = np.array(i)
        arr = arr[:, :, np.newaxis]
        print("The shape of Image is: ", end="")
        print(f"({i.size[1]}, {i.size[0]}, 1) or {i.size}")
        printImgInfo(arr, 0)
        ri = rotateImg(i)
        arr = np.array(ri)
        print("New shape after Transpose: ", end="")
        print(f"{ri.size}")
        printImgInfo(arr, 1)
        plt.imshow(ri, cmap="gray")
        plt.axis('on')
#        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
