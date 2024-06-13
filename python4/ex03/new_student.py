import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random string of 15 characters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    """Generate a login from the first letter of the name and the surname."""
    return name[0] + surname


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = generate_id()

    def __post_init__(self):
        """Initialize the login attribute."""
        self.login = generate_login(self.name, self.surname)
