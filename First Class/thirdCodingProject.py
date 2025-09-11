def AskData():
    a = float(input("Enter a scale factor number: "))
    r = float(input("Enter the common ratio number: "))

    elements = []
    value = 0
    
    def roundDecimal(num):
        if num == int(num):
            return int(num)
        else:
            return round(num, 2)
        
    for i in range(3):
        value = a * (r ** i)
        elements.append(roundDecimal(value))

    if abs(r) < 1:
        sumInfinity = a / (1 - r)
        print(f"This GP converges with infinite elements to {roundDecimal(sumInfinity)}")
    else:
        n = int(input("This GP does not converge to a finite number with infinite elements, give me a number: "))
        sumNumber =  a * (r ** n - 1) / (r - 1)
        print(f"This GP sum with {n} elements is equal to {roundDecimal(sumNumber)}")

    print(f"The first elements are {elements[0]}, {elements[1]}, and {elements[2]}")

AskData()
