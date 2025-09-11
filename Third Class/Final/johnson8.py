def bruteForce(A, B):
    C = []
    for a in A:
        value = False
        for b in B:
            if a == b:
                value = True
                break
        if not value:
            C.append(a)
    return C    

A = [2, 4, 6]
B = [3, 4, 5]
result = bruteForce(A, B)
print("Difference of sets A and B:", result)