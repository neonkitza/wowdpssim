'''
Created on Jul 15, 2016

@author: Neonkitza
'''
import random
from simulation.Population import Population
class Algorithm():
    mutationRate = 30
    elitism = True
    
    def evolvePopulation(self,oldPop):
        newPopulation = Population(oldPop.popSize,False)
        elitismOffset = 0
        if elitism:
            newPopulation.saveIndividual(oldPop.getFittest())
            elitismOffset = 1
        
        for i in range(elitismOffset,newPopulation.popSize):
            self.mutate(newPopulation.individuals[i])
        
        return newPopulation
        
    
    def mutate(self,indi):
        for spell in indi.charNeonpewpew.castSpellList.values():
                if random.randint(0,100)< Algorithm.mutationRate:
                    sta = bool(random.getrandbits(1))
                    if sta:
                        spell.increasePriority()
                    else:
                        spell.decreasePriority()
            
    