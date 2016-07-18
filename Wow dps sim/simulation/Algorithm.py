
import random
from simulation.Population import Population
from simulation.Trigger import Trigger
class Algorithm():
    mutationRate = 20
    deletitionRate = 15
    newRate = 30
    elitism = True
    
    def evolvePopulation(self,oldPop):
        newPopulation = Population(oldPop.popSize,False)
        elitismOffset = 0
        if Algorithm.elitism:
            newPopulation.saveIndividual(oldPop.getFittest())
            elitismOffset = 1
        
#        for i in newPopulation.individuals
        for i in range(elitismOffset,newPopulation.popSize):
            self.mutate(self,newPopulation.individuals[i])
            newPopulation.individuals[i].runIndi()
        
        return newPopulation
        
    
    def mutate(self,indi):
        #menjam triggere
        #mutate triggers of indi
        toDelete = []
        for i in range(len(indi.triggers)-1):
            if random.randint(0,100) < Algorithm.deletitionRate:
                toDelete.append(i)
                
            if random.randint(0,100) < Algorithm.mutationRate:
                indi.triggers[i].mutateExisting()
                print("Mutirao triger")
        for k in toDelete:
            del indi.triggers[k]
            print("Obrisao trigger")
        if random.randint(0,100) < Algorithm.newRate:
            nrSpells = 4
            nrTriggerTypes = 9
        
            spellId = random.randint(0,nrSpells)
            triggerType = random.randint(1,nrTriggerTypes)
            print("Napravio novi triger")
            
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

       
   
    