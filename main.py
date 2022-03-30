# Alexei Doell and Salahuddin Yunus
# 24 Mar 2022
# AP CSP 30 Final Project

import os
import PIL
import matplotlib.pyplot as plt
import time
import evidence
import dialogue
import pickle


playerStats = {'location' : 'kitchen', 'inventory' : []}



def checkInv():
    # for later B)
    pass

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
    
kitchen()