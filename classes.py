# Alexei and Salahuddin
# 24 Mar 2022
# classes

class Evidence(object):
    '''
    Current plan is have folder with item descriptions txt files

    
    
    '''
    def __init__(self, description='', type=''):
        self.description = description
        self.type = type



class physEvidence(Evidence):
    '''
    
    '''
    def __init__(self, description='', type=''):
        Evidence.__init__(self, description, 'physical')


knife = physEvidence('bruh.txt')

print(knife.type)
