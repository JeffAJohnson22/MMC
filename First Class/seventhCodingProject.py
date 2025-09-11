 
def fact(n):
    acc = 1
    for i in range(2, n + 1):
        acc *= i
    return acc

def combine(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def CalculateProbablity():
    n = int(input("Enter the total number of possible numbers n value: "))
    k = int(input("Enter the number of chosen numbers k value: "))

    totalOutcomes = combine(n, k)

    waysToWinBig = 1
    bigWin = waysToWinBig / totalOutcomes


    waysToPickK = combine(k, k - waysToWinBig)  
    waysToPickWrong = combine(n - k, waysToWinBig) 
    waysToWinLittle = waysToPickK * waysToPickWrong

    littleWin = waysToWinLittle / totalOutcomes

    print(f"Probability of Big Win {bigWin}")  
    print(f"Probability of Little Win {littleWin}")  

CalculateProbablity()
