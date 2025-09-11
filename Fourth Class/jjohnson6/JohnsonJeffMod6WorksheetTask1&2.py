import random

# Implement the randomized Las Vegas algorithm
# 2_A. Las Vegas algorithm correctly implemented. 
def lasVegasAlgo(arr):
    tries = 0
    # las vegas has an unlimited runtime and doesn't stop until it has the answer
    while True:
        tries += 1
        position = random.choice(range(len(arr)))
        # that searches for an element holding a 1
        # run the search until we find it
        if arr[position] == 1:
            return position, tries


def main():
    # Create a program that generates a random array of 10,000 elements with equal number of 0's and 1's
    # 1. Random arrays generated according to the specifications of the prompt.
    array = []
    for _ in range(5000):
        array.append(0)
    for _ in range(5000):
        array.append(1)

    # Shuffle the array cause the append just put a bunch of 0's first
    random.shuffle(array)

    position, tries = lasVegasAlgo(array)
    # Your program should output the position of the first 1 found, plus the number of tries before finding it.
    # 2_B. The Las Vegas function should always return an position of a 1 from the input array.
    print(f"Found 1 at position {position} using Las Vegas after {tries} tries.")

main()


# Implement the randomized Monte Carlo algorithm
# 3_A. Monte Carlo algorithm correctly implemented.
def monteCarloAlgo(arr, k):
    # a counter for the number of tries before finding it
    tried = 0
    while True:
        # monte carlo has a fixed run time and stopping condition and can stop even if it hasn't found the answer
        for _ in range(k):
            tried += 1
            output = random.choice(range(len(arr)))
            # that searches for an element holding a 1
            # runs the search until we find it or attempts are exceeded 
            if arr[output] == 1:
                return output, tried
        # Need to return None to break out the loop
        # In testing with an array of zeros it wont stop after the first number of tries
        return None

def main():
    # Create a program that generates a random array of 10,000 elements with equal number of 0's and 1's
    # 1. Random arrays generated according to the specifications of the prompt.
    array = []
    for _ in range(5000):
        array.append(0)
    for _ in range(5000):
        array.append(1)

    # if you want to test with an array of zeros
    # array = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    # Shuffle the array cause the append just put a bunch of 0's first
    random.shuffle(array)

    # Set k equal to 10
    k = 10
    # 3_B. The Monte Carlo function should take two inputs: an array of 0s and 1s and an integer k,
    # setting a limit to the amount of attempts at finding a 1.
    output, tried = monteCarloAlgo(array, k)

    if tried is not None:
        # Your program should output the position of the first 1 found,
        # 3_C. It should output either an index of the first 1 found or a message saying that all attempts have been exhausted.
        print(f"Found 1 at position {output} using Monte Carlo after {tried} tries.")
    else:
        print(f"Couldn't find 1 using Monte Carlo after {k} tries.")
main()