import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    """

    """

    try:
        if not isinstance(family, list):
            raise AssertionError("Family is not a list")
        if not all(isinstance(array, list) for array in family):
            raise AssertionError("Family is not a list of list")
        if not all(len(array) == 2 for array in family):
            raise AssertionError("Family has a non 2D array")
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Start or End is not an integer")
        array = np.array(family)
        print(f"My shape is : {array.shape}")
        print(f"My new shape is : {array[start:end].shape}")
        return array[start:end].tolist()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return []
