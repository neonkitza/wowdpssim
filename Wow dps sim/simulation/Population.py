

from simulation.Individual import Individual
import copy, random
from characters.Neonpewpew import Neonpewpew
from simulation.Trigger import Trigger
class Population(object):
    gen = 0
    def __init__(self,popSize,init):
        Population.gen+=1
        self.trigGenRate=50
        self.individuals = []
        self.popSize = popSize;
        if init:
            for i in range(self.popSize):
                novi = Individual()
                self.generateTriggers(novi)
                novi.generateIndividual()
                
                self.individuals.append(novi)
       
    
    def getFittest(self):
        fittest = self.individuals[0]
        i = 0
        for i in self.individuals:
            if fittest.getTotalDmgDone() < i.getTotalDmgDone():
                fittest = i;
        
        return fittest
    def saveIndividual(self,indi):
        for i in range(0,self.popSize):
            if i == 0:
                self.individuals.append(copy.deepcopy(indi))
                
            else:
                noviIndi = Individual()
                noviIndi.triggers = copy.deepcopy(self.individuals[0].triggers)
                noviIndi.setcastSpellList(self.individuals[0].charNeonpewpew.castSpellList)
                self.individuals.append(noviIndi)
            
       
        
    def generateTriggers(self,indi):
        
        nrSpells = 4
        nrTriggerTypes = 9
        
        spellId = random.randint(0,nrSpells)
        triggerType = random.randint(1,nrTriggerTypes)
        c=0
        while c<2:
            if random.randint(0,100) < self.trigGenRate:
                if triggerType in (1,4,5,6):
                    sp = [3,1,0]
                    spellId = random.choice(sp)
                    
                    t = Trigger(triggerType,spellId,bool(random.getrandbits(1)))
                    indi.triggers.append(t)
                if triggerType == 2:
                    sp = [2]
                    spellId = random.choice(sp)
                    
                    t = Trigger(triggerType,spellId,bool(random.getrandbits(1)))
                    indi.triggers.append(t)
                if triggerType == 3:
                    sp = [0,1,2]
                    spellId = random.choice(sp)
                    
                    t = Trigger(triggerType,spellId,bool(random.getrandbits(1)))
                    indi.triggers.append(t)
                if triggerType == 7:
                    sp = [3,4]
                    spellId = random.choice(sp)
                    
                    t = Trigger(triggerType,spellId,bool(random.getrandbits(1)))
                    indi.triggers.append(t)
                if triggerType == 8:
                    sp = [3,4]
                    spellId = random.choice(sp)
                    
                    t = Trigger(triggerType,spellId,bool(random.getrandbits(1)))
                    indi.triggers.append(t)
                if triggerType == 9:
                    sp = [1,2]
                    spellId = random.choice(sp)
                    
                    t = Trigger(triggerType,spellId,bool(random.getrandbits(1)))
                    indi.triggers.append(t)
                
            c+=1        
                
                    
        
    def size(self):
        return len(self.individuals)