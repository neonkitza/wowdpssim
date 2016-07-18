
class Trigger(object):
    def __init__(self,tt,sid,inc):
        self.triggerType = tt
        self.spellId = sid
        self.increase = inc
        #ako mutateExsisting onda self.increase flip
    
    def mutateExisting(self):
        self.increase = not self.increase
        
    