1. Linked Lists - Create a Swap Method

def swapCurrentNext(self):
    if self.Header is None or self.Current is None or self.Current.Next is None:
        return -1

    next_node = self.Current.Next

    prev = None
    if self.Current != self.Header:
        prev = self.Header
        while prev.Next != self.Current:
            prev = prev.Next
    
    self.Current.Next = next_node.Next
    next_node.Next = self.Current
    
    if prev is None:  
        self.Header = next_node
    else:
        prev.Next = next_node
    
    self.Current = next_node
    return 0

2. Asymptotic Notations - Computing the Complexity

(A) What is the complexity of A?

The complexity of algorithm A is O(n + n) = O(2n) = O(n), cause of the 2 loops.

(B) What is the complexity of B?

The complexity of algorithm B is O(n * n) = O(n^2), cause of the two nested loops.

(C) What is the complexity of C?

The complexity of algorithm C is O(n * n^2) = O(n^3), since each O(n) call has a complexity of O(n^2).

(D) What is the complexity of D?

The complexity of algorithm D is O(n^2 * log n), since each O(n^2) calls O(log n).

3. Brute-Force Algorithm - Create the Difference of Two Sets

(A) Brute force function
def bruteForce(A, B):
    C = []
    for a in A:
        found = False
        for b in B:
            if a == b:
                found = True
                break
        if not found:
            C.append(a)
    return C    

A = [2, 4, 6]
B = [3, 4, 5]
result = bruteForce(A, B)
print("Diff of sets A - B:", result) 

(B) Trace the algorithm 

A = [20, 40, 70, 30, 10, 80, 50, 90, 60]
B = [35, 45, 55, 60, 50, 40]
result = bruteForce(A, B)
print("Diff of sets A - B:", result)

20 is not in B, add to C
40 is in B, do not add to C
70 is not in B, add to C
30 is not in B, add to C
10 is not in B, add to C
80 is not in B, add to C
50 is in B, do not add to C
90 is not in B, add to C
60 is in B, do not add to C

Diff of sets A - B is [20, 70, 30, 10, 80, 90]


(C) Asymptotic analysis

The maximum number of comparisons is m * n. So the Big O is O(m * n).

(4) Recursion - Breadth First Search and Depth First Search

(A) Adjacency lists
A: B, D  
B: A, C, G  
C: A, B  
D: E, F  
E: F  
F: B  
G: C, F

(B) BFS Algorithm - Create the BFS Traversal of a Graph
A:0, B:1, C:2, D:3, E:4, F:5, G:6

A = ['B', 'D']
Vertex A is visited
Current array: [0, -1, -1, -1, -1, -1, -1]
Vertex B and D enqueued, Current queue: [B, D]
Vertex A is dequeued, Current queue: [B, D]

B = ['A', 'C', 'G']
Vertex B is visited
Current array: [0, 1, -1, -1, -1, -1, -1]
Vertex A is already visited
Vertex C and G enqueued, Current queue: [D, C, G]
Vertex B is dequeued, Current queue: [D, C, G]

D = ['E', 'F']
Vertex D is visited
Current array: [0, 1, -1, 3, -1, -1, -1]
Vertex E and F enqueued, Current queue: [C, G, E, F]
Vertex D is dequeued, Current queue: [C, G, E, F]

C = ['A', 'B']
Vertex C is visited
Current array: [0, 1, 2, 3, -1, -1, -1]
Vertex A is already visited
Vertex B is already visited
Vertex C is dequeued, Current queue: [G, E, F]

G = ['C', 'F']
Vertex G is visited
Current array: [0, 1, 2, 3, -1, -1, 6]
Vertex C is already visited
Vertex F is enqueued, Current queue: [E, F]
Vertex G is dequeued, Current queue: [E, F]

E = ['F']
Vertex E is visited
Current array: [0, 1, 2, 3, 4, 5, 6]
Vertex F is enqueued, Current queue: [F]
Vertex E is dequeued, Current queue: [F]

F = ['B']
Vertex F is visited
Current array: [0, 1, 2, 3, 4, 5, 6]
Vertex B is already visited
Vertex F is dequeued, Current queue: []

Final Array: [A:0, B:1, D:2, C:3, G:4, E:5, F:6]


(C)DFS Algorithm - Create the DFS Traversal of a Graph

A:0, B:1, C:2, D:3, E:4, F:5, G:6

A = ['B', 'D']
Vertex A is visited
Current array: [0, -1, -1, -1, -1, -1, -1]
Visit Vertex B

B = ['A', 'C', 'G']
Vertex B is visited
Current array: [0, 1, -1, -1, -1, -1, -1]
Visit Vertex C

C = ['A', 'B']
Vertex C is visited
Current array: [0, 1, 2, -1, -1, -1, -1]
Vertex A and B are already visited
Go to Vertex G

G = ['C', 'F']
Vertex G is visited
Current array: [0, 1, 2, -1, -1, -1, 6]
Vertex C is already visited
Go to Vertex F

F = ['B']
Vertex F is visited
Vertex B is already visited
Current array: [0, 1, 2, -1, -1, 5, 6]
Go to Vertex D

D = ['E', 'F']
Vertex D is visited
Current array: [0, 1, 2, 3, -1, -1, -1]
Go to Vertex E

E = ['F']
Vertex E is visited
Current array: [0, 1, 2, 3, 4, -1, -1]
Vertex F is already visited

Final Array: [A:0, B:1, C:2, G:3, F:4, D:5, E:6]


5. Recursion - Master Method

(A) T(n) = 4T(n/2) + n^3

a = 4 
b = 2
f(n) = n^3
log_b(a) = log(4)/log(2) = 2
Worst case: T(n) = Θ(n^3)

(B) T(n) = 4T(n/2) + n^2

a = 4
b = 2
f(n) = n^2
log_b(a) = log(4)/log(2) = 2
Worst case: T(n) = Θ(n^2)

(C) T(n) = 4T(n/2) + n

a = 4
b = 2
f(n) = n
log_b(a) = log(4)/log(2) = 2
f(n) = n^log_b(a) = n^2
Worst case: T(n) = Θ(n^2)

(6) Decrease-and-Conquer Algorithm - Maximum Element in Array

(A) Recursive decrease-and-conquer algorithm
def Maximum(A, right):
    if right == 0:
        return A[0]
    else:
        max = Maximum(A, right - 1)
        return max if max > A[right] else A[right]
    
A = [5, 13, 9, 10]
print(Maximum(A, len(A) - 1))

(B) Trace the algorithm

def Maximum(A, right):
    if right == 0:
        print(f"Base case: return A[0] = {A[0]}")
        return A[0]
    else:
        max = Maximum(A, right - 1)
        current = A[right]
        max_val = max if max > current else current
        print(f"Comparing A[{right}] = {current} with max = {max} -> max = {max_val}")
        return max_val

A = [17, 62, 49, 73, 26, 51]
print("Maximum element is:", Maximum(A, len(A) - 1))

Base case: return A[0] = 17
Comparing A[1] = 62 with max = 17 -> max = 62
Comparing A[2] = 49 with max = 62 -> max = 62
Comparing A[3] = 73 with max = 62 -> max = 73
Comparing A[4] = 26 with max = 73 -> max = 73
Comparing A[5] = 51 with max = 73 -> max = 73
Maximum element is: 73

(C) Recursive relation

T(n) = T(n - 1) + 1 , T(1) = 0
T(n) = T(n - 1) + 1
T(n) = T(n - 2) + 2
T(n) = T(n - 3) + 3

Big O is O(n)

(7) Divide-and-Conquer Algorithms - Mergesort and Quicksort

(A) Worst case for Mergesort and Quicksort
For Mergesort the Big O for the worst case is O(n log n)
For Quicksort the Big O for the worst case is O(n^2) 

(B) Average case for Mergesort and Quicksort
For Mergesort the Big O for the average case is O(n log n)
For Quicksort the Big O for the average case is O(n log n)

(C) Trace the Mergesort algorithm
A = [127, 48, 62, 51, 198, 17, 52, 209]

Left: [127] Right: [48]
Merged: [48, 127]

Left: [62], Right: [51]
Merged: [51, 62]

Left: [198], Right: [17]
Merged: [17, 198]

Left: [52], Right: [209]
Merged: [52, 209]

Left: [48, 127], Right: [51, 62]
Merged: [48, 51, 62, 127]

Left: [17, 198], Right: [52, 209]
Merged: [17, 52, 198, 209]

Sorted array: [17, 48, 51, 52, 62, 127, 198, 209]

(D) Trace the Quick algorithm

i = 0; j = 0
A[j] = 127; pivot = 52
127 > 52: leave array alone
Less than: []
Greater than: [127]

i = 0; j = 1
A[j] = 48; pivot = 52
48 < 52: swap A[0] and A[1] -> [48, 127, 62, 51, 198, 17, 209, 52]
Less than: [48]
Greater than: [127]

i = 1; j = 2
A[j] = 62; pivot = 52
62 > 52: leave array alone
Less than: [48]
Greater than: [127, 62]

i = 1; j = 3
A[j] = 51; pivot = 52
51 < 52: swap A[1] and A[3] -> [48, 51, 62, 127, 198, 17, 209, 52]
Less than: [48, 51]
Greater than: [127, 62]

i = 2; j = 4
A[j] = 198; pivot = 52
198 > 52: leave array alone
Less than: [48, 51]
Greater than: [127, 62, 198]

i = 2; j = 5
A[j] = 17; pivot = 52
17 < 52: swap A[2] and A[5] -> [48, 51, 17, 127, 198, 62, 209, 52]
Less than: [48, 51, 17]
Greater than: [127, 62, 198]

i = 3; j = 6
A[j] = 209; pivot = 52
209 > 52: leave array alone
Less than: [48, 51, 17]
Greater than: [127, 62, 198, 209]

i = 3; j = 7
Swap pivot A[7] = 52 with A[3] = 127 -> [48, 51, 17, 52, 198, 62, 209, 127]



(8) Transform-and-Conquer Algorithms – A VL Trees

(A) Show tree after adding 38 and not balancing

We attach it to 33 cause its less than 56 go to the left
Its greater than 25 go right
Its less than 44 go right
Its greater than 33 go right


                                            56
                                           /  \
                                         25   72
                                        / \   / \
                                       12 44 64 88
                                            \
                                           33
                                            \
                                             38

(B) Describe what possible rotations
Right rotation on 44
Right rotation on 33

(C)

Right rotation on 44
                                            56
                                           /  \
                                         25   72
                                        / \   / \
                                       12 44 64 88
                                            \
                                           33
                                            \
                                             38

Right rotation on 33
                                            56
                                           /  \
                                         25   72
                                        / \   / \
                                       12 44 64 88
                                            \
                                           38
                                          /
                                         33