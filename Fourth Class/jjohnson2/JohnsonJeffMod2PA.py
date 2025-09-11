
# Tribonacci function follows one of the two dynamic programming approaches introduced in class
def trib(n, values):
    if(n < len(values)):
        return values[n]
    ans = trib(n-1, values) + trib(n-2, values) + trib(n - 3, values)
    values += [ans]
    return ans

def main():
    # make a loop while true continues
    # Program continues to ask users for integer input.
    while True:
        try:
            # get a number from the user
            n = int(input("Choose an integer: "))
            # if less than 1 exit the program
            # Program ends correctly
            # Program ends when user enters an integer less than 1.
            if n < 1:
                print("Exiting the program.")
                break
            
            values = [0, 1, 1, 1] 

            print("The {}-th element of the tribonacci sequence is: {}".format(n, trib(n, values)))
        # error checking for non-integer input
        # Program controls for incorrect user input such as real numbers or nonnumeric values.
        except ValueError:
            print("You must enter a positive number.")
main()