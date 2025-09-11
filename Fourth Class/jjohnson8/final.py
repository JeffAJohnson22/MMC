import random
def alea():
    import random
    arr = []
    for _ in range(333):
        arr.append(2)
    for _ in range(333):
        arr.append(3)
    for _ in range(334):
        arr.append(4)
    random.shuffle(arr)
    return arr

def pick(a):
    index = random.randint(0, len(a) - 1)
    if a[index] == 2:
        return index
    else:
        return None 
        
# Test the functions
arr = alea()
index = pick(arr)
if index is not None:
    print(f"Value at index {index}: {arr[index]}")
else:
    print("No value found (index is None)")
