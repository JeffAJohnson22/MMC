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
    return ans           # returns the list of added items

# You'll have to uncomment the values, weights, and capacity lists to test the other cases.
def main():
    values = [
        [5, 8, 12], 
        # [3, 5, 7, 11, 13],
        # [5, 6, 7 ,8], 
        # [5, 6, 7 ,8], 
        # [15, 73, 20, 5]
        ]
    weights = [
        [10, 20, 30], 
        # [17, 23, 29, 31, 37],
        # [25, 36, 49, 64], 
        # [25, 36, 49, 64], 
        # [10, 21, 6, 4]
        ]
    capacity = [
        838, 
        # 997,
        # 250,
        # 360, 
        # 500
        ]
    for i in range(len(capacity)):
        answer = knapsack(values[i], weights[i], capacity[i])
    tv, tw = 0, 0
    for a in answer:
        print("Item - Value:", values[i][a], "- Weight:", weights[i][a])
        tv += values[i][a]
        tw += weights[i][a]
    print("Items:", len(answer), "- Value:", tv, "- Weight:", tw)

main()

# Task 3
# For test case 1 ([5,10] [8,20] [12,30]) - capacity 838
# There are 83 instances of item 1: (5, 10), totaling 415 in value and 830 weight.

# For test case 2 ([3,17] [5,23] [7,29] [11,31] [13,37] - capacity 997
# There are 32 instances of item 4: (11, 31), totaling 352 in value and 992 weight.

# For test case 3 ([5,25] [6,36] [7,49] [8,64] - capacity 250
# There are 10 instances of item 1: (5, 25), totaling 50 in value and 250 weight.

# For test case 4 ([5,25] [6,36] [7,49] [8,64] - capacity 360
# There are 14 instances of item 1: (5, 25), totaling 70 in value and 350 weight.

# Task 4
# For test case 5 ([15, 10], [73,21], [20, 6], [5, 4] - capacity 500
# There are 23 instances of item 2: (73, 21)
# There are 2 instances of item 3: (20, 6)
# There is 1 instance of item 4: (5, 4), totaling 1724 in value and 499 weight.
