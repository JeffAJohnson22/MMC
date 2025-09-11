from random import randrange
# 1. Double Array Queue Implementation Included for class slides
class Queue:
    def __init__(self):
        self.a_in = []
        self.a_out = []
        self.costly = 0
        self.cheap = 0

    def enqueue(self, data):
        self.a_in.append(data)
        # modified to count cheap operations
        self.cheap += 1

    def dequeue(self):
        # if both a_in and a_out are empty, we cannot dequeue
        if self.a_out == [] and self.a_in == []:
            return None
            
        if (self.a_out == []):
            while len(self.a_in) > 0:
                # move elements is costy
                self.a_out.append(self.a_in.pop())
                self.costly += 1

        # dequeuing is cheap
        else:
            self.cheap += 1
        return self.a_out.pop()


def main():
    # 2. Captures user input for probabilities of enqueues and dequeues.
    probEnqueues = int(input("Give the probability of enqueues, 33-67: "))
    while True:
        try:
            # validates the input to ensure it is between 33 and 67.
            if probEnqueues >= 33 and probEnqueues <= 67:
                q = Queue()
                for i in range(100000):
                    # use the user input to determine whether to enqueue or dequeue
                    if (randrange(100) < probEnqueues):
                        q.enqueue(randrange(1000))
                    else:
                        q.dequeue()
                # 3. Controls for correct amount of enqueues/dequeues.
                # Values should always add to 100 and neither should never be less than 33 or greater than 67.
                print(f"The probability of enqueues is {probEnqueues}%.")
                print(f"The probability of dequeues is therefore {100 - probEnqueues}%.")

                # 4. Program correctly computes the amount of costly and cheap operations and prints them out for the user. Both the amount and percentage of operations should be included.
                total_operations = q.costly + q.cheap
                costly_percentage = (q.costly / total_operations) * 100
                cheap_percentage = (q.cheap / total_operations) * 100   
                print("Costly operations percentage: {:.2f}%".format(costly_percentage))
                print("Cheap operations percentage: {:.2f}%".format(cheap_percentage))
                print("Total operations percentage:", costly_percentage + cheap_percentage)
                break
            else:
                # If the value is not in the correct range try again
                probEnqueues = int(input("Invalid input. Please enter a number between 33 and 67: "))
        # Since Im using a try I have to catch the ValueError
        except ValueError:
            probEnqueues = int(input("Invalid input. Please enter a number between 33 and 67: "))
main()

# 5 Criterion Long Description 
# Included