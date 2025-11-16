from S1E9 import Character


class Baratheon(Character):

    def __init__(self, name: str, is_alive: bool = True):
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Mark the Stark character as dead.
        Change is_alive to False"""
        self.is_alive = False


class Lannister(Character):
    def __init__(self, name: str, is_alive: bool = True):
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Mark the Stark character as dead.
        Change is_alive to False"""
        self.is_alive = False

    # def create_lannister():
