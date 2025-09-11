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
        print("1/{}".format(a), end=" \n")

def main():

    arrays = [
        # Task 1
        [5, 6],     # 1/2, 1/3
        [7, 15],    # 1/3, 1/8, 1/120
        [23, 34],   # 1/2, 1/6, 1/102
        [121, 321], # 1/3, 1/23, 1/7383
        [5, 123],   # 1/25, 1/1538, 1/4729350

        # Task 2
        # For the following value I noticed a slight difference between what I got and the manually calculated result on slide 18.
        [5, 121],   # 1/25, 1/757, 1/763309, 1/873960180913, 1/1 527 612 795 642 093 385023488
    ]
    for x in arrays:
        egyptian(x[0], x[1])

main()

