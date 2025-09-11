# Egyptian fraction Greedy
from math import ceil
  
# n is the numerator, d is the denominator
def egyptian(n, d):
  
    print("The Egyptian Fraction of {}/{}".format(n, d))
    ans = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)          # compute the minimal larger denominator
        ans.append(x)            # hold it to the numerator list
        n, d = x * n - d, d * x  # update the remainder to n and d
    for a in ans:
        print("1/{}".format(a), end=" ")

def main():
    print("Greedy Algorithm to Compute Egytian Fractions")
    stay = True
    while stay:
        n = int(input("Enter the numerator: "))
        d = int(input("Enter the denominator: "))
        egyptian(n, d)
        stay = ("n" != (input("\nCompute another? (no to stop) ")+" ")[0])

main()

