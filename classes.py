# Alexei and Salahuddin
# 24 Mar 2022
# classes

import os

class Evidence(object):
    '''
    Current plan is have folder with item descriptions txt files

    
    
    '''
    def __init__(self, name ='', description='', type=''):
        self.name = name
        self.description = description
        self.type = type
    
    def displayDesc(self):
        descFile = open('./evidencedesc/' + self.description, 'r')
        desc = descFile.read()
        os.system('cls')
        print(desc)



class physEvidence(Evidence):
    '''
    

    '''
    def __init__(self, name, description=''):
        Evidence.__init__(self, name, description, 'physical')


knife = physEvidence('knife,','knife.txt')

knife.displayDesc()
