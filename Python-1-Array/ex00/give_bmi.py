import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:

    """

    """

    try:
        if len(height) != len(weight):
            raise ValueError("Lists have different size")
        if not all(isinstance(h, (int, float)) for h in height):
            raise ValueError("Height is not a list of integer or float")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise ValueError("Weight is not a list integer or float")
        if not all(h > 0 for h in height):
            raise ValueError("Height has a negative or null value")
        if not all(w > 0 for w in weight):
            raise ValueError("Weight has a negative or null value")
        h = np.array(height)
        w = np.array(weight)
        bmi = w / (h**2)
        return bmi.tolist()

    except Exception as error:
        print("Exception error : ", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    """

    """

    try:
        if not isinstance(bmi, list):
            raise ValueError("BMI is not a list")
        if not all(isinstance(tmp, (int, float)) for tmp in bmi):
            raise ValueError("BMI is not a list of integer or float")
        if not isinstance(limit, int):
            raise ValueError("Limit is not an integer")
        result = np.array(bmi) > limit
        return result

    except Exception as error:
        print("Exception error : ", error)
        return []
