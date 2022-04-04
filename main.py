# Alexei Doell and Salahuddin Yunus
# 04 Apr 2022
# AP CSP 30 Final Project

import os
from re import L
import PIL
import matplotlib.pyplot as plt
import time
import evidence
import dialogue
import pickle

playerStats = {'location' : 'kitchen', 'inventory' : []}
fork = evidence.trueEvidence('Fork')
bruh = evidence.trueEvidence('Bruh')
playerStats['inventory'].extend([fork, bruh])


def checkInv():
    for i in range(len(playerStats['inventory'])):
        print(str(i + 1) + ' - ' + playerStats['inventory'][i].name)

'''
def saveGame():
    with open('savefile.txt', 'w') as f:
       pickle.dump(playerStats, f)

def loadGame():
    with open('savefile.txt') as f:
        playerStats = pickle.load(f)
'''

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
    global operations
    while low <= high:
        operations += 1
        mid = (low + high)//2
        if sortedList[mid].lower() == name.lower():
            return mid
        elif sortedList[mid].lower() > name.lower():
            high = mid - 1
        elif sortedList[mid].lower() < name.lower():
            low = mid + 1
    return False

def choices(location):
    # location could be list with attributes of the location (choices available, name of file for image, etc.)
    choice = False
    while choice == False:
        print('1 - Check Location')
        print('2 - Check Inventory')
        for i in range(len(location[1])):
            print(str(i + 3) + ' - ' + location[1][i])
        print(str(i + 4) + ' - Leave the area')
        choice = dialogue.choice(len(location[1]) + 3)

    return int(choice)
    

def kitchen():
    while True:
        kitchen = ["Kitchen", ["Look at Fork", ]]
        option = choices(kitchen)
        if option == 1:
            fork = evidence.trueEvidence('fork', 'fork.txt')
            if fork not in playerStats['inventory']:
                print('inside his body you find a fork')
                playerStats['inventory'].append(fork)
        for i in playerStats['inventory']:
            i.displayDesc()
    
#kitchen()
checkInv()