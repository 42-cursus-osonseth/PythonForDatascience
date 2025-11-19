from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize Baratheon."""
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Mark the Stark character as dead.
        Change is_alive to False"""
        self.is_alive = False


class Lannister(Character):
    """Representing Lanister family."""

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize Lanister."""
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Mark the Stark character as dead.
        Change is_alive to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name: str, is_alive: bool):
        """return an new object of Lanister"""
        return cls(name, is_alive)
