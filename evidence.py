# Alexei and Salahuddin
# 10 Apr 2022
# AP CSP 30 Final Project

import os
import dialogue

class Evidence(object):
    '''
    Evidence objects stored with names, types, and descriptions
    Names are used to open description files
    types are given through inheritence to other objects that simply init as Evidence with certain types
    '''
    def __init__(self, name ='', type=''):
        self.name = name
        self.type = type
        with open('./evidencedesc/' + self.name + '.txt', 'r') as f:
            self.desc = f.readlines()


    def displayDesc(self):
        for i in range(len(self.desc)):
            self.desc[i] = self.desc[i].rstrip('\n')
        dialogue.dialoguePrint(self.desc)

    def __eq__(self, other): 
        # We need this implemented in order to properly compare save data evidence to newly instantiated evidence
        # Without this, evidence stored in the player's inventory after it's loaded in will be considered different evidence to newly instantiated evidence
        # This is because they have different positions/associations within memory, which makes them abstractly equal but strictly equal
        # This method an equality comparison return True if even the name attributes are the same

        if not isinstance(other, Evidence):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name

class trueEvidence(Evidence):
    '''
    Just Evidence but type = 'true'
    '''
    def __init__(self, name=''):
        Evidence.__init__(self, name, 'true')

class normalEvidence(Evidence):
    '''
    Just Evidence but type = 'normal'
    '''
    def __init__(self, name=''):
        Evidence.__init__(self, name, 'normal')
