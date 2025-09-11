
def fact(n):
    acc = 1
    for i in range(2, n + 1):
        acc *= i
    return acc

def arrangements(k , n, subsetSizes):
    denominator = fact(n - k)
    for size in subsetSizes:
        denominator *= fact(size)
    return fact(n) // denominator

def AskData():
    while True:
        j = int(input("Enter the number of subsets more than 3 but less than 8: "))
        if 3 < j < 8:
            break
        print(f"{j} has to be between 4 and 7.")
    
    subsetSizes = []
    for i in range(1, j + 1):
        m = int(input(f"Enter a size of a subset {i}: "))
        subsetSizes.append(m)

    n = sum(subsetSizes)

    while True:
        k = int(input(f"Enter the number of elements to arrange (must be less than {n}): "))
        if k < n:
            break
        print(f"{k} has to be less than {n}.")

    print(f"Given your inputs, the number of arrangements is {arrangements(k, n, subsetSizes)}")  
AskData()
