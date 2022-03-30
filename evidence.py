# Alexei and Salahuddin
# 24 Mar 2022
# classes

import os

class Evidence(object):
    '''
    Current plan is have folder with item descriptions txt files
    '''
    def __init__(self, name ='', type=''):
        self.name = name
        self.type = type
    
    def displayDesc(self):
        descFile = open('./evidencedesc/' + self.name + '.txt', 'r')
        desc = descFile.read()
        print(desc)
        descFile.close()



class trueEvidence(Evidence):
    '''

    '''
    def __init__(self, name=''):
        Evidence.__init__(self, name, 'true')


class falseEvidence(Evidence):
    '''

    '''
    def __init__(self, name=''):
        Evidence.__init__(self, name, 'false')

class normalEvidence(Evidence):
    '''

    '''
    def __init__(self, name=''):
        Evidence.__init__(self, name, 'normal')
