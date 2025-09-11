def AskData():
    while True: 
        n = int(input("Enter a value:"))
    
        for i in range(n):
            print(' ' * (n - i), end='')
    
            ans = 1
            for j in range(i + 1):
                print(ans, end=' ')
                ans = ans * (i - j) // (j + 1)
            print()
AskData()
