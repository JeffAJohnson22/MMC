def AskData():
    username = input("Enter your name:")
    userage = int(input("Enter your age:"))
    currentyear = int(input("What year is it:"))
    print(f"Dear {username} you were born either in {currentyear - (userage + 1)} or {currentyear - userage}")

AskData()