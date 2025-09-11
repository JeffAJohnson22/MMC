from random import randrange

def test(initialSize, probRemove):
    # Instantiates accumulators for cheap and costly operations.
    # leaving the Costy spelling
    accCheap, accCosty = 0, 0
    # Sets the initial size and maximum size.
    s = initialSize
    # Maximum size is double the initial size.
    m = 2*s
    # Runs the test 100000 times.
    for i in range(100000):
        # If the random number is less than probRemove, it attempts to remove an item.
        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
        # otherwise, it attempts to add an item.    
            if (s == m):
                print("s:", s, "m:", m, "probRemove:", probRemove)
                # If the size and the max are equal, double the max size.
                m = m*2
                s += 1
                # Increment the costly operation counter.
                accCosty += 1
            else:
                # If the size is less than the max, just add an item.
                s += 1
                # Increment the cheap operation counter.
                accCheap += 1

    # what numbers for initialSize and probRemove result in a costly outcome of 1%
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCosty, 100*accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap, 100*accCheap/(accCosty+accCheap)))

def main():
    # Includes hard coded example(s) trying to maximize the probability of costly operations.
    test(1, -1) # Initial size: 1 Prob Remove: -1 out of 100 Costy: 16 (0.02%) Cheap:   99984 (1e+02%)
main()

# Includes explanation in the comments of how it was possible to maximize the costly operations and why

# To maximize costly operations:
# Start with a small initial size
# Use a low removal probability
# Costy operations happen only when s == m.
# Since m is doubling so fast, we want s to hit m as early on and as often as possible.
# Once m gets too big, hitting s == m wont happen.

# So using initialSize = 1 and probRemove = -1 works because:
# -1 means no removals, so s keeps growing to hit m.
# Starting at 1 means resizes happen early, before m grows too large.
# So it hits m often, maximizing costly operations.