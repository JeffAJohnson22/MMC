# Problem set 1
# inputs array of numbers and a number
def findEntries(arr, number):
    count = 0
    for i in range(len(arr)):
        # Check if the current number is divisible by the number
        # increase the count if it is
        if arr[i] % number == 0:
            count += 1
    # returns the count of numbers that are divisible by the number
    return count

print("Problem set 1")
value =[20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
number = 7
print(f"From the numbers of this unsorted array: {value}, the {number} is divisible {findEntries(value, number)} times.")

value =[18, 54, 76, 81, 36, 48, 99]
number = 9
print(f"From the numbers of this unsorted array: {value}, the {number} is divisible {findEntries(value, number)} times.")
print("\n")

def findSmallestGap(arr):
    # Create empty array to store the minimum gap
    minGap = []
    # append the first gap to the array
    minGap.append(abs(arr[1] - arr[0]))
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            gap = abs(arr[j] - arr[i])
            # Check if the current gap is less than the current minimum gap
            if gap < minGap[0]:
                # If it is, update the minimum gap
                minGap[0] = gap
    # return the minimum gap
    return abs(minGap[0])

print("Problem set 2")
arr = [50, 120, 250, 100, 20, 300, 200]
print(f"The minimum absolute gap from this array: {arr} is {findSmallestGap(arr)}.")

arr = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
print(f"The minimum absolute gap from this array: {arr} is {findSmallestGap(arr)}.")
print("\n")

def findMatrixProduct(posInt, matrixA, matrixB):
    # Create empty array to store the result
    result = []
    for i in range(posInt):
        # Append an empty array to the result
        result.append(posInt * [0])
    for i in range(posInt):
        for j in range(posInt):
            value = 0
            for k in range(posInt):
                # Multiply the current number in the first matrix by the current number in the second matrix
                value += matrixA[i][k] * matrixB[k][j]
            # Round the value to 2 decimals
            result[i][j] = round(value, 2)
    # returns the product of the two matrices
    return result

print("Problem set 3")

posInt = 2
A =[[2,7],[3, 5]]
B = [[8, -4],[6,6]]
result = findMatrixProduct(posInt, A, B)
print(f"The product of the two matrices {A}, {B} is:")
for row in result:
    print(row)

posInt = 3
A =[[1,0,2],[3, -2, 5],[6, 2, -3]] 
B = [[.3, .25, .1],[.4, .8, 0],[-.5, .75, .6]]
result = findMatrixProduct(posInt, A, B)
print(f"The product of the two matrices {A}, {B} is:")
for row in result:
    print(row)
