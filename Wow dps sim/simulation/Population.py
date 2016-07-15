'''
Created on Jul 15, 2016

@author: Neonkitza
'''
# from characters.Neonpewpew import Neonpewpew
from simulation.Individual import Individual

class Population(object):
    def __init__(self,popSize,init):
        self.individuals = []
        self.popSize = popSize;
        if init:
            for i in range(self.popSize):
                novi = Individual()
                novi.generateIndividual()
                self.individuals.append(novi)
    
    def getFittest(self):
        fittest = self.individuals[0]
        i = 0
        for i in self.individuals:
            if fittest < i.getTotalDmgDone():
                fittest = i;
        
        return fittest
    def saveIndividual(self,indi):
        self.individuals[0] = indi
    
    def size(self):
        return len(self.individuals)