#Action functins
#Hunt
#Cook
#Gather
#Craft
#Rest
import time
import random
import re
import craftingMod
import mapMod
#Inventory Indexes
#Index 0: Materials
#Index 1: Tools
#Index 2: Food
inv = [[], [], [], []]#A list is used for the user's inventory
hp = 85# The user's hp, thirst and hunger stats
thirst = 75
hunger = 75
#Huntable animals and items to be appended
hunteds = ['raw rabbit', 'raw squirrel', 'raw bear', 'raw jaguar']
animals = ['a rabbit', 'a squirrel', 'a bear', 'a jaguar', 'nothing']
animalPercent = [60, 50, 10, 15, 0]
#Gatherable materials in the following locationshunger = hunger-5
materialCave = ['stone', 'some ore']
materialForest = ['twig', 'leaf', 'wood', 'wood', 'wood']
materialLake = ['lake water']
#Cookable items
cookables = ['rabbit', 'squirrel', 'bear', 'jaguar']
craftable = []

hasAxe = 0
hasLight = 0

campsite = ['nothing']#Used to determine what is in the user's camp
firepitWood = 0# Usedto store the amount of firewood inside the firepit

hunger = hunger-5
rounds = 0#Stores the rounds the user has survived

#Hunting function
def hunt():
    global hunted
    global hunger
    global thirst
    global hp
    if 'spear' in inv[1]:#If the user has a spear in their inventory, they will have a better chance to kill animals
        spearPercent = 20
    else:
        spearPercent = 0
    print('You begin hunting')
    time.sleep(1)
    print('.', end = '')#Add ... to the end of the string
    time.sleep(1)
    print('.', end = '')
    hunger = hunger-5
    time.sleep(1)
    print('.')
    time.sleep(1)
    indexAnimal = random.randint(0,4)#Randomly select a index for what the user finds
    animal = animals[indexAnimal]#Set the animal the user finds using the random index
    huntPercent = animalPercent[indexAnimal]+spearPercent#Set the percent the user has to kill that animal by using the created lists
    print('You stumble upon..', animal)
    #If the user has actually found an animal..
    if animal != 'nothing':
        huntPick = ''
        while huntPick != 'yes' and huntPick != 'no':#Does the user want to try to kill it?
            print('Would you like to attack it?')
            print('You have a', huntPercent, '% chance to kill it')
            huntPick = input().lower()
        if huntPick == 'yes':#If the user wants to kill the animal
            attacking = random.randint(0, 100)#Roll a number that determines if the user kills he animal or not.
            if attacking <= huntPercent:#If the user kills it...
                hunted = hunteds[indexAnimal]#
                print('You killed a', animal, 'and obtained', hunted)
                inv[2].append(hunted)
            else:
                print('After struggling with the', animal, 'you \nfail to kill it. You take 10 points of damage')#If the user does not kill the animal, they lose 10 hp
                hp = hp-10 
        else:
            print('You walk away from the', animal)#If the user doesn't want to attack the animal, they will leave
    else:
        print('You fail to find anything')
    print('After hunting, you feel hungrier and thirstier')
    hunger = hunger-5#User becomes more thirsty and hungry after completing actions
    thirst = thirst-5
        
def gather():
    global hunger
    global thirst
    global location
    location = ''
    while location != 'forest' and location != 'lake' and location != 'cave':#Ask the user where they want to gather materials
        print('Where would you like to gather?')
        print('forest, lake, cave')
        location = input()
    if location == 'forest':#If they pick forest
        mapMod.updateMap()#Update the map to display their location
        print('You begin to gather at the forest', end = '')
        time.sleep(1)
        print('.', end = '')
        time.sleep(1)
        print('.', end = '')
        time.sleep(1)
        print('.')
        if 'axe' in inv[1]:#If the user has a axe, they have a chance to recieve wood.
            gathered = materialForest[random.randint(0,4)]
        else:
            gathered = materialForest[random.randint(0,1)]#Else, they recieve twigs and leaves
    elif location == 'lake':#If they pick lake
        mapMod.updateMap()#Update the map to display their location
        print('You begin to gather at the lake')
        if 'woodenbucket' in inv[1]:#If they have a bucket, they may gather lakewater
            print('Using your bucket, you gather some lake water.')
            print('You should probably boil this before drinking it..')
            gathered = materialLake[0]
        else:#Else, they recieve nothing.
            print('If only you had a bucket to gather water..')
            gathered = 'nothing'
    elif location == 'cave':#If the user picks cave
        mapMod.updateMap()#Update their position
        print('You begin to gather at the cave')
        if hasLight == '1': 
            print('You venture into the cave using your torch')
            gathered = materialCave[1]
        else:
            print('The cave is pitch black, so you decide to stay outside.')
            print('You gather rocks outside the caves.')
            gathered = materialCave[0]
    if location != 'lake':#The program must determine if the user was at the lake or not, as this will change which part of the inventory must be appeneded to.
        for i in range(0, random.randint(1, 4)):#Repeat the following code for a random amount of times to add a random amount of the item to the user's inventory
            inv[0].append(gathered)#Add to the inventory
        print('You managed to get some...', gathered)
    else:
        inv[2].append(gathered)#Add lake water to the users inventory
        print('You managed to get some...', gathered)
    print('After gathering, you feel hungrier and thirstier')
    hunger = hunger-5
    thirst = thirst-5
    print('You begin walking back to your campsite', end = '')
    time.sleep(1)
    location = ''
    mapMod.updateMap()
    print('.', end = '')
    time.sleep(1)
    print('.', end = '')
    time.sleep(1)
    print('.')

def craft():
    global hunger
    global thirst
    print('Your materials:')
    print(inv[0])
    print()
    craftingMod.checkInv()#Run the checkInv function from the craftingMod module to determine what items the user has and what is craftable
    print('Craftable items:')
    print(craftable)#Print the craftable items the user has that is generated from checkInv
    print()
    wantCraft = ''
    wantItem = ''
    while wantCraft != 'yes' and wantCraft != 'no':#If the user wants to craft..
        if len(craftable) >= 1:#if there are iems in craftable..
            print('Would you like to craft a item?')
            print('yes, no')
            wantCraft = input().lower()
        else:#if the user has no craftable items
            print('You have no craftable objects.')
            return
    if wantCraft == 'yes' or wantCraft == 'Yes':#If they choose to craft
        while wantItem not in craftable:#Determine what item they want to craft. They must type a string that is in craftable
            print('Which item would you like to craft?')
            print(craftable)
            wantItem = input()
        for i in range(len(craftable)):#Search through the craftable list
            if wantItem == craftable[i]:#If the item they want is in the list
                inv[1].append(craftable[i])#Add the item to their inventory
        print('You crafted a', wantItem)
        {#Create a dictionary to store the craftable items. Each item is assigned a function name from the craftingMod module.
        'firepit': craftingMod.firepit,
        'axe': craftingMod.axe,
        'spear': craftingMod.spear,
        'bucket': craftingMod.bucket,
        'sleeping bag': craftingMod.sleepingBag,
        }.get(wantItem)()#Get the users input, and run the module corresponding to the item the user picked. The module will determine the materials to be removed.
        craftable[:] = []
        for i in range(craftingMod.amount):#Remove the materials that need to be removed
            inv[0].remove(craftingMod.material)#Remove the materials from the user's inventory
        hunger = hunger - 10
        thirst = thirst - 10
        print('After crafting, you feel a bit hungrier and thirstier.')
                
    else:#If the user does not want to craft
        print('Okay then.')
        craftable[:] = []
        return
        
cookedables = ['bear', 'rabbit', 'squirrel']#A list to store the food that is already cooked.
def cook():
    global firepitWood
    global hunger
    global thirst
    global inv
    invLength = len(inv[2])
    if 'firepit' in campsite:#Determine if the user has a firepit
        if firepitWood <= 1:#If the user has no wood in the firepit, they must add wood to cook.
            woodAdd = ''
            while woodAdd != 'yes' and woodAdd != 'Yes' and woodAdd != 'no' and woodAdd != 'No':
                print('You must add 1 wood to the firepit.')
                print('Add 1 wood?')
                woodAdd = input()
            if woodAdd == 'Yes' or woodAdd == 'yes':
                firepitWood = firepitWood +1
            else:
                print('You must add wood to cook.')
                return
            print('Your food items:')
            print(inv[2])
            chooseFood = ''
            while chooseFood not in inv[2]:#Determine what food the user wants to cook
                print('What would you like to cook?')
                chooseFood = input()
            if chooseFood in cookedables:#If pick something that is already cooked, it cannot be cooked
                print(chooseFood, 'cannot be cooked.')
                cooker = 'no'
            if chooseFood != 'lake water' and chooseFood != 'jazz berry' and chooseFood != 'ded berry':#If they choose to cook raw food
                cooked = chooseFood
                inv[2].remove(cooked)#Remove the food from their inventory
                cooked = re.sub("raw ", "", cooked, count=1)#Make the food to append the original name without raw.
                print('Would you like to cook', chooseFood, '?')
                cooker = input().lower()
            elif chooseFood != 'jazz berry' and chooseFood != 'ded berry':#If the user picks water
                cooked = 'water'
                inv[2].remove(cooked)
                print('Would you like to cook', chooseFood, '?')
                cooker = input().lower()
            else:#If the user picks a uncookable food
                print(chooseFood,'is not cookable.')
                cooker = 'no'#Set cooker to no so nothing gets appended
            if cooker == 'yes':#If they choose to cook
                print('Cooking', cooked)
                print('You now have', cooked)
                inv[2].append(cooked)#Add the item to their inv
                firepitWood = firepitWood -1#Use one firewood and remove it
        hunger = hunger - 10
        thirst = thirst - 10
    else:
        print('You cannot cook without a firepit')

def rest():
    global hp
    global hunger
    global thirst
    print('You decide to rest at your campsite')
    if hp < 100:#If the user has less than 100 hp
        print("You gain 5 hp")
        hp = hp+5#Add 5 hp
        if hp > 100:
            hp = 100
    else:
        print('You rest at your campsite')
        time.sleep(1)
        print('.', end = '')
        time.sleep(1)
        print('.', end = '')
        time.sleep(1)
        print('.')
        time.sleep(1)
    hunger = hunger - 10
    thirst = thirst - 10
    print('After resting, you are a bit hungrier and thirstier.')


def consume():
    global hunger
    global thirst
    global hp
    global inv
    invLength = len(inv[2])
    print('You decide to consume')
    print('Consumable items:')
    if invLength >= 1:
        print('Your food items:')
        print(inv[2])
        chooseFood = ''
        while chooseFood not in inv[2]:
                print('What would you like to consume?')
                chooseFood = input()
        for i in range(0,invLength):
            if chooseFood == inv[2][i]:
                print('You consume the', chooseFood)
                inv[2].remove(chooseFood)
                if 'raw' not in chooseFood and chooseFood != 'water bottle' and chooseFood != 'jazz berry' and chooseFood != 'ded berry':
                    hunger = hunger +10
                    thirst = thirst +5
                    return
                elif chooseFood != 'water bottle' and chooseFood != 'jazz berry' and chooseFood != 'ded berry':
                    hunger = hunger +15
                    thirst = thirst +15
                    hp = hp -10
                    print('You lose health from eating the raw food.')
                    return
                elif chooseFood == 'jazz berry' or chooseFood == 'ded berry':
                    if chooseFood == 'jazz berry':
                        hp = 0
                        print('Jazz berries kill you. Haha.')
                        return
                    else:
                        hp = hp + 5
                        hunger = hunger+10
                        thirst = thirst+10
                        return
                else:
                    thirst = thirst +20
                    return
    else:
        print('You have no consumables')

    
#Random Events
def randomEvent1():
    global inv
    print('Before returning to your camp...')
    time.sleep(1)
    crateChance = ['cooked rabbit', 'water bottle', 'cooked bear', 'cooked squirrel' ]
    print('An airplane flying above you is too heavy and drops a crate to reduce the plane\'s weight.')
    time.sleep(1)
    answer = ''
    while answer != 'yes' and answer != 'Yes' and answer != 'no' and answer != 'No':
        print('Do you want to investigate the crate??')
        answer = input()
    if answer == 'yes' or answer == 'Yes':
        print('You walk towards the crate.')
        time.sleep(1)
        print('You open it to find...')
        print('')
        chosenCrate = random.choice(crateChance)
        time.sleep(1)
        print('7',chosenCrate + 's')
        time.sleep(1)
        if 'cooked' in chosenCrate:
            chosenCrate = chosenCrate.replace('cooked ','',1)
            print(chosenCrate)
        for i in range(7):
            inv[2].append(chosenCrate)
        
    else:
        print('You decide to ignore it.')
    return
def randomEvent2():
    global inv
    global hp
    print('Before returning to your camp...')
    time.sleep(1)
    print('You run into a mysterious human being.')
    time.sleep(1)
    print('You ask him many questions, but he replies to none')
    time.sleep(1)
    print('Suddenly, out of the blue he offers you an abundant amount of supplies.')
    time.sleep(1)
    print('Will you take his offer?')
    choice = input().lower()
    if choice == 'yes':
        print('You agree to take some supplies')
    else:
        print('You run away from the mystery man')
        return
    chance = random.randint(1,3)
    if chance == 1:
        print('He pulls out many different supplies, and gives you 4 water bottles')
        for i in range(4):
            inv[2].append('water bottle')
    else:
        print('He walks towards you, but suddenly punches you in the face!')
        hp = hp - 25
        print('You lose 25 hp')
def randomEvent3():
    global inv
    print('You find what seems to be a wooden bucket.')
    muhBucket = ''
    while muhBucket != 'yes' and muhBucket != 'no':
        print('Take the bucket?')
        print('yes/no')
        muhBucket = input().lower()
    if muhBucket == 'yes':
        print('You take the bucket')
        inv[1].append('woodenbucket')
        return
    else:
        print('You leave the bucket.')
        return        
def randomEvent4():
    global inv
    global hp
    print('You stumble apon a smartphone.')
    time.sleep(1)
    print('You try to take a bite out of it, but it is too hard.')
    time.sleep(1)
    print('You chip a tooth, and loose 5 hp.')
    time.sleep(1)
    print('You decide to chuck the phone into the woods.')
    hp = hp  -5
def randomEvent5():
    global inv
    print('You stumble apon some very large rocks.')
    time.sleep(1)
    print('Unfortunately, you do not even lift.')
    time.sleep(1)
    print('You decide to take two small rocks.')
    for i in range(3):
        inv[0].append('stone')

def randomEvent6():
    global hp
    print('You walk into a snare trap!')
    time.sleep(1)
    for i in range(40):
        print('Hurry! Press ENTER' , 40 - i , 'more times to get out of the snare!')
        print()
        input()
    print()
    print()
    print('Yay! You escaped from the snare, but lost 10 hp in the process.')
    hp = hp - 10
    
def badBerry():
    for i in range(2):
        inv[2].append('jazz berry')

def goodBerry():
    for i in range(2):
        inv[2].append('ded berry')
berryType = [badBerry, goodBerry]

def randomEvent7():
    global inv
    berryAnswer = ''
    berryChance = random.randint(1,2)
    print('You find what seems to be a berry bush.')
    time.sleep(1)
    print('Do you pick the berries?')
    berryAnswer = input().lower()
    if berryAnswer == 'yes':
        random.choice(berryType)()
        
    
    
