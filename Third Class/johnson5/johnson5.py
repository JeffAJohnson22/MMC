def DigitCount(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return 1 + DigitCount(n // 2)

# Test cases
n = 750
print("For {} the count is {}".format(n, DigitCount(n)))
n = 256
print("For {} the count is {}".format(n, DigitCount(n)))


def SumOfSquares(n):
    if n == 1:
        return 1
    else:
        return n**2 + SumOfSquares(n - 1)
    
 # Test cases
n = 12
print("Sum of squares for {} is {}".format(n, SumOfSquares(n)))
n = 20
print("Sum of squares for {} is {}".format(n, SumOfSquares(n)))




