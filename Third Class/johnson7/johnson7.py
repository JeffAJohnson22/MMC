def quickSort(A, left, right, swaps, recursiveCalls):
    if left < right:
        recursiveCalls += 1
        pivotIndex, swaps = lumuto(A, left, right, swaps)
        swaps, recursiveCalls = quickSort(A, left, pivotIndex - 1, swaps, recursiveCalls)
        swaps, recursiveCalls = quickSort(A, pivotIndex + 1, right, swaps, recursiveCalls)
    return swaps, recursiveCalls

def lumuto(A, left, right, swaps):
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] > pivot:  
            i += 1
            A[i], A[j] = A[j], A[i]
            swaps += 1
    A[i + 1], A[right] = A[right], A[i + 1]
    swaps += 1
    return i + 1, swaps


A = [38, 21, 39, 60, -1, 10, 81, 23]
print("Original array:", A)
swaps, recursiveCalls = quickSort(A, 0, len(A) - 1, 0, 0)
print("Sorted array in descending order:", A)
print("Number of swaps:", swaps)
print("Number of recursive calls:", recursiveCalls)
print("\n")

B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
print("Original array:", B)
swaps, recursiveCalls = quickSort(B, 0, len(B) - 1, 0, 0)
print("Sorted array in descending order:", B)
print("Number of swaps:", swaps)
print("Number of recursive calls:", recursiveCalls)
print("\n")

C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
print("Original array:", C)
swaps, recursiveCalls = quickSort(C, 0, len(C) - 1, 0, 0)
print("Sorted array in descending order:", A)
print("Number of swaps:", swaps)
print("Number of recursive calls:", recursiveCalls)