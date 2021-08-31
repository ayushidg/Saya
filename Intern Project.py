# how much water the customer uses per billing period

#billing formula



    
#size of the water service connection and the cost
waterConnection = [ "inch" : "cost", 0.625 : 30.52, 1:46.63, 1/2 : 86.90, 2: 135.22, 3:247.98, 4:409.06, 6:811.76, 8:1939.23, 10:3066.89]

#amount of water used

    #number of residents
 singleFamily = ["tier" : "cost", 1 : 2.68, 2 : 2.75 , 3 : 2.85]
 multiFamily = ["tier" : "cost" , 1: 2.67, 2 : 2.71, 3 : 2.76]
    
    #Agriculture
agriculture = 2.73
    
    #commercial 
commercial = 2.74
    
    #construction
construction = 2.73
    
    #ask the user what size their water service is
connection = input("What size water service connection do you have?)
     #ask for number of residents
residents = input("How many residents in your home?")
     #ask if they use water for agricultural, commercial or construction use
 
def billingFormula(connection, residents, extras):
                      
    
        
                       
                      



monthlyBill = 0 
    



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



#dictionary holding gallons saved based on behavior changes
savedIndoorBehavior = [1:2, 2:13, 3:1.6, 4:5, 5:15, 6:18]


#dictionary holding gallons saved based on internal system changes
savedIndoorHardware = [1:8, 2:10, 3:14, 4:15, 5:30]


#this funcion is for reccomending steps for indoor behavior if indoor behavior is the problem area         
def indoorBehavior(numbers):
    
    print("Based on your water usage data, you should focus on saving water indoors.")
    #we are planning on displaying each tip for water saving in the GUI and having the user choose which tips they want to go through with. This way, the total amount of gallons saved can be calculated and shown.
    
    print(\n)
    goal = input("How many gallons would you like to save?")
    
    #algorithm for giving tips that can satisfy the goal 
    
    #based on the goal amount,  
    
    
    
    
    """
    choice = input("Would you like behavior related tips or hardware related tips?")
    if choice == "behavior" or choice == "Behavior": 
        print("Here are some behavior related tips:")
        print(\n)
        
        print("1. Run the dishwasher only when full. \n 2. Turn water off when not in use (shower, brushing teeth, dishes) \n 3. Do not use the toilet as a wastebasket \n 4. Shorten shower times by 2 minutes \n 5. Turn the washing machine on only when full. \n 6. Fill the bathtub half full while bathing")
        
        print(\n)
        while True:
            numbers = input("Enter the number corresponding to the action you will take to reduce your water usage. When you are finished, enter None")
        #while the user is still entering numbers, add the corresponding gallons saved to the gallonsSaved variable
            gallonSaved = gallonSaved + savedBehavior[int(numbers) - 1]
            if numbers == "None"or numbers == "none":
                break
     elif choice == "Hardware" or choice == "hardware":
        print("Here are tips on how to improve your water system:")
        print(\n)
        
        print("1. Replace old, ineffiecient toilets with newer, better ones. \n 2. Purchase a new front loading clothes washer \n 3. Install aerators with flow restrictors on kitchen/bathroo, faucets \n 4. Fix a leaky faucet \n 5. Fix a leaky toilet")
        
        print(\n)
        while True:
            numbers = input("Enter the number corresponding to the action you will take to reduce your water usage. When you are finished, enter None")
        #while the user is still entering numbers, add the corresponding gallons saved to the gallonsSaved variable
            gallonSaved = gallonSaved + savedBehavior[int(numbers) - 1]
            if numbers == "None"or numbers == "none":
                break
      else:
        print("Invalid input, please try again.")
      """ 
        
          
   
   
 #dictionary holding gallons saved based on behavior changes         
savedOutdoorBehavior = [1:20, 2:20, 3:22, 4:25, 5:100] 
#dictionary holding gallons saved based on internal system changes
savedOutdoorHardware = [1:5, 2:]
    
    
    
    
#this is outdoor behavior, same as indoor ^
          
def outdoorBehavior():
    print("Based on your water usage data, you should focus on saving water outdors.")
    print(\n)
    
    goal = input("How many gallons would you like to save?")
    
    
    
    """
    choice = input("Would you like behavior related tips or hardware related tips?")
       if choice == "behavior" or choice == "Behavior": 
            print("Here are some behavior related tips:")
            print(\n)
            print("1. Water your yard before 6 am or after 8 pm to reduce evaporation \n 2. Adjust sprinklers to reduce spray on sidewalks or other areas that don't need water \n 3. Use a broom instead of a hose to clean off driveways or other surfaces \n 4. Add mulch (2"-3") around trees and plants (1,000 sq. ft.) \n 5. Reduce irrigation time by 2 minutes or eliminate one irrigation cycle per week")
            
            
            
          
       elif choice == "Hardware" or choice == "hardware":
            print("Here are tips on how to improve your water system:")
            print(\n)
           print("1. Install a pool cover to reduce evaporation \n 2. Repair pipe leak or broken sprinkler head \n 3. Install water-efficient drip 
   """ 
    
    
    
    
  

# if the user's tier is greater than or equal to 3, then implement L B H
#based on what Saya's algorithm detects, the three variables will either become true or false which will trigger the respective algorithms                      
leaks = False
behavior = False
hotWater = False                    
                      

    
    
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












