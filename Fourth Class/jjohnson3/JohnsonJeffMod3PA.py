import csv
import os

def knapsack(values, weights, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(values)):
        rwv.append([values[i]/weights[i],weights[i],values[i],i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans   # returns the list of added items

def main(): 
    # Initialize variables   
    values, items, volumes, names = [], [], [], []
    capacity, totalVolume, totalValue = 0, 0, 0
    amountOfItems = {}

    filePath = "./items.csv"
    # Error checking in case the file isnt there or spelled wrong
    if not os.path.exists(filePath):
        print("Check the file path or name.")
        return
    
    # Read the CSV file and populate the lists
    with open(filePath, 'r') as file:
        # Read the CSV file
        reader = csv.reader(file)
        for row in reader:
                
                # Rather than looping through the row, we can unpack the values directly
                name, value, height, width, depth = [item.strip() for item in row]

                # Attach the values to their variables
                names.append(name)
                values.append(int(value)) # casting to int 

                # Calculate the volume and append it to the volumes variable
                # Cubic size is calculated as height * width * depth
                volume = int(height) * int(width) * int(depth)  # casting to int
                volumes.append(volume)

                 # Ask for the capacity of the knapsack
                if capacity == 0:
                    capacity = int(input("Whats the capacity of the knapsack in cubic inches: "))   # casting to int
    
    # Run through the knapsack function to get the answer
    answer = knapsack(values, volumes, capacity)

    # From the answer calculate the total value and total volume of the items in the knapsack
    for i in answer:
        totalValue += values[i]
        totalVolume += volumes[i]

    # Count the number of each item in the knapsack
        if i in amountOfItems:
            # if the item is already in the array, increment its count
            amountOfItems[i] += 1
        else:
            # if the item isnt there start a count for it at 1
            amountOfItems[i] = 1

    # Loop through the amountOfItems
    # Using the items method which gives an object 
    for i, count in amountOfItems.items():
        # A ternary operator to handle single and plural values
        items.append(f"{count} {names[i]}{'s' if count > 1 else ''}")
    items = ", ".join(items)

    # Calculate the space left in the knapsack
    spaceLeft = capacity - totalVolume

    # Print the results
    print(f"The suggested items are: {items} with a total value of ${totalValue}. There were {spaceLeft} cubic inches left unused.")

main()