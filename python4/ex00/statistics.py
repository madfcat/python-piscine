def try_except(num_list: list, func, name: str) -> None:
    try:
        print(name, " : ", func(num_list))
    except Exception as e:
        print("ERROR")

def mean(num_list: list) -> float:
    """This function takes a list of numbers and returns the mean."""
    return sum(num_list) / len(num_list)


def is_odd(num: int) -> bool:
    """This function takes an integer and returns a boolean."""
    return bool(num % 2)


def median(num_list: list) -> float:
    """This function takes a list of numbers and returns the median."""
    num_list.sort()
    size = len(num_list)
    if size == 0:
        raise ValueError("size is 0")
    if size == 1:
        return num_list[0]
    return num_list[size // 2] \
        if is_odd(size) \
        else (num_list[size // 2 - 1] + num_list[size // 2]) / 2


def quartile(num_list: list) -> list:
    """This function calculates the 25% and 75% quartiles."""
    num_list.sort()
    size = len(num_list)

    # Calculate Q1 (25th percentile)
    if size % 4 == 0:
        Q1 = (num_list[size // 4 - 1] + num_list[size // 4]) / 2
    else:
        Q1 = num_list[size // 4]

    # Calculate Q3 (75th percentile)
    if size % 4 == 0:
        Q3 = (num_list[3 * size // 4 - 1] + num_list[3 * size // 4]) / 2
    else:
        Q3 = num_list[3 * size // 4]

    return [Q1, Q3]

def var(num_list: list) -> float:
    return sum((x - mean(num_list)) ** 2 for x in num_list) / len(num_list)

def std(variance: float) -> float:
    return (var(variance)) ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """This function takes a list of numbers and a dictionary of strings."""

    num_list = list(args)

    for key, value in kwargs.items():
        match value:
            case "mean":
                try_except(num_list, mean, "mean")
            case "median":
                try_except(num_list, median, "median")
            case "quartile":
                try_except(num_list, quartile, "quartile")
            case "std":
                print("std", std(num_list))
            case "var":
                print("var", var(num_list))
