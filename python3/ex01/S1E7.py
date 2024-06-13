from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, *args):
        """Initializes a Baratheon character with the given first name and
        optional arguments."""
        super().__init__(first_name, *args)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """Returns a string representation of the Baratheon character."""
        return ("Vector: "
                f"('{self.family_name}','{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """Returns a string representation for debugging purposes of the
        Baratheon character."""
        return ("Vector: "
                f"('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def die(self):
        """Sets the character's alive status to False."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, *args):
        """Initializes a Lannister character with the given first name and
        optional arguments."""
        super().__init__(first_name, *args)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """Returns a string representation of the Lannister character."""
        return ("Vector: "
                f"('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """Returns a string representation for debugging purposes of the
        Lannister character."""
        return ("Vector: "
                f"('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def die(self):
        """Sets the character's alive status to False."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, *args):
        """Factory method to create a new Lannister instance."""
        return cls(first_name)
