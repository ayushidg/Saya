# how much water the customer uses per billing period


monthlyBill = 0 #code formula for determining monthly bill later

def tier(totalUsage, monthlyBill):
    # cost of water is $0.006/gallon
    cost = totalUsage * 0.006
    usagePercent = [(monthlyBill - cost) // monthlyBill] * 100
    if usagePercent <= 40:
        return 1
    elif usagePercent <= 100:
        return 2
    elif usagePercent <= 140:
        return 3
    else:
        return 4



# if the user's tier is greater than or equal ro 3, then implement L B H
# l = leaks
l = 0
# b=behavior
b = 0
# h=hot water
h = 0

totalSavings = l + b + h

waterRates = [1.47, 2.00, 4.86, 13.63]


def moneySaved(tier, totalSavings):
    moneySaved = totalSavings * waterRates[tier - 1]
    return moneySaved

