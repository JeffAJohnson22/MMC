# Basic Animal Class and Inheritance Example
class Animal:
    # The base class for all the animals
    # The __init__ method for the name and species of the animal
    # The make_sound function is a placeholder and should be overridden by subclasses
    # The info function returns a string with the animal's name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "a generic sound"

    def info(self):
        return f"{self.name} is a {self.species} and makes a sound like '{self.make_sound()}'."


class Bear(Animal):
    # The subclass that represents a bear
    # The __init__ method for the name, species, and fur color of the bear
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    # The make_sound function returns the sound a bear makes    
    def make_sound(self):
        return "GRRROOOAAARRR"
    
    # The info function returns a string with the bear's name, species, and fur color
    def info(self):
        return f"{self.name} is a bear of the {self.species} species with {self.fur_color} fur and {self.make_sound()} sound."

class Elephant(Animal):
    # The subclass that represents a elephant
    # The __init__ method for the name, species, and weight of the elephant
    def __init__(self, name, species, weight):
        super().__init__(name, species)
        self.weight = weight

    # The make_sound function returns the sound a elephant makes
    def make_sound(self):
        return "TOOT TOOT"
    
    # The info function returns a string with the elephant's name, species, and weight
    def info(self):
        return f"{self.name} is an elephant of the {self.species} species and weighs {self.weight} kg, making a {self.make_sound()} sound."

class Penguin(Animal):
    # The subclass that represents a penguin
    # The __init__ method for the name, species, and height of the penguin
    def __init__(self, name, species, height):
        super().__init__(name, species)
        self.height = height

    # The make_sound function returns the sound a penguin makes
    def make_sound(self):
        return "QUACK QUACK"
    
    # The info function returns a string with the penguin's name, species, and height
    def info(self):
        return f"{self.name} is a penguin of the {self.species} species and stands at a height of {self.height} ft, and makes a {self.make_sound()} sound."


class Lion(Animal):
    # The subclass that represents a lion
    # The __init__ method for the name, species, and gender of the lion
    def __init__(self, name, species, gender):
        super().__init__(name, species)
        self.gender = gender.lower()

    # The make_sound function returns the sound a lion/lioness makes
    def make_sound(self):
        return "MEWWWWW" if self.gender == "female" else "ROARRRR"
    
    # The info function returns a string with the lion's name gender, species, and sound
    def info(self):
        return f"{self.name} is a {'lioness' if self.gender == 'female' else 'lion'} of the {self.species} species and makes a sound like '{self.make_sound()}'."

def main():
    print(f"Welcome to the Zoo! Its empty though. Add some animals!")   
    print(" =====================================================  ")

    zoo = []

    while True:
        print("===Zoo Menu===")
        print("1. Add Animal")
        print("2. Print All Animals")
        print("3. Print Specific Animal")
        print("4. Exit")
        print("===============")
        print(f"Total animals in zoo: {len(zoo)}")

        # Prompt the user to select an option
        choice = int(input("Choose an option: "))

        match choice:

            case 1:
                print("===Add Menu===")
                print("1. Add Bear")
                print("2. Add Elephant")
                print("3. Add Penguin")
                print("4. Add Lion")
                print("===============")
                # Prompt the user to select an animal type
                animalOption = int(input("Pick an Animal Option: "))

                match animalOption:
                    case 1:
                        name = input("Enter name: ")
                        species = input("Enter species: ")
                        fur_color = input("Enter fur color: ")
                        # Create a Bear object and add it to the zoo list
                        bear = Bear(name, species, fur_color)
                        zoo.append(bear)

                    case 2:
                        name = input("Enter name: ")
                        species = input("Enter species: ")
                        weight = float(input("Enter weight (in kilograms): "))
                        # Create an Elephant object and add it to the zoo list
                        elephant = Elephant(name, species, weight)
                        zoo.append(elephant)

                    case 3:
                        name = input("Enter name: ")
                        species = input("Enter species: ")
                        height = float(input("Enter height (in feet): "))
                        # Create a Penguin object and add it to the zoo list
                        penguin = Penguin(name, species, height)
                        zoo.append(penguin)

                    case 4:
                        name = input("Enter name: ")
                        species = input("Enter species: ")
                        gender = input("male or female: ")
                        # Create a Lion object and add it to the zoo list
                        lion = Lion(name, species, gender)
                        zoo.append(lion)

                    case _:
                        print("Invalid choice.")

            case 2:
                print("===All Animals in Zoo===")
                for animal in zoo:
                    print(animal.info())

            case 3:
                print("===Print Menu===")
                print("1. Print Bear")
                print("2. Print Elephant")
                print("3. Print Penguin")
                print("4. Print Lion")
                print("===============")
                animalOptionTwo = int(input("Pick an Animal option: "))

                match animalOptionTwo:
                    
                    case 1:
                        # Print all bears in the zoo
                        print("===All Bears in Zoo===")
                        for animal in zoo:
                            if isinstance(animal, Bear):
                                print(animal.info())

                    case 2:
                        # Print all elephants in the zoo
                        print("===All Elephants in Zoo===")
                        for animal in zoo:
                            if isinstance(animal, Elephant):
                                print(animal.info())

                    case 3:
                        # Print all penguins in the zoo
                        print("===All Penguins in Zoo===")
                        for animal in zoo:
                            if isinstance(animal, Penguin):
                                print(animal.info())
                    case 4:
                        # Print all lions in the zoo
                        print("===All Lions in Zoo===")
                        for animal in zoo:
                            if isinstance(animal, Lion):
                                print(animal.info())

                    case _:
                        print("Invalid choice.")

            case 4:
                # Exit the program
                print("Exiting Zoo Program")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
