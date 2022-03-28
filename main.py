# Alexei Doell and Salahuddin Yunus
# 24 Mar 2022
# AP CSP 30 Final Project

import os
import PIL
import matplotlib.pyplot as plt
import evidence
import dialogue


testLocation = ['Kitchen', ['Eat mcdonal', 'weaash hand', 'check cutlery', 'kill salah']]
def choices(location):
    
    #location could be list with attributes of the location (choices available, name of file for image, etc.)
    choice = False
    while choice == False:
        print('1 - Check Location')
        for i in range(len(location[1])):
            print(str(i + 2) + ' - ' + location[1][i])
        choice = dialogue.choice(len(location[1]) + 2)

    return choice
    
choices(testLocation)