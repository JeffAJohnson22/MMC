"""
A Viltrumite class.
This file defines a Viltrumite class.
It demonstrates how to create a class with attributes,
a constructor, and basic methods.
"""

class Viltrumite:
    """
    A class to represent a Viltrumite.

    Attributes are name.

    Methods
    __init__(name: str)
        Initializes a new Viltrumite object.
    greet()
        Prints a greeting message with the Viltrumite's name.
    """

    def __init__(self, name: str):
        """
        Initializes a new Viltrumite object.

        Params are name.
        """
        self.name = name

    def greet(self):
        """
        Prints a message with the Viltrumite's name.
        """
        print(f"Prepare for my arrival worm, they call me {self.name}.")


def main():
    """
    Main function to run the Viltrumite class.
    """
    p1 = Viltrumite("Conquest")
    p1.greet()

main()