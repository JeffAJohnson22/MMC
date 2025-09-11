# Create a tree node
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, data):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, data):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right,
                                          temp.data)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def getMaxValueNode(self, root):
        if root is None or root.right is None:
            return root
        return self.getMaxValueNode(root.right)

    def printPreOrder(self, root):
        if not root:
            return
        print(root.data, end=" ")
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)

    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.data, end=" ")
        self.printInOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            print(currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

    # Efficiency
    # C: The program is able to search for elements in the AVL tree without losing O(lg(n)) efficiency.
    def search(self, root, key):
        # start out checking the root
        # if we have the value we need return it
        if root is None or root.data == key:
            return root
        if key < root.data:
            # if the key value is less go left
            return self.search(root.left, key)
        # if the key value is more go right
        return self.search(root.right, key)
    
# E: The program includes appropriate comments.
def main():
    myTree = AVLTree()
    root = None
    # test numbers to enter
    # nums = 33, 13, 52, 9, 21, 61, 8, 11, 13, 27, 17

    # A loop that keeps asking for a positive integer
    while True:
        try:
            value = int(input("Enter a positive integer, a non-positive integer will end the program: "))
            if value <= 0:
                # Control Flow
                # F: Programs keeps running without crashing until the user enters a negative integer to stop the program.
                myTree.printHelper(root, "", True)
                break
            resultFromSearch = myTree.search(root, value)
            print("Search result:", resultFromSearch)
            if resultFromSearch is None:
                # Insertions
                # A: AVL Tree is able to insert elements into the appropriate space given the specifications of AVL trees.
                root = myTree.insert_node(root, value)
            else:
            # Deletions
            # B: AVL Tree is able to delete elements from the appropriate space given the specifications of AVL trees.
                root = myTree.delete_node(root, value)
            myTree.printHelper(root, "", True)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

main()

# Report
# D: The program includes a report including a substantial description of student’s experience on this assignment,
# incorporating technical terms from the class such as big-O analysis of algorithms

# The time complexity for search in this AVL tree is O(log n), cause at each node I only make one comparison
# then eliminate half of the tree, go left or right, all while halving the search until I get the value I want.
# Since we already had most of the code written, I just had to add the search function and made sure its O(log n).
# This assignment might have been the most straightforward of the assignments.