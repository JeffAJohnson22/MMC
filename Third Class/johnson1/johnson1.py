class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = None

    def addANode(self, number):
        newNode = Node(number)
        newNode.next = self.head
        self.head = newNode
        if self.curr is None:
            self.curr = newNode
        return True

    def printNodes(self):
        curr = self.head
        print_str = ""
        while curr:
            print_str += str(curr.data) + ", "
            curr = curr.next
        print_str = print_str[:-2]
        print_str += ";"
        print(print_str)

    def nodeToThirdPosition(self):
        curr_node = self.head
        count = 1
        while count < 3 and curr_node:
            curr_node = curr_node.next
            count += 1

        if curr_node:
            self.curr = curr_node
            return True
        return False

    def removeNextToCurr(self):
        if self.curr and self.curr.next:
            node_to_remove = self.curr.next
            self.curr.next = self.curr.next.next
            del node_to_remove
            return True
        return False

    def insertNextToCurr(self, number):
        if self.curr:
            newNode = Node(number)
            newNode.next = self.curr.next
            self.curr.next = newNode
            return True
        return False

# Create a LinkedList
linkedList = LinkedList()

# Add numbers in reverse order
linkedList.addANode(91)
linkedList.addANode(56)
linkedList.addANode(34)
linkedList.addANode(11)
linkedList.addANode(88)
linkedList.addANode(76)

# Print the current list
print("\nCurrent Status:")
linkedList.printNodes()

# Add a node in the third position
linkedList.nodeToThirdPosition()

# Remove the next element to the current node
linkedList.removeNextToCurr()

# Insert 23 next to the current node
linkedList.insertNextToCurr(23)

# Print the modified list
print("\nFinal Status:")
linkedList.printNodes()
print("\n")