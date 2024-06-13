from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class Character"""

    def __init__(self, first_name, is_alive=True):
        """Your docstring for Character Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Your docstring for Character Method"""
        pass


class Stark(Character):
    """Your docstring for Class Stark"""

    def __init__(self, first_name,  *args, **kwargs):
        """Your docstring for Stark Constructor"""
        super().__init__(first_name,  *args, **kwargs)

    def die(self):
        """Your docstring for Stark Method"""
        self.is_alive = False
