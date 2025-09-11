class CreatureNode:
    # This class represents a node.
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class MythicalFamilyTree:
    # This class represents the family tree.
    def __init__(self):
        self.root = None

    # This method adds the root creature to the tree.
    def addRoot(self, name):
        if self.root is None:
            self.root = CreatureNode(name)
            print(f"Root creature '{name}' added.")
        else:
            print("Root creature already exists!")

    # This method finds a node in the tree.
    def findNode(self, current, name):
        if current is None:
            return None
        if current.name == name:
            return current
        return self.findNode(current.left, name) or self.findNode(current.right, name)

    # This method adds a child creature to the tree.
    def addCreature(self, parentName, side, childName):
        parent = self.findNode(self.root, parentName)
        if not parent:
            print(f"Parent creature '{parentName}' not found.")
            return
        # Check if the side is 'L' or 'R' for left or right child.
        if side.upper() == 'L':
            if parent.left is None:
                # If the left child is None, create a new node.
                parent.left = CreatureNode(childName)
                print(f"{parentName}\n | \n{childName}")
            else:
                print("Left child already exists.")
        elif side.upper() == 'R':
            if parent.right is None:
                # If the right child is None, create a new node.
                parent.right = CreatureNode(childName)
                print(f"{parentName}\n | \n{childName}")
            else:
                print("Right child already exists.")
        else:
            print("Invalid side. Choose 'L' or 'R'.")

    # This method prints the tree structure.
    def printTree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.right:
            # If the right child exists, print it first.
            self.printTree(node.right, level + 1)
        print("  |  " * level + f"{node.name}")
        if node.left:
            # If the left child exists, print it next.
            self.printTree(node.left, level + 1)

    # This method finds the ancestors of a specific creature.
    def findAncestor(self, targetName):
        related = []
        if self.findAncestorHelper(self.root, targetName, related):
            if related:
                # If ancestors are found, format the output.
                # It will get the ancestors and keeps adding them to the list.
                # then it will loop through the list and print them.
                result = f"The {targetName} is descended from the " + " who is descended from the ".join(related)
                print(f"{result}.")
            else:
                print(f"The {targetName} has no known ancestors.")
        else:
            print(f"No creature named '{targetName}' found.")

    # This helper method recursively finds the ancestors.
    def findAncestorHelper(self, node, targetName, related):
        if node is None:
            # If the node is None this is False.
            return False
        if node.name == targetName:
            # If the current node is the target this is True.
            return True
        # Recursively check the left and right children.
        # If either is True, add the current node to the ancestors list.
        if (self.findAncestorHelper(node.left, targetName, related) or 
            self.findAncestorHelper(node.right, targetName, related)):
            related.insert(0, node.name)
            return True
        return False

def main():
    tree = MythicalFamilyTree()

    while True:
        print("===Menu===")
        if tree.root is None:
            print("0. Add Root Creature")
        else:
            print("1. Add Creature")
            print("2. Print All")
            print("3. Print Specific")
            print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
            match choice:
                case 0:
                    # Add root creature
                    # This option is only available if no root has been added yet.
                    if tree.root is None:
                        name = input("Enter name: ")
                        tree.addRoot(name)
                    else:
                        print("Creature already exists")
                case 1:
                    # Add a child creature to the tree.
                    # This option is only available if a root has been added.
                    if tree.root is not None:
                        print("===Creatures===")
                        tree.printTree()
                        parent = input("Enter parent creature name: ")
                        side = input("Enter L or R for child: ")
                        child = input("Enter name of new creature: ")
                        tree.addCreature(parent, side, child)
                    else:
                        print("No root creature found. Please add a root first.")
                case 2:
                    # Print the entire tree.
                    print("===Creatures===")
                    tree.printTree()
                case 3:
                    # Print the ancestors of a specific creature.
                    name = input("Enter name: ")
                    tree.findAncestor(name)
                case 4:
                    # Exit the program.
                    print("Exiting Mythical Creature Program")
                    break
                case _:
                    print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
