#import the modules for the game
import control#Manages stats, inventory and actions
import time#import the time module
import mapMod#manages the gui
import random#import the random module
import csv#import the csv module to store scores
#Inventory Category Indexes
#0 - Materials
#1 - Tools
#2 - Food

firstRun = 1
running = 1

#The blank function is added to decrease the chance of getting an event
def blank():
    print()

#Create a list to store the random events that may occur
randomFunctions = [control.randomEvent7, control.randomEvent1, control.randomEvent2, control.randomEvent3, control.randomEvent4, control.randomEvent5, control.randomEvent5, control.randomEvent5,control.randomEvent6,control.randomEvent6, control.randomEvent6,control.randomEvent7,control.randomEvent7, control.randomEvent7, blank, blank, blank, blank, blank, blank, blank, blank, blank]


#Main menu function
def mainMenu():
    global mainAnswer
    print('''
           __          __  _                            _                    
           \ \        / / | |                          | |                   
            \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___              
             \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \             
              \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  _   _   _ 
               \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  (_) (_) (_)
                 _______ _    _ ______    _____          __  __ ______       
                |__   __| |  | |  ____|  / ____|   /\   |  \/  |  ____|      
                   | |  | |__| | |__    | |  __   /  \  | \  / | |__         
                   | |  |  __  |  __|   | | |_ | / /\ \ | |\/| |  __|        
                   | |  | |  | | |____  | |__| |/ ____ \| |  | | |____       
                   |_|  |_|  |_|______|  \_____/_/    \_\_|  |_|______|      

''')
    mainAnswer = ''
    print('Would you like to...')#Ask the user what they want to do
    while mainAnswer != 'play' and mainAnswer != 'scores' and mainAnswer != 'exit':#Take only three specific inputs
        print('Play/Scores/Exit')
        mainAnswer = input().lower()#Set their input to lowecase
        
def intro():#Title screen
    print('Move the windows around so you can see both the shell and map')
    print('You wake up alone in the middle of a forest')
    time.sleep(1)
    print('You must survive for as many turns as you can.')
    print('')

def camp():
    global firstRun
    global atCamp
    if firstRun != 1 and atCamp != 1:#If the user is playing for the first time, it won't give them a random event.
        time.sleep(1)
        random.choice(randomFunctions)()#Choose a random event from the event list and call that function
    atCamp = 0
    firstRun = 0#Set first run to 0
    mapMod.updateStats()#Call the mapMod.updateStats function to update the stats that are displayed in turtle
    global action
    global running
    global rounds
    control.rounds = control.rounds +1# add 1 to the rounds survived
    action = ''
    if control.hp >=1: #If the user hasn't died yet
        if control.hunger < 20:#If the hunger/thirst is less than 20, the user will take damage.
            print('You are very hungry, and take 5 damage')
            control.hp = control.hp - 10
        if control.thirst < 20:
            print('You are very thristy, and take 5 damage')
            control.hp = control.hp - 5
        print("You return to your campsite")
        while action != 'hunt' and action != 'gather' and action != 'craft' and action != 'cook' and action != 'rest' and action != 'consume':#Ask the user what they want to do, only take specific input
            print("What would you like to do?")
            print("hunt, gather, craft, cook, rest, consume")
            action = input()
        print("You decide to", action)
        time.sleep(1)

def scoresD():# Display the scores from previous games
    global reader
    global row
    with open ('survivalScores.csv', 'rt') as csvfile:#Open the csv file
        reader = csv.reader(csvfile)#Create a reader to read the file
        for row in reader:# For the rows in the file
            if '' not in row:
                if len(row) == 0:
                    continue#If row is empty, skip it.
                elif len(row) > 0:# Print the row
                    print(row)
    return

scores = [['']]#Scores list to store the score when the user dies

mainMenu()#Run mainMenu
while mainAnswer == 'scores':# if the user wants to see scores...
    scoresD()#Display the sores
    while mainAnswer != 'play' and mainAnswer != 'exit':#Ask what they want to do
        print('Play or Exit?.')
        mainAnswer = input().lower()
    
while mainAnswer == 'play':#If the user wants to play
    intro()#Run the intro
    while running == 1:#Main game loop
        camp()#Go to camp to determine what the user wants to do, and update the user's stats
        {#Use a dictionary to determine which function to call based on the user's selected action
        'hunt': control.hunt,
        'gather': control.gather,
        'craft': control.craft,
        'cook': control.cook,
        'rest': control.rest,
        'consume': control.consume,
        }.get(action)()#Take the user's input, and run the function from the dictionary
        if action != 'hunt' and action != 'gather':
            atCamp = 1
        print("\n")
        if control.hp <= 0:#If the uer has died...
            print('¯\_(ツ)_/¯ You died! ¯\_(ツ)_/¯')  
            print('You survived', control.rounds, 'turns.')#Display how many rounds they survived
            print('Please type your name.')
            userName = input()#Take their name to display their score
            addUser = [userName+': '+str(control.rounds)]# Add the score to the end of their name
            scores.append(addUser) # Appends the score list with the inputted user name
            print(scores) # Prints the score
            #
            fl = open('survivalScores.csv', 'a') # Opens the score csv file
            writer = csv.writer(fl) # Creates a writer to write in the csv file
            for values in scores:# For the values in the score list...
                writer.writerow(values) # Write the scores in 
            fl.close() # Close the file
            #
            time.sleep(1)
            print('Would you like to try again?')
            input()
            print('just kidding no time to create play again, restart the program yourself :C :C :C')
            break
