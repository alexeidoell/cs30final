# Alexei and Salahuddin
# 6 Apr 2022
# AP CSP 30 Final Project

import os
import dialogue

class Evidence(object):
    '''
    Current plan is have folder with item descriptions txt files
    '''
    def __init__(self, name ='', type=''):
        self.name = name
        self.type = type
        self.desc = open('./evidencedesc/' + self.name + '.txt', 'r')
        self.desc.close


    def displayDesc(self):
        desc = self.desc.readlines()
        for i in range(len(desc)):
            desc[i] = desc[i].rstrip('\n')
        dialogue.dialoguePrint(desc)

    def __eq__(self, other): 
        if not isinstance(other, Evidence):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name and self.type == other.type and self.desc == self.desc

class trueEvidence(Evidence):
    '''

    '''
    def __init__(self, name=''):
        Evidence.__init__(self, name, 'true')

class normalEvidence(Evidence):
    '''

    '''
    def __init__(self, name=''):
        Evidence.__init__(self, name, 'normal')
