class Node:
    def __init__(self, number):
        self.number = number
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = None

    def addNodes(self, number):
        newNode = Node(number)
        isEmpty = self.head is None
        addFirst = isEmpty or number <= self.head.number
        if addFirst:
            newNode.next = self.head
            self.head = newNode
        else:
            self.curr = self.head
            while self.curr.next and self.curr.next.number < number:
                self.curr = self.curr.next
            newNode.next = self.curr.next
            self.curr.next = newNode
    
    def deleteNodes(self, number):
        self.curr = self.head
        prev = None
        while self.curr:
            if self.curr.number == number:
                if prev:
                    prev.next = self.curr.next
                else:
                    self.head = self.curr.next
            prev = self.curr
            self.curr = self.curr.next

    def hasNumber(self, number):
        curr = self.head
        while curr:
            if curr.number == number:
                return True
            curr = curr.next
        return False

    def printNodes(self):
        curr = self.head
        printStr = ""
        while curr:
            printStr += str(curr.number) + ", "
            curr = curr.next
        if printStr:
            printStr = printStr[:-2]
        printStr += ";"
        return printStr

def main():
    print("Welcome to the Linked List Game!")
    linkedList = LinkedList()

    with open("data.txt", "r") as file:
        lines = file.readlines()
        array = [int(line.strip()) for line in lines]
    array.sort()

    for num in array:
        linkedList.addNodes(num)

    while True:
        print("===Menu===")
        print("1. Modify Linked List")
        print("2. Exit The Program")

        try:
            choice = int(input("Enter an option: "))
            if choice == 1:
                print("Enter a number to add to current linked list.")
                print(linkedList.printNodes())
                value = input("Enter a number: ")
                number = int(value)
                if linkedList.hasNumber(number):
                    linkedList.deleteNodes(number)
                    print("===Number Removed===")
                    print(f"The number {number} already existed, so it was removed.")
                    print("Modified Linked List:")
                    print(linkedList.printNodes())
                else:
                    linkedList.addNodes(number)
                    print("===Number Added===")
                    print(f"The number {number} didnt exists, so it was added.")
                    print("Modified Linked List:")
                    print(linkedList.printNodes())
            elif choice == 2:
                print("Exiting the program.")
                return
            else:
                 print("Invalid. Try again.")
        except ValueError:
            print("Invalid. Enter a number.")

if __name__ == "__main__":
    main()
