def selectionSort(array):
    arrayLength = len(array)
    for i in range(arrayLength - 1):
        maxIndex = 0
        comparisons = 0
        swaps = 0
        for j in range(1, arrayLength - i):
            comparisons += 1
            if array[j] > array[maxIndex]:
                maxIndex = j
        if maxIndex != arrayLength - i - 1:
            array[maxIndex], array[arrayLength - i - 1] = array[arrayLength - i - 1], array[maxIndex]
            swaps = 1
            swapInfo = f"Swapped indices {maxIndex} and {arrayLength - i - 1}"
        else:
            swapInfo = "No swap"
        print(f"Iteration {i + 1}: {swapInfo}, Comparisons: {comparisons}, Swaps: {swaps}, Array: {array}")
    print("Array is sorted")
    return array



A = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
print("Selection Sort 1:")
selectionSort(A)
print("\n")

A = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
print("Selection Sort 2:")
selectionSort(A)
print("\n")

A = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
print("Selection Sort 3:")
selectionSort(A)
print("\n")


def bubbleSort(array):    
    for i in range(len(array)):
        swapped = False
        compare = 0
        swaps = 0
        for j in range(0, len(array) - i - 1):
            compare += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                swaps += 1
                print(f"Swapped indices {j} and {j+1}: {array}")
        print(f"Iteration {i + 1}: Comparisons: {compare}, Swaps: {swaps}, Array: {array} \n")
        if not swapped:
            print("Array is sorted")
            break
    return array


A = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
print("Bubble Sort 1:")
bubbleSort(A)
print("\n")

A = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
print("Bubble Sort 2:")
bubbleSort(A)
print("\n")

A = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
print("Bubble Sort 3:")
bubbleSort(A)
