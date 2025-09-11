import random

def findKthSmallest(arr, k):
     k = k -1

     def quickSelect(l,r):
        pivot, p = arr[r], l
        for i in range(l, r):
                if arr[i] <= pivot:
                    arr[i], arr[p] = arr[p], arr[i]
                    p += 1
        arr[p], arr[r] = arr[r], arr[p]

        if p > k:
            return quickSelect(l, p - 1)
        elif p < k:
            return quickSelect(p + 1, r)
        else:
            return arr[p]
        
     return quickSelect(0, len(arr) - 1)

k = random.randint(1, 30)
arr = random.sample(range(1, 123), 30)
kthSmallest = findKthSmallest(arr, k)
arrLength = len(arr)
print("Array:", sorted(arr))
print("The {}-th smallest element in the array with a length of {} is: '{}'.".format(k + 1, arrLength, kthSmallest))


