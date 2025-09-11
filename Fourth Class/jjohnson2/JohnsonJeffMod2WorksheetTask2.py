def hanoi(n):
    if n == 0:
        return 0
    else:
        return 2 * hanoi(n - 1) + 1

n = int(input("Enter a number of disks:"))

print("with {} disks you need a minimum of {} movements".format(n, hanoi(n)))