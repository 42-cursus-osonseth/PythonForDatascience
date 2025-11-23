import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random string ID"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student with automatic login and ID generation."""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login: str = self.name[0] + self.surname
