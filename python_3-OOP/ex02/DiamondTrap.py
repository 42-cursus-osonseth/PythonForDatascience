from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King."""

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize king."""
        super().__init__(name, is_alive)

    def set_eyes(self, color: str):
        """Set eye color."""
        self.eyes = color

    def set_hairs(self, color: str):
        """Set hair color."""
        self.hairs = color

    def get_eyes(self):
        """Get eye color."""
        return self.eyes

    def get_hairs(self):
        """Get hair color."""
        return self.hairs
