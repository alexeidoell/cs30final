# Alexei Doell and Salahuddin Yunus
# 11 Apr 2022
# AP CSP 30 Final Project

import os
import PIL
import matplotlib.pyplot as plt
import json
import jsonpickle
import evidence
import dialogue

# Instantiating our pieces of evidence
fork = evidence.trueEvidence('Fork')
wife = evidence.normalEvidence('Wife\'s Body')
brokenWindow = evidence.trueEvidence('Broken Window')
wife2 = evidence.trueEvidence('Closer Examination of Wife')
openWindow = evidence.normalEvidence('Opened Window')
openWindow2 = evidence.trueEvidence('Revelation of Opened Window')
shoes = evidence.normalEvidence("Spiffy Pair of Ferragamo Plain Toe Oxfords")
poop = evidence.normalEvidence("Toilet Visit Remnants")
phoneCall = evidence.trueEvidence("Last Phone Call With My Wife")

playerStats = {'location' : 'Kitchen', 'inventory' : []}
if os.path.isfile('savefile.txt') and os.path.getsize('savefile.txt') > 0:
    # When game is opened, save file is automatically opened and loaded if it exists
    with open('savefile.txt') as f:
        # Needs to have jsonpickle decode it after json loads it in order to convert it back into an actual proper dictionary

        playerStats = jsonpickle.decode(json.load(f))

def sort(initialList):
    # Other part of mergesort function

    mid = len(initialList) // 2
    leftList = initialList[:mid]
    rightList = initialList[mid:]
    if len(initialList) < 2:
        return initialList
    sortedList = merge(sort(leftList), sort(rightList))
    return sortedList

def merge(list1, list2):
    # Normal merge sort repurposed to work by checking name attribute

    mergedList = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0].name < list2[0].name:
            mergedList.append(list1[0])
            list1.pop(0)
        elif list1[0].name > list2[0].name:
            mergedList.append(list2[0])
            list2.pop(0)
        else:
            mergedList.append(list1[0])
            list1.pop(0)
            mergedList.append(list2[0])
            list2.pop(0)
    if len(list1) != 0:
        mergedList.extend(list1)
    if len(list2) != 0:
        mergedList.extend(list2)
    return mergedList

def binarySearch(name, sortedList):
    # Repurposed binary search for checking name attribute

    low = 0
    high = len(sortedList) - 1
    while low <= high:
        mid = (low + high)//2
        if sortedList[mid].name.lower() == name.lower():
            return mid
        elif sortedList[mid].name.lower() > name.lower():
            high = mid - 1
        elif sortedList[mid].name.lower() < name.lower():
            low = mid + 1
    return None

def picture(image):
    # This function standardizes the setup so that plt.figure() does not need to be written before every single image

    plt.figure(figsize=(20, 10))
    plt.imshow(image)
    plt.show()


def checkClues():
    os.system('cls')
    choice = None
    #if player does not have any evidence, will tell player
    if len(playerStats['inventory']) == 0:
        dialogue.dialoguePrint(('You are clueless.',))
        return
    
    #sorts inventory to be in alphabetical order
    playerStats['inventory'] = sort(playerStats['inventory'])

    #player can choose evidence or continue exploring
    while choice == None:
        #displays each piece of evidence and option to go back to exploring
        for i in range(len(playerStats['inventory'])):
            print(str(i + 1) + ' - ' + playerStats['inventory'][i].name)
        print((i + 2),'- Go Back to Exploring')

        #player must enter full name of clue so that binary search can find it
        choice = input('Please enter name of clue or choose to return to exploring. \n')
        if choice != str(i + 2):
            clueIndex = binarySearch(choice, playerStats['inventory'])
            if clueIndex != None:
                playerStats['inventory'][clueIndex].displayDesc()
            else:
                dialogue.dialoguePrint(('Invalid clue name',))
            choice = None


def saveGame():
    save = jsonpickle.encode(playerStats)
    # Uses jsonpickle and json to encode our player stats dictionary
    # Without jsonpickle, json can't properly dump complicated structures like objects

    with open('savefile.txt', 'w') as f:
       json.dump(save, f)


def clearSave():
    # Simply deletes the save file
    if os.path.isfile('savefile.txt'):
        os.remove('savefile.txt')


def choices(location):
    # Location is a list with options (things to investigate in the scene)
    # choices() prints some general actions, then location specifics
    print('1 - Check Location')
    print('2 - Check Clues')
    print('3 - Leave The Area')
    print('4 - Write In Your Journal (Save)')
    print('5 - Take A Break (Quit)')

    for i in range(len(location[1])):
        print(str(i + 6) + ' - ' + location[1][i])
    
    choice = dialogue.choice(len(location[1]) + 6)
    return choice
    

def titleScreen():
    userChoice = None
    while userChoice == None:
        print("The Pyramid\n")
        if os.path.isfile('savefile.txt'):
            # Checks for if a savefile is present, and that determines whether or not the option 'load game' is printed

            print("1 - New Game")
            print("2 - Load Game")
            print("3 - Quit")
            userChoice = dialogue.choice(3)
            
            #if new game is chosen
            if userChoice == 1:
                os.system('cls')
                clearSave()
                
                # Sets up a blank slate save file in the starter position of the kitchen, with no evidence 
                playerStats['location'] = 'kitchen'
                playerStats['inventory'].clear()
                prologue()
                
            #if load game is chosen
            elif userChoice == 2:
                os.system('cls')
                gameState()

            #if quit is chosen
            elif userChoice == 3:
                os.system('cls')
                quit()
        else:
            print("1 - New Game")
            print("2 - Quit")
            userChoice = dialogue.choice(2)

            #if new game is chosen
            if userChoice == 1:
                os.system('cls')
                prologue()

            #if quit is chosen
            elif userChoice == 2:
                os.system('cls')
                quit()


def prologue():
    #opening dialogue sequence
    dialogue.dialoguePrint(("- THE PRECINCT -\nTIME: 10:45 PM","Jesus, what a long day at work.", "I could not be more tired.", "I better pack up.", "Can't wait to get home and crack open a cold beer.", "*sigh*", "This case has been getting nowhere.", "Multiple homicides within the last 2 weeks, all suspected to have been done by the same person.", "Who the hell uses utensils to murder someone?!?!!??", "Whatever it is, they must be sending a message of some sort.", "Not like it matters much to me anyways, cases like this always go cold, no matter the detective.", "...", "Shit, where the hell did I put my keys?", "Oh.", "*car starts*", "It sure as hell is rainy outside.", "Welp, better listen to my wife and drive safely for once.", "8 MINUTES LATER", "*phone rings*", "Huh, its the wife. Better let her know that I'm already on my way home.", '"Hey honey, where are you? It\'s pouring cats and dogs outside and it\'s really late."', '"Sorry sweetie, I didn\'t expect to get held up this late. I\'m on my way home right now, I\'ll be there soon."', '"Okay, I was just worried. Man, it\'s cold. Did you open the window when you left? I just closed them all."', '"Its really weird though, I\'ve been hearing these strange noises all night. It mostly sounds like rustling leaves, but there\'s also the occasional scratching sort of noise."', '"I\'m sure it\'s nothing sweetie. It\'s probably just our neighbour walking their dog or something. If it gives you any comfort Sakura-chan, I\'m around 3 minutes away. I\'ll be there soon."', '"Okay honey, See you soon."', "*hangs up*", "Jeez, she seems to be really worried. Better hurry home.", "3 MINUTES LATER", "*beep beep*", "Phew, I'm so glad to be home.", "Can't wait to give the wifey a kiss on the cheek.", "*begins to unlock door*", "Huh, what was that loud noise? Sounds like shuffling...", "*opens door*", '"Sakura-chan?"', '"Where are you sweetie?"', '*slowly creeps into kitchen*','"Oh."', '"My."', '"God."'))

    #game sequence begins
    gameState()   


'''
COMMENTS FOR KITCHEN(), LIVINGROOM(), AND BATHROOM() FUNCTIONS
--------------------------------------------------------------
Below, our 'location' functions are written. They all work the same way, basically having a list with options to choose from by the player, and then checking all the possible choices.
First few are generic common tasks like saving, checking an image of the location, moving to another location, or quitting.
Beyond that, there is unique text and evidence, but the overall structure is the same for almost every action.
Some will check for other pieces of evidence and give you new actions or new dialogue/evidence, an example of this is getting the option to check the fork, which then gives you new dialogue when checking the body.
The reason we have the generic options essentially copy and pasted between each function is that we believed it worked better with the implementation of our choices() function, and we wanted to keep choices and results separate.
'''


def kitchen():
    kitchen = ["Kitchen", ["Analyze Body", "Investigate Blood Dripping From LG Smart Refrigerator", "Inspect Broken Window", "Check Leaky Faucet", "Search Opened Drawer"]]
    locationLoop = True
    while locationLoop == True:
        if wife in playerStats['inventory'] and 'Check Fork' not in kitchen[1]:
            kitchen[1].append('Check Fork')
        os.system('cls')
        print(kitchen[0])
        option = choices(kitchen)
        os.system('cls')
        if option == 1:
            location = PIL.Image.open('.\scenes\kitchen.png')
            picture(location)
        if option == 2:
            checkClues()
        if option == 3:
            locationLoop = False
        if option == 4:
            dialogue.dialoguePrint(('You write your thoughts down in your journal...',))
            saveGame()
        if option == 5:
            dialogue.dialoguePrint(('Are you sure you would like to quit? (You will lose any unsaved progress)',))
            userChoice = None
            while userChoice == None:
                print('1 - Yes')
                print('2 - No')
                userChoice = dialogue.choice(2)
                if userChoice == 1:
                    os.system('cls')
                    quit()
        
        #if player analyzes body
        if option == 6:
            if fork not in playerStats['inventory']:
                dialogue.dialoguePrint(('It\'s...', 'Sakura-chan.', 'Who could\'ve done such a thing...', 'Her eye... where is it?', 'Jesus...', 'It\'s been stabbed with a fork...'))
                if wife not in playerStats['inventory']:
                    dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -",))
                    playerStats['inventory'].append(wife)
            else:
                dialogue.dialoguePrint(('Wait, I forgot to look at her chest.', 'What\'s all this blood?', 'A bullet hole from behind...', 'No conflict.', 'Looks like a murder...'))
                if wife2 not in playerStats['inventory']:
                    dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -",))
                    playerStats['inventory'].append(wife2)

        #if player investigates blood dripping from LG Smart Refrigerator
        if option == 7:
            dialogue.dialoguePrint(('This fridge looks so gruesome.', 'What could these people have hidden in here to scare me?', 'Oh...', 'It\'s pomegranate juice.'))

        #if player inspects the broken window
        if option == 8:
            dialogue.dialoguePrint(('The window is broken, but from the outside.', 'Was this a burglary gone horribly wrong?'))
            if brokenWindow not in playerStats['inventory']:
                dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -",))
                playerStats['inventory'].append(brokenWindow)

        #if player checks the leaky faucet
        if option == 9:
            dialogue.dialoguePrint(('He left the water on?', 'Nothing special.'))
            
        #if player searchs the opened drawer
        if option == 10:
            dialogue.dialoguePrint(('Nothing\'s missing from our cutlery except a fork.',))

        #if player chooses to pick the new option that appears after analyzing body, check fork
        if option == 11:
            dialogue.dialoguePrint(('My wife\'s eye is stuck on a fork.', 'Looks like it was gouged out.', 'What the fuck...', 'Doesn\'t seem like that was what killed her though.'))
            if fork not in playerStats['inventory']:
                dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -",))
                playerStats['inventory'].append(fork)        


def livingRoom():
    livingRoom = ["Living Room", ["Check TV", "Look Under Couch", "Search Fireplace", "Investigate Mysterious Pyramid"]]
    locationLoop = True
    while locationLoop == True:
        os.system('cls')
        print(livingRoom[0])
        option = choices(livingRoom)
        os.system('cls')
        if option == 1:
            location = PIL.Image.open('.\scenes\livingRoom.png')
            picture(location)
        if option == 2:
            checkClues()
        if option == 3:
            locationLoop = False
        if option == 4:
            dialogue.dialoguePrint(('You write your thoughts down in your journal...',))
            saveGame()
        if option == 5:
            dialogue.dialoguePrint(('Are you sure you would like to quit? (You will lose any unsaved progress)',))
            userChoice = None
            while userChoice == None:
                print('1 - Yes')
                print('2 - No')
                userChoice = dialogue.choice(2)
                if userChoice == 1:
                    os.system('cls')
                    quit()

        #if player checks TV
        if option == 6:
            dialogue.dialoguePrint(("The TV's still here.",))
            if brokenWindow in playerStats['inventory']:
                dialogue.dialoguePrint(("Wait...", "If it really was a burglary, wouldn't they have taken the TV?",))
            dialogue.dialoguePrint(("Odd...",))

        #if player looks under the couch
        if option == 7:
            dialogue.dialoguePrint(("Nothing weird under the couch.",))

        #if player searchs the fireplace
        if option == 8:
            dialogue.dialoguePrint(("The fire's on...", "She did say it was cold.",))
            if phoneCall not in playerStats['inventory']:
                dialogue.dialoguePrint(( "Wait...", "The phone call!"))
                dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -",))
                playerStats['inventory'].append(phoneCall)

        #if player investigates the pyramid, will trigger ending if all pieces of true evidence have been discovered
        if option == 9:
            count = 0
            for item in playerStats['inventory']:
                if item.type == 'true':
                    count += 1
            #if the player does not have all true evidence
            if count != 5:
                dialogue.dialoguePrint(("What the hell is this pyramid?", "They just left it here..."))
            #if the player has all true evidence, will trigger ending
            else:
                epilogue()

            
        os.system('cls')


def bathroom():
    bathroom = ["Bathroom", ["Analyze Opened Window", "Investigate Shoes in Bathtub", "Inspect Toilet"]]
    locationLoop = True
    while locationLoop == True:
        os.system('cls')
        print(bathroom[0])
        option = choices(bathroom)
        os.system('cls')
        if option == 1:
            location = PIL.Image.open('./scenes/bathroom.png')
            picture(location)
        if option == 2:
            checkClues()
        if option == 3:
            locationLoop = False
        if option == 4:
            dialogue.dialoguePrint(('You write your thoughts down in your journal...',))
            saveGame()
        if option == 5:
            dialogue.dialoguePrint(('Are you sure you would like to quit? (You will lose any unsaved progress)',))
            userChoice = None
            while userChoice == None:
                print('1 - Yes')
                print('2 - No')
                userChoice = dialogue.choice(2)
                if userChoice == 1:
                    os.system('cls')
                    quit()

        #if the player analyzes the opened window
        if option == 6:
            if shoes not in playerStats['inventory']:
                dialogue.dialoguePrint(("The window is open.",))
            if brokenWindow in playerStats['inventory']:
                dialogue.dialoguePrint(("Didn't Sakura-chan say she was gonna close the window?",))
            if openWindow not in playerStats['inventory']:
                dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -", ))
                playerStats['inventory'].append(openWindow)
            else:
                dialogue.dialoguePrint(("He left his shoes here...", "He's still in the house.", "Where are you!?"))
                if openWindow2 not in playerStats['inventory']:
                    dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -",))
                    playerStats['inventory'].append(openWindow2)

        #if the player investigates the shoes in the bathtub
        if option == 7:
            dialogue.dialoguePrint(("There's a pair of Ferragamo Plain Toe Oxfords laying in the bathtub...", "Immaculately placed.", "No scuffs, waxed to perfection.", "I can see my reflection in the shoes.", "Man, I should save up for my own pair.", "Wouldn't be as perfectly kept, but still...", "I just can't stop appreciating these shoes.", "You can really tell this guy cares about his appearance.", "I should ask him/her about them.", "I wonder if he has a nice suit too.", "I can't wait to meet this guy.", "Seems like a put together, well dressed guy.", "I should show my wife these.", "Oh..."))
            if shoes not in playerStats['inventory']:
                dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -",))
                playerStats['inventory'].append(shoes)

        #if the player inspects the toilet
        if option == 8:
            dialogue.dialoguePrint(("Someone forgot to flush!",))
            if poop not in playerStats['inventory']:
                dialogue.dialoguePrint(("- NEW EVIDENCE ACQUIRED -",))
                playerStats['inventory'].append(poop)


def epilogue():
    # final dialogue
    dialogue.dialoguePrint(('This pyramid...', 'There\'s gotta be something bigger going on here.', 'What if the window in the kitchen was a red herring?', 'The shoes.', 'The open window.', 'Nothing stolen.', 'And this damn pyramid.', 'This isn\'t the work of one guy.', 'Who planned all this?', 'MASAKA!!!', 'I\'ve figured out the case!', 'Shit, what\'s that sound behind me?', 'Who\'s there!?', '"Hmph."'))
    
    # will display ending images
    for i in range(1, 13):
        ending = PIL.Image.open('.\scenes\epilogue' + str(i) + '.png')
        picture(ending)
    
    # ending credits
    credit = PIL.Image.open('.\scenes\developers.png')
    picture(credit)
    quit()


def chooseLoc():
    # This function just gives you choices of all the locations to pick from, it's the least complicated part of the switching locations process
    locations = ('Kitchen', 'Bathroom', 'Living Room')
    print('Where would you like to move to?')
    for i in range(len(locations)):
        print(str(i + 1) + ' - ' + locations[i])
    playerStats['location'] = locations[dialogue.choice(len(locations)) - 1]


def gameState():
    # Loops through locations until an endgame flag is triggered and the player is removed from the loop (epilogue() function)
    # After each location it runs the chooseLoc() function in order to change the players current location, then the loop restarts with the new location
    # Will show drawing of location everytime
    while True:
        os.system('cls')
        if playerStats['location'] == 'Kitchen':
            location = PIL.Image.open('.\scenes\kitchen.png')
            picture(location)
            kitchen()
            chooseLoc()
        elif playerStats['location'] == 'Bathroom':
            location = PIL.Image.open('./scenes/bathroom.png')
            picture(location)
            bathroom()
            chooseLoc()
        elif playerStats['location'] == 'Living Room':
            location = PIL.Image.open('.\scenes\livingRoom.png')
            picture(location)
            livingRoom()
            chooseLoc()


titleScreen()

