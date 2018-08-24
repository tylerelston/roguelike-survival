#Crafting
import control # Imports the control module

def checkFirepit(): # Defines the firepit function
    global craftable # Turns craftable global
    count() # Calls the count function to count the materials for the firepit
    if stoneCount >= 5: # If there are 5 stones in the inventory...
        control.craftable.append('firepit') # Append the craftable list in control
        
        
def checkAxe(): # Defines the checkAxe function
    global craftable
    count() # Calls the count function to count the amount of twigs in the inventory
    if twigCount >= 3: # If there are 3 twigs in the inventory...
        control.craftable.append('axe') # Append the craftable list in control
        
        ### These functions are all the same, just defining the rules for crafting each item, and to append the craftable item list. 
        
def checkSpear(): ###
    global craftable
    count()
    if woodCount >= 3:
        control.craftable.append('spear')
        
        
def checkSleepingBag():###
    global craftable
    count()
    if leafCount >= 3:
        control.craftable.append('sleeping bag')
        
        
def checkBucket():###
    global craftable
    count()
    if woodCount >= 4:
        control.craftable.append('bucket')
        

def count():#Checks the user's inventory to see what materials they have and store them in variables
    global stoneCount # Makes each material count variable global
    global woodCount
    global leafCount
    global twigCount
    stoneCount = control.inv[0].count('stone') # Counts the amount of stones in the inventory
    woodCount = control.inv[0].count('wood') # Counts the amount of wood in the inventory
    leafCount = control.inv[0].count('leaf') # Counts the amount of leaves in the inventory
    twigCount = control.inv[0].count('twig') #

def checkInv():#A function used to check the invntory to see what items are craftable
    checkFirepit() 
    checkAxe()
    checkSpear()
    checkSleepingBag()
    checkBucket()
    

def firepit(): #Defines the firepit function
    global material # Turns the needed variables global
    global amount
    global campsite
    if 'nothing' in control.campsite: # If there isnohting in the campsite...
        control.campsite.remove('nothing') # Remove that nothing and
    control.campsite.append('firepit') # Replace it with firepit
    amount = 5 # Sets the amount taken away
    material = 'stone' # Sets the material to be taken away
    
    
def axe(): # Defines the axe function
    global material # Gllllooooobal
    global amount
    amount = 3 # Sets the amount taken away
    material = 'twig' # Sets the material to be taken away
    
    
def spear(): # Defines the spear funciton
    global material # glOoOoOOOoOoBaL
    global amount
    amount = 3 # Sets amount taken away
    material = 'wood' # Sets material to be taken away
    
    
def sleepingBag(): # Sets sleepint bag function
    global material
    global amount
    global campsite
    if 'nothing' in control.campsite: # If there is nothing in the campsite...
        control.campsite.remove('nothing') # Remove that nothing
    control.campsite.append('sleeping bag') # Replace it with a sleeping bag
    amount= 3 # Sets the amount taken away
    material = 'leaf' # Sets material to be taken away
    
    
def bucket(): # I has a bucket
    global material#global
    global amount
    amount = 4 # Sets amount taken away
    material = 'wood' # Sets material to be taken away
