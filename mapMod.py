import turtle
import control

wn = turtle.Screen()#Create the turtle screen
wn.setup(616,569) # Sets the screen size
player = turtle.Turtle() # Creates the player's turtle 
wn.register_shape("player.gif") # Registers the "kappa.gif" for the turtle's shape
player.shape("player.gif") # Sets the player's turtle shape as the "kappa.gif"
stat = turtle.Turtle() # Creates the turtle that will display the text
stat.penup() # Makes it so that the stat turtle will not create a line behind it
wn.bgpic('map.gif') # Sets the screen backdrop as "map.gif"
player.speed(0.6) # Sets the speed of the player turtle
player.penup() # Makes it so that the player turtle will not not create a line behind it
player.setposition(0, 37)# Sets the player turtle position to the center of the screen
turtle.title("Minimap+Stats")# Titles the turtle window

#Defining player movement functions
def camp():# Based on the chosen location the player chooses, the corresponding function will be called to display movement
    global player
    player.setposition(0, 37)
    return
def forest():
    global player
    player.setposition(150, 145)
    return
def lake():
    global player
    player.setposition(0, -100)
    return
def cave():
    global player
    player.setposition(-235,145)
#def cave():

#def lake():
def updateStats():# Each time the user returns to camp, their inventory and stats will be updated.
    stat.ht()#Makes the stat turtle invisible
    stat.speed(10)#Sets the speed to 10
    wood = str(control.inv[0].count('wood'))# Find the amount of an item the user has by searching through their inventory and counting the items in it, then convert it into a string to be displayed.
    wood = wood + " Wood"

    twig = str(control.inv[0].count('twig'))
    twig = twig + " Twig"

    leaf = str(control.inv[0].count('leaf'))
    leaf = leaf + " Leaf"
    
    stone = str(control.inv[0].count('stone'))
    stone = stone + " Stone"

    spear = str(control.inv[1].count('spear'))
    spear = spear + " Spear"

    axe = str(control.inv[1].count('axe'))
    axe = axe + " Axe"

    torch = str(control.inv[1].count('torch'))
    torch = torch + " Torch"

    woodenbucket = str(control.inv[1].count('woodenbucket'))
    woodenbucket = woodenbucket + " Bucket"

    firepit = str(control.inv[1].count('firepit'))
    firepit = firepit + " Firepit"

    sleepingbag = str(control.inv[1].count('sleepingbag'))
    sleepingbag = sleepingbag + " Sleeping Bag"

    rawrabbit = str(control.inv[2].count('raw rabbit'))
    rawrabbit = rawrabbit + " Raw Rabbit"

    rawsquirrel = str(control.inv[2].count('raw squirrel'))
    rawsquirrel = rawsquirrel + " Raw Squirrel"

    rawbear = str(control.inv[2].count('raw bear'))
    rawbear = rawbear + " Raw Bear"

    cookedrabbit = str(control.inv[2].count('rabbit'))
    cookedrabbit = cookedrabbit + " Rabbit"

    cookedbear = str(control.inv[2].count('bear'))
    cookedbear = cookedbear + " Bear"

    cookedsquirrel = str(control.inv[2].count('squirrel'))
    cookedsquirrel = cookedsquirrel + " Squirrel"

    waterbottle = str(control.inv[2].count('water bottle'))
    waterbottle = waterbottle + " Water Bottle"

    lakewater = str(control.inv[2].count('lake water'))
    lakewater = lakewater + " Lake Water"

    water = str(control.inv[2].count('water'))
    water = water + " Water"
    
    jazzberry = str(control.inv[2].count('jazz berry'))
    jazzberry = jazzberry + " Jazz Berry"
    
    dedberry = str(control.inv[2].count('ded berry'))
    dedberry = dedberry + " Ded Berry"
    
    stat.clear()# Clear the original drawing
    stat.ht() # Hide the turtle
    stat.speed(2)
    stat.setposition(-220, -215) #Move to a specific position, then write the stat or item the user has.
    stat.write(control.hp)
    stat.setposition(-220, -240)
    stat.write(control.hunger)
    stat.setposition(-220, -265)
    stat.write(control.thirst)
    stat.setposition(-180, -205)
    stat.write(wood)
    stat.setposition(-180, -215)
    stat.write(twig)
    stat.setposition(-180, -225)
    stat.write(leaf)
    stat.setposition(-180, -235)
    stat.write(stone)

    stat.setposition(-140, -205)
    stat.write(spear)
    stat.setposition(-140, -215)
    stat.write(axe)
    stat.setposition(-140, -225)
    stat.write(torch)
    stat.setposition(-140, -235)
    stat.write(woodenbucket)
    
    stat.setposition(-100,-205)
    stat.write(rawrabbit)
    stat.setposition(-100,-215)
    stat.write(rawbear)
    stat.setposition(-100,-225)
    stat.write(rawsquirrel)

    stat.setposition(-25, -205)
    stat.write(cookedrabbit)
    stat.setposition(-25, -215)
    stat.write(cookedbear)
    stat.setposition(-25, -225)
    stat.write(cookedsquirrel)
    stat.setposition(-25, -235)
    stat.write(waterbottle)
    stat.setposition(-25, -245)
    stat.write(lakewater)
    stat.setposition(-25, -255)
    stat.write(water)
    stat.setposition(-25, -265)
    stat.write(jazzberry)
    stat.setposition(-25, -275)
    stat.write(dedberry)

    stat.setposition(85,-205) # Display the items the user has at their camp
    campsiteDisplay = str(control.campsite)
    campsiteDisplay = campsiteDisplay.replace("'",'') # Remove brackets from the string
    campsiteDisplay = campsiteDisplay.replace("[",'')
    campsiteDisplay = campsiteDisplay.replace("]",'')
    stat.write(campsiteDisplay)

def updateMap(): # Update the player's location depending on the location they pick to visit
    global player
    if control.location == 'forest':
        forest()
        return
    if control.location == 'lake':
        lake()
        return
    if control.location == 'cave':
        cave()
        return
    else:
        camp()
        return
