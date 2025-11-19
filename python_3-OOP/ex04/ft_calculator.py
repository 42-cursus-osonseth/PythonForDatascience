import numpy as np

np.set_printoptions(precision=1, floatmode="fixed")


class calculator:
    """Vector calculator."""

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """Print dot product."""
        v1 = np.array(V1)
        v2 = np.array(V2)
        print(np.sum(v1 * v2))

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Print vector sum."""
        v1 = np.array(V1, dtype=float)
        v2 = np.array(V2, dtype=float)
        print(v1 + v2)

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Print vector difference."""
        v1 = np.array(V1, dtype=float)
        v2 = np.array(V2, dtype=float)
        print(v1 - v2)
