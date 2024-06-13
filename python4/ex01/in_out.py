def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a function that applies function to x."""
    count = 0

    def inner() -> float:
        nonlocal x
        nonlocal count
        x = function(x)
        return x

    return inner
