import numpy as np

np.set_printoptions(precision=1, floatmode="fixed")


class calculator:
    """Vector calculator."""
    def __init__(self, vector: list):
        """Initialize with vector."""
        self.vector = np.array(vector)

    def __add__(self, object) -> None:
        """Add scalar to vector."""
        print(self.vector + object)

    def __mul__(self, object) -> None:
        """Multiply vector by scalar."""
        print(self.vector * object)

    def __sub__(self, object) -> None:
        """Subtract scalar from vector."""
        print(self.vector - object)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError("Division by 0 is impossible")
        """Divide vector by scalar."""
        print(self.vector / object)
