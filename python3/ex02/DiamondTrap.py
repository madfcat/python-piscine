from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A character inheriting traits from Baratheon and Lannister families
    with methods to set and get eye and hair colors."""

    def __init__(self, first_name, *arg):
        """Initializes a new King with the given first name and optional
        arguments."""
        super().__init__(first_name, *arg)

    def set_eyes(self, color):
        """Sets the color of the King's eyes."""
        self.eyes = color

    def set_hairs(self, color):
        """Sets the color of the King's hair."""
        self.hairs = color

    def get_eyes(self):
        """Returns the color of the King's eyes."""
        return self.eyes

    def get_hairs(self):
        """Returns the color of the King's hair."""
        return self.hairs
