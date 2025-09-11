# Constants
totalFlour = 80   # packs
totalMilk = 80    # jugs

# Resource requirements
flourPerCookie = 4
milkPerCookie = 5
profitPerCookie = 150

flourPerMuffin = 3
milkPerMuffin = 1
profitPerMuffin = 100

# Brute-force search for best combination
maxProfit = 0
bestCookies = 0
bestMuffins = 0

# Try all possible combinations
for cookies in range(0, totalFlour // flourPerCookie + 1):
    for muffins in range(0, totalFlour // flourPerMuffin + 1):
        usedFlour = (cookies * flourPerCookie) + (muffins * flourPerMuffin)
        usedMilk = (cookies * milkPerCookie) + (muffins * milkPerMuffin)

        if usedFlour <= totalFlour and usedMilk <= totalMilk:
            profit = (cookies * profitPerCookie) + (muffins * profitPerMuffin)
            if profit > maxProfit:
                maxProfit = profit
                bestCookies = cookies
                bestMuffins = muffins

# Output the result
print("Best number of cookie boxes: {}".format(bestCookies))
print("Best number of muffin boxes: {}".format(bestMuffins))
print("Maximum profit: ${}".format(maxProfit))
