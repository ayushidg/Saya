# how much water the customer uses per billing period


monthlyBill = 0 #total gallons used by user divided by 1,000 and multiplied by the price per gallon
#function for finding monthly bill
def monthlyBillCalculator(monthlyBill, totalUsage):
    bill = (totalUsage / 1,000) * 0.006
    monthlyBill = monthlyBill + bill
    return monthlyBill
    



#this function allows us to rank water users so we can reccomend what actions to take based on how effecient they are with their water usage
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

#based on what tips the user selects, the gallons they save will be added to the variable below and displayed later
gallonsSaved = 0 #total gallons saved from water saving tips

#dictionary to hold steps and how many gallons they will save (this may be removed in future, its just some internal shtuff)
indoorSteps = []


#if the user choose gray water as their problem area then use the function below

def grayWater():
    #have the user indicate which actions they are going to take 
    print("Please indicate which steps you will take to reduce your gray water usage.")
    
    #print out the different steps that the yser can take to reduce their water usage
    print("Steps printed here.")
    
    stepsTaken = input("Please enter the number corresponding to the step you wish to take. If you do not want to try any of these tips, type Next.")
    #based on whichever steps they would like to take, a variable will hold the number of gallons they will save by taking those steps
    for item in indoorSteps:
        if stepsTaken != "Next":
            

 #this funcion is for reccomending steps for indoor behavior if the user selects indoor behavior as their problem area         
def indoorBehavior():
    areaFocus = input("What system would you like tips for?"+\n+"1. Gray Water" #add other options when known )
    if location == "gray water":
        print("Based on your usage data, your gray water system is consuming lots of water." + \n +  "To lower your tier below 2, please take some of the following steps:" + \n + "tips for indoor usage, formatting done later")
    
 
#this is outdoor behavior, same as indoor ^
def outdoorBehavior():
    #tips for outdoor usage, same as above function
    
    
    
    
    
    
  

# if the user's tier is greater than or equal to 3, then implement L B H
if tier == 1:
    print("You are efficient with your water usage.")


if tier >= 3:
    if leaks == True:
        #put code for leaks
    elif behavior == True:
        #use the function for recommending behavior
    elif hotWater == True:
        #code for hot water
        



leaks == False
#if there is a sudden spark in water usage, then leaks will become True, this data will be supplied to us via Saya
if leak == True:
    #code for leaks

behavior == False
#if the user is using too much water, then reccomend good behavior. This can be determined by the tier ranking of users
if tier >= 3:
    behavior == True
    indoor == False
    if indoor == True:
        
    #if user indicated where 
    outdoor == False
    
    
# h=hot water
hotWater = False



totalSavings = #return to later
waterRates = [1.47, 2.00, 4.86, 13.63]


def moneySaved(tier, totalSavings):
    moneySaved = totalSavings * waterRates[tier - 1]
    return moneySaved












