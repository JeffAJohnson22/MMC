# Cookies
cookie = 10
profitPerCookie = 150  # Profit per cookie box
totalProfitPerCookie = profitPerCookie * cookie
flourPerCookie = 4
milkPerCookie = 5
totalFlourForCookies = flourPerCookie * cookie
totalMilkForCookies = milkPerCookie * cookie
print("Total profit from cookies if all 10 are made: ${}".format(totalProfitPerCookie))
print("Total flour used for 10 cookies: {} packs".format(totalFlourForCookies))
print("Total milk used for 10 cookies: {} jugs\n".format(totalMilkForCookies))

# Muffins
muffin = 10
profitPerMuffin = 100  # Profit per muffin box
totalProfitPerMuffin = profitPerMuffin * muffin
flourPerMuffin = 3
milkPerMuffin = 1
totalFlourForMuffins = flourPerMuffin * muffin
totalMilkForMuffins = milkPerMuffin * muffin
print("Total profit from muffins if all 10 are made: ${}".format(totalProfitPerMuffin))
print("Total flour used for 10 muffins: {} packs".format(totalFlourForMuffins))
print("Total milk used for 10 muffins: {} jugs\n".format(totalMilkForMuffins))

# Constraints
maxFlour = 80
maxMilk = 80

maxProfit = 0
bestCookie = 0
bestMuffin = 0

# Loop to find best combination under constraints
for cookie in range(0, 27):  # Reasonable upper bound for search
    for muffin in range(0, 27):
        flourUsed = (4 * cookie) + (3 * muffin)
        milkUsed = (5 * cookie) + (1 * muffin)
        if flourUsed <= maxFlour and milkUsed <= maxMilk:
            profit = (150 * cookie) + (100 * muffin)
            if profit > maxProfit:
                maxProfit = profit
                bestCookie = cookie
                bestMuffin = muffin

# Output optimal combination
print("Best number of cookies: {}".format(bestCookie))
print("Best number of muffins: {}".format(bestMuffin))
print("Maximum profit: ${}".format(maxProfit))
