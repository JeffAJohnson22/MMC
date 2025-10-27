# import random
# import cProfile

# # def quickSort(A, left, right):
# #     if left < right:
# #         # if the left index is less than the right index, we can sort
# #         pivotIndex = lumuto(A, left, right)
# #         quickSort(A, left, pivotIndex - 1)
# #         quickSort(A, pivotIndex + 1, right)

# # def lumuto(A, left, right):
# #     # make a pivot using the last element in the array
# #     pivot = A[right]
# #     # set the index to the left of the pivot
# #     i = left - 1
# #     for j in range(left, right):
# #         if A[j] < pivot:
# #             i += 1
# #             A[i], A[j] = A[j], A[i]
# #     A[i + 1], A[right] = A[right], A[i + 1]
# #     return i + 1

# # arrays = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# # for x in arrays:
# #     A = [random.randint(-100, 100) for _ in range(x)]
# #     cProfile.run('quickSort(A, 0, len(A) - 1)')


# # # The big O of this quick sort algorithm is O(n log n). 
# # # Because the algorithm splits the array in half and sorts each half recursively.

# from itertools import combinations

# def permutations(n):
#     ones = list(combinations(list(range(n)), n//2))
#     ans = []
#     for o in ones:
#         case = []
#         for i in range(n):
#             if i in o:
#                 case.append(1)
#             else:
#                 case.append(0)
#         ans.append(case)
#     return ans

# def check(mat):
#     n = len(mat[0])
#     for j in range(n):
#         acc0, acc1 = 0, 0
#         for i in range(len(mat)):
#             if (mat[i][j] == 1):
#                 acc1 += 1
#             elif (mat[i][j] == 0):
#                 acc0 += 1
#             if (acc0 > (n//2)) or (acc1 > n//2):
#                 return False
#     return True

# def layer(r, mat, perm, ans):
#     for p in perm:
#         mat.append(p)
#         if check(mat):
#             if (r+1 == len(p)):
#                 ans +=1
#             else:
#                 ans = layer(r+1, mat, perm, ans)
#         mat.pop()
#     return ans

# def balanced01mat(n):
#     perm = permutations(n)
#     ans = layer(0, [], perm, 0)
#     return ans

# import cProfile
# cProfile.run('print("Balanced matrices of size 6:", balanced01mat(6))')


class Queue:
    """    
    This class implements a first in first out (FIFO) data structure using
    two lists: one for enqueuing elements and another for dequeuing elements.
    """
    
    def __init__(self):
        """
        Initialize an empty Queue with two internal lists.
        
        Attributes:
        a_in (list): Internal list that stores newly enqueued elements.
        a_out (list): Internal list that stores elements ready to be dequeued.
        """
        self.a_in = []
        self.a_out = []
        
        
    def enqueue(self, d):
        """
        Add an element to the back of the queue.
        
        Args:
        d: The element to add to the queue. Can be of any type.
        """
        self.a_in.append(d)
        
    def dequeue(self):
        """
        Remove and return the element at the front of the queue.
        
        Returns:
            The element at the front of the queue (the oldest element).
        """
        if (self.a_out == []):
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = [] 
        return self.a_out.pop(0)
