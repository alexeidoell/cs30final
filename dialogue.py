# Alexei Doell & Salahuddin Yunus
# 10 Apr 2022
# AP CSP 30 Final Project

import os


#clear screen at beginning to get rid of any unneccessary things for user
os.system('cls')

def dialoguePrint(dialogueList):
    os.system('cls')


    # dialogue is stored in tuples/lists. in order to play out the scene, it iterates through the list of lines
    for i in dialogueList:


        #prints line
        print(i)

        #waits for any input before clearing the terminal
        input('')
        os.system('cls')    



def choice(options):


    #infinite loop, until it gets to a point where the function returns a value
    while True:


        userChoice = input('')


        #as with dialogue(), it always clears after an input. if the input is valid it will return the answer and break the loop, or it will restart and re ask the question
        try:
            userChoice = int(userChoice)
            if userChoice <= options and userChoice > 0:
                return userChoice
        except ValueError:
            os.system('cls')
        return None
