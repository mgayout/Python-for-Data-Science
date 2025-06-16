from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:

    """"""

    sorted_args = sorted(args)
    size = len(sorted_args)
    if size == 0:
        for value in kwargs.items():
            print("ERROR")
        return
    mean = sum(args) / size
    median = sorted_args[int(size / 2)]
    quartile = [float(sorted_args[int(size / 4)]),
                float(sorted_args[int((size * 3) / 4)])]
    var = sum((x - mean) ** 2 for x in args) / size
    std = var ** 0.5
    result = {"mean": mean, "median": median, "quartile": quartile,
              "std": std, "var": var}

    for key, value, in kwargs.items():
        if value in result:
            print(f"{value} : {result[value]}")
