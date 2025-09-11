import random
import cProfile

def quickSort(A, left, right):
    if left < right:
        # if the left index is less than the right index, we can sort
        pivotIndex = lumuto(A, left, right)
        quickSort(A, left, pivotIndex - 1)
        quickSort(A, pivotIndex + 1, right)

def lumuto(A, left, right):
    # make a pivot using the last element in the array
    pivot = A[right]
    # set the index to the left of the pivot
    i = left - 1
    for j in range(left, right):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1

arrays = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
for x in arrays:
    A = [random.randint(-100, 100) for _ in range(x)]
    cProfile.run('quickSort(A, 0, len(A) - 1)')


# The big O of this quick sort algorithm is O(n log n). 
# Because the algorithm splits the array in half and sorts each half recursively.


