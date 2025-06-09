from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
import sys


def printImgInfo(arr):
    length = arr.shape[0]
    print("[[", end="")
    for pixel in arr[0, :3]:
        print(pixel)
    print("     ...     ")
    for i, pixel in enumerate(arr[length - 1, -3:]):
        if i == len(arr[length - 1, -3:]) - 1:
            print(pixel, end="")
        else:
            print(pixel)
    print("]]")


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
        print("The shape of Image is: ", end="")
        print(f"({i.size[1]}, {i.size[0]}, {i.layers})")
        printImgInfo(arr)
        i = i.crop((450, 100, 850, 500))
        i = i.convert("L")
        arr = np.array(i)
        arr = arr[:, :, np.newaxis]
        print("New shape after slicing: ", end="")
        print(f"({i.size[1]}, {i.size[0]}, 1) or {i.size}")
        printImgInfo(arr)

        plt.imshow(i, cmap="gray")
        plt.axis('on')
#        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
