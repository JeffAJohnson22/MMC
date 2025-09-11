import random

def MCSS(a):
    largest, acc, i = 0, 0, 0
    start = 0
    end = 0
    # Iterate through the array
    for j in range(len(a)):
        # Add the current element to the accumulator
        acc += a[j]
        if (acc > largest):
            # If the accumulated sum is more then the largest number
            # update the largest number and shift the indexes 
            largest = acc
            # update the start and end indexes since the value updated
            start = i
            end = j
        elif (acc < 0):
            # If the accumulated sum is less than 0, update the accumulator to 0
            acc = 0
            # update the starting index to the next element
            i = j + 1
    return largest, start, end

# A random array of numbers
a = [-2, 34, -16, 9, -32, 12, 38, -1, 81, -76, 9, 34, -4, 12]

# test values from the power point
# a = [ 5, -1, 56, -3, -18, 22, -9 ] 
# a = [ -2 , 11, -4, 13, -5, 2 ]

print("The random Array:", a)
result, i, j = MCSS(a)
print("Maximum value:", result)
print("Starting index:", i)
print("Ending index", j)


