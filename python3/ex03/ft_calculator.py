class calculator:
    """Perform element-wise arithmetic operations on a vector."""

    def __init__(self, vector):
        """Initialize the calculator with a vector."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar or element-wise add another vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply by a scalar or element-wise multiply by another vector."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar or element-wise subtract another vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide by a scalar or element-wise divide by another vector."""
        if object == 0:
            raise ZeroDivisionError("divider is 0")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
