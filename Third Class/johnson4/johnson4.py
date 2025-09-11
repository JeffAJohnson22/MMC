def binSearch(A, start, end, k):
    if start > end:
        return None
    mid = (start + end) // 2
    print(f"Searching in subarray: {A[start:end + 1]} (mid index: {mid})")

    if A[mid] == k:
        return mid
    elif A[mid] < k:
        return binSearch(A, start, mid - 1, k)
    else:
        return binSearch(A, mid + 1, end, k)
    
n = 44
A = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]
print("Looking for, {}".format(n))
print("{} is at index {}".format(n, binSearch(A, 0, len(A) - 1, n)))
print("\n")

n = 56
A = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]
print("Looking for, {}".format(n))
print("{} is at index {}".format(n, binSearch(A, 0, len(A) - 1, n)))
print("\n")

n = 42
A = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]
print("Looking for, {}".format(n))
print("{} is at index {}".format(n, binSearch(A, 0, len(A) - 1, n)))
print("\n")

n = -1
A = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]
print("Looking for, {}".format(n))
print("{} is at index {}".format(n, binSearch(A, 0, len(A) - 1, n)))
print("\n")

n = -7
A = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9] 
print("Looking for, {}".format(n))
print("{} is at index {}".format(n, binSearch(A, 0, len(A) - 1, n)))
print("\n")


def Max(A, start, end):
    print(f"Recursive call with start = {start}, end = {end}")
    if start == end:
        return end
    else:
        mid = (start + end) // 2
        fst = Max(A, start, mid)
        lst = Max(A, mid + 1, end)
        result = fst if A[fst] < A[lst] else lst
        print(f"Returning index {result} with value {A[result]}")
        return result
    
A = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
print("First test A3")
print(f"The minimum value of Array is {A[Max(A, 0, len(A) - 1)]}\n")

A = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
print("Second test A4")
print(f"The minimum value of Array is {A[Max(A, 0, len(A) - 1)]}\n")
print("\n")

A = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
print("Third test A5")
print(f"The minimum value of Array is {A[Max(A, 0, len(A) - 1)]}\n")
print("\n")
