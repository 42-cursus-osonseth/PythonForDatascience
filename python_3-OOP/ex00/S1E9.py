from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a generic character.

    Attributes
    ----------
    name : str
        The name of the character.
    is_alive : bool
        Status indicating whether the character is alive (default True).
    """

    def __init__(self, name: str, is_alive: bool = True):
        """
        Initialize a character with a name and alive status.

        Parameters
        ----------
        name : str
            The name of the character.
        is_alive : bool, optional
            Whether the character is alive (default is True).
        """
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method to mark the character as dead.

        Must be implemented by subclasses to update the alive status
        appropriately.
        """
        pass


class Stark(Character):
    """Concrete class representing a Stark character."""

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize a Stark character with name and alive status."""
        super().__init__(name, is_alive)

    def die(self):
        """Mark the Stark character as dead.
        Change is_alive to False"""
        self.is_alive = False
