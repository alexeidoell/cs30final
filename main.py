# Alexei Doell and Salahuddin Yunus
# 8 Apr 2022
# AP CSP 30 Final Project

import os
import PIL
import matplotlib.pyplot as plt
import json
import jsonpickle
import evidence
import dialogue


fork = evidence.trueEvidence('Fork')
wife = evidence.normalEvidence('Wife\'s Body')
brokenWindow = evidence.trueEvidence('Broken Window')
wife2 = evidence.trueEvidence('Closer Examination of Wife')
openWindow = evidence.normalEvidence('Opened Window')
footprints = evidence.trueEvidence("Footprints In Bathroom")
openWindow2 = evidence.trueEvidence('Revelation of Opened Window')
shoes = evidence.normalEvidence("Spiffy Pair of Ferragamo Plain Toe Oxfords")
poop = evidence.normalEvidence("Toilet Visit Remnants")

playerStats = {'location' : 'kitchen', 'inventory' : []}
if os.path.isfile('savefile.txt') and os.path.getsize('savefile.txt') > 0:
    with open('savefile.txt') as f:
        playerStats = jsonpickle.decode(json.load(f))

def sort(initialList):
    mid = len(initialList) // 2
    leftList = initialList[:mid]
    rightList = initialList[mid:]
    if len(initialList) < 2:
        return initialList
    sortedList = merge(sort(leftList), sort(rightList))
    return sortedList

def merge(list1, list2):
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


def checkClues():
    os.system('cls')
    choice = None
    if len(playerStats['inventory']) == 0:
        dialogue.dialoguePrint(('You are clueless.',))
        return
    playerStats['inventory'] = sort(playerStats['inventory'])
    while choice == None:
        for i in range(len(playerStats['inventory'])):
            print(str(i + 1) + ' - ' + playerStats['inventory'][i].name)
        print((i + 2),'- Go Back to Exploring')
        choice = input('Please enter name of clue or choose to return to exploring. \n')
        if choice != str(i + 2):
            clueIndex = binarySearch(choice, playerStats['inventory'])
            if clueIndex != None:
                playerStats['inventory'][clueIndex].displayDesc()
            else:
                dialogue.dialoguePrint(('Invalid clue name',))
            choice = None

"""
def checkClues():
    os.system('cls')
    choice = False
    if len(playerStats['inventory']) == 0:
        dialogue.dialoguePrint(('You are clueless.',))
        return
    playerStats['inventory'] = sort(playerStats['inventory'])
    while choice == False:
        for i in range(len(playerStats['inventory'])):
            print(str(i + 1) + ' - ' + playerStats['inventory'][i].name)
        print(str(i + 2) + ' - Go Back to Exploring')
        choice = dialogue.choice(len(playerStats['inventory']) + 6)
    if choice != i + 2:
        playerStats['inventory'][choice - 1].displayDesc()
        choice = False
"""


def saveGame():
    save = jsonpickle.encode(playerStats)
    with open('savefile.txt', 'w') as f:
       json.dump(save, f)


def clearSave():
    if os.path.isfile('savefile.txt'):
        os.remove('savefile.txt')
    else:
        dialogue.dialoguePrint(('Your journal is empty',))


def choices(location):
    # location could be list with attributes of the location (choices available, name of file for image, etc.)
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
        print("TITLE\n")
        if os.path.isfile('savefile.txt'):
            print("1 - New Game")
            print("2 - Load Game")
            print("3 - Quit")
            userChoice = dialogue.choice(3)
            if userChoice == 1:
                os.system('cls')
                clearSave()
                playerStats['location'] = 'kitchen'
                playerStats['inventory'].clear()
                prologue()
            elif userChoice == 2:
                os.system('cls')
                gameState()
            elif userChoice == 3:
                os.system('cls')
                quit()
        else:
            print("1 - New Game")
            print("2 - Quit")
            userChoice = dialogue.choice(2)
            if userChoice == 1:
                os.system('cls')
                gameState()
            elif userChoice == 2:
                os.system('cls')
                quit()


def prologue():
    dialogue.dialoguePrint(("",))
    gameState()   


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
            location = PIL.Image.open('.\kitchen.png')
            plt.imshow(location)
            plt.show()
        if option == 2:
            checkClues()
        if option == 3:
            locationLoop = False
        if option == 4:
            dialogue.dialoguePrint(('You write your thoughts down in your journal.',))
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
        if option == 6:
            if fork not in playerStats['inventory']:
                dialogue.dialoguePrint(('Your wife\'s dead body.', 'Killed within the last 10 minutes.', 'Her eye... where is it?', 'Jesus...', 'It\'s been stabbed with a fork...'))
                if wife not in playerStats['inventory']:
                    playerStats['inventory'].append(wife)
            else:
                dialogue.dialoguePrint(('Wait, I forgot to look at her chest.', 'What\'s all this blood?', 'A bullet hole from behind...', 'No conflict.', 'Looks like a murder...'))
                if wife2 not in playerStats['inventory']:
                    playerStats['inventory'].append(wife2)
        if option == 7:
            dialogue.dialoguePrint(('This fridge looks so gruesome.', 'What could these people have hidden in here to scare me?', 'Oh...', 'It\'s pomegranate juice.'))
        if option == 8:
            dialogue.dialoguePrint(('The window is broken, but from the outside.', 'Looks like a burglary turned wrong.'))
            if brokenWindow not in playerStats['inventory']:
                playerStats['inventory'].append(brokenWindow)
        if option == 9:
            dialogue.dialoguePrint(('He left the water on?', 'Nothing special.'))
        if option == 10:
            dialogue.dialoguePrint(('Nothing missing from our cutlery except a fork.',))
        if option == 11:
            dialogue.dialoguePrint(('My wife\'s eye is stuck on a fork.', 'Looks like it was gouged out.', 'Doesn\'t seem like that was what killed her though.'))
            if fork not in playerStats['inventory']:
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
            location = PIL.Image.open('.\livingRoom.png')
            plt.imshow(location)
            plt.show()
        if option == 2:
            checkClues()
        if option == 3:
            locationLoop = False
        if option == 4:
            dialogue.dialoguePrint(('You write your thoughts down in your journal.',))
            saveGame()
        if option == 6:
            dialogue.dialoguePrint(("A burglary, but they didn't steal the TV?",))
        if option == 7:
            dialogue.dialoguePrint(("Nothing weird under the couch.",))
        if option == 8:
            dialogue.dialoguePrint(("The fire's on...", "She did say it was cold."))
        if option == 9:
            count = 0
            for item in playerStats['inventory']:
                if item.type == 'true':
                    count += 1
            if count != 5:
                dialogue.dialoguePrint((""))
            else:
                dialogue.dialoguePrint((""))

            
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
            location = PIL.Image.open('./bathroom.png')
            plt.imshow(location)
            plt.show()
        if option == 2:
            checkClues()
        if option == 3:
            locationLoop = False
        if option == 4:
            dialogue.dialoguePrint(('You write your thoughts down in your journal.',))
            saveGame()
        if option == 6:
            if shoes not in playerStats['inventory']:
                dialogue.dialoguePrint((""))
                if openWindow not in playerStats['inventory']:
                    playerStats['inventory'].append(openWindow)
            else:
                dialogue.dialoguePrint((""))
                if openWindow2 in playerStats['inventory']:
                    playerStats['inventory'].append(openWindow2)
        if option == 7:
            dialogue.dialoguePrint(("There's a pair of Ferragamo Plain Toe Oxfords laying in the bathtub...", "Immaculately placed.", "No scuffs, waxed to perfection.", "I can see my reflection in the shoes.", "Man, I should save up for my own pair.", "Wouldn't be as perfectly kept, but still...", "I just can't stop appreciating these shoes.", "You can really tell this guy cares about his appearance.", "I should ask him/her about them.", "I wonder if he has a nice suit too.", "I can't wait to meet this guy.", "Seems like a put together, well dressed guy.", "I should show my wife these.", "Oh..."))
            if shoes not in playerStats['inventory']:
                playerStats['inventory'].append(shoes)
        if option == 8:
            dialogue.dialoguePrint(("Someone forgot to flush!",))
            if poop not in playerStats['inventory']:
                playerStats['inventory'].append(poop)


def epilogue():
    pass 


def chooseLoc():
    locations = ('kitchen', 'bathroom', 'living room')
    print('Where would you like to move to?')
    for i in range(len(locations)):
        print(str(i + 1) + ' - ' + locations[i].capitalize())
    playerStats['location'] = locations[dialogue.choice(len(locations)) - 1]


def gameState():
    while True:
        os.system('cls')
        if playerStats['location'] == 'kitchen':
            kitchen()
            chooseLoc()
        elif playerStats['location'] == 'bathroom':
            bathroom()
            chooseLoc()
        elif playerStats['location'] == 'living room':
            livingRoom()
            chooseLoc()


titleScreen()

