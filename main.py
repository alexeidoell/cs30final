# Alexei Doell and Salahuddin Yunus
# 04 Apr 2022
# AP CSP 30 Final Project

import os
import PIL
import matplotlib.pyplot as plt
import pickle
import evidence
import dialogue


playerStats = {'location' : 'kitchen', 'inventory' : []}
fork = evidence.trueEvidence('Fork')
wife = evidence.normalEvidence('Wife\'s Body')
window = evidence.trueEvidence('Broken Window')
wife2 = evidence.trueEvidence('Closer examination of wife')
window2 = evidence.normalEvidence('Opened Window')

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
        if sortedList[mid].lower() == name.lower():
            return mid
        elif sortedList[mid].lower() > name.lower():
            high = mid - 1
        elif sortedList[mid].lower() < name.lower():
            low = mid + 1
    return False

def checkInv():
    os.system('cls')
    choice = False
    if len(playerStats['inventory']) == 0:
        dialogue.dialoguePrint(('Your inventory is empty.',))
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


def saveGame():
    with open('savefile.txt', 'w') as f:
       pickle.dump(playerStats, f)

def loadGame():
    with open('savefile.txt') as f:
        playerStats = pickle.load(f)


def choices(location):
    # location could be list with attributes of the location (choices available, name of file for image, etc.)
    choice = False
    while choice == False:
        print('1 - Check Location')
        print('2 - Check Inventory')
        print('3 - Leave the area')
        print('4 - Write in your journal')
        for i in range(len(location[1])):
            print(str(i + 5) + ' - ' + location[1][i])
        choice = dialogue.choice(len(location[1]) + 5)

    return int(choice)
    

def kitchen():
    kitchen = ["Kitchen", ["Analyze Body", "Investigate Blood Dripping from LG Smart Refrigerator", "Inspect Broken Window", "Check Leaky Faucet", "Search Opened Drawer"]]
    while True:
        option = choices(kitchen)
        if option == 1:
            location = PIL.Image.open('.\kitchen.png')
            plt.imshow(location)
            plt.show()
        if option == 2:
            checkInv()
        if option == 5:
            if fork not in playerStats['inventory']:
                dialogue.dialoguePrint(('Your wife\'s dead body.', 'Killed within the last 10 minutes.', 'Her eye... where is it?'))
                if wife not in playerStats['inventory']:
                    playerStats['inventory'].append(wife)
                    kitchen[1].append('Check Fork')
            else:
                dialogue.dialoguePrint(('Wait, I forgot to look at her chest.', 'What\'s all this blood?', 'A bullet hole from behind...', 'No conflict.', 'Looks like a murder...'))
                playerStats['inventory'].append(wife2)
        if option == 6:
            dialogue.dialoguePrint(('This fridge looks so gruesome.', 'What could these people have hidden in here to scare me.', 'Oh...', 'It\'s pomegranate juice.'))
        if option == 7:
            dialogue.dialoguePrint(('The window is broken, but from the outside.', 'Looks like a burglary turned wrong.'))
            if window not in playerStats['inventory']:
                playerStats['inventory'].append(window)
        if option == 8:
            dialogue.dialoguePrint(('He left the water on?', 'Nothing special.'))
        if option == 9:
            dialogue
        if option == 10:
            dialogue.dialoguePrint(('Your wife\'s eye is stuck on a fork.', 'Looks like it was gouged out.', 'Doesn\'t seem like that was what killed her though.'))
            if fork not in playerStats['inventory']:
                playerStats['inventory'].append(fork)
            
        os.system('cls')


def livingRoom():
    livingRoom = ["Living Room", ["Check TV", "Look Under Couch", "Search Fireplace", "Investigate Mysterious Pyramid"]]
    while True:
        option = choices(livingRoom)
        if option == 1:
            location = PIL.Image.open('.\livingRoom.png')
            plt.imshow(location)
            plt.show()
        if option == 2:
            checkInv()
#        if option == 5:
#        if option == 6:
#        if option == 7:

            
        os.system('cls')


def bathroom():
    bathroom = ["Bathroom", ["Check Opened Window", "Analyze Footprints", "Inspect Toilet"]]
    while True:
        option = choices(bathroom)
        if option == 1:
            location = PIL.Image.open('./bathroom.png')
            plt.imshow(location)
            plt.show()
        if option == 2:
            checkInv()
        if option == 5:
            if footprints not in playerStats['inventory']:
                dialogue.dialoguePrint(("", "", ""))
                if footprints not in playerStats['inventory']:
                    playerStats['inventory'].append(window2)
            else:
                dialogue.dialoguePrint(("", "", ""))
                playerStats['inventory'].append(wife2)
        if option == 6:
            pass
        if option == 7:
            pass
            
        os.system('cls')



kitchen()