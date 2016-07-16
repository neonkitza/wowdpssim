'''
Created on Jul 15, 2016

@author: Neonkitza
'''
from characters.Neonpewpew import Neonpewpew

import random
class Individual():
    def __init__(self):
        self.charNeonpewpew = Neonpewpew()
        self.eventList = []
        self.fitness = 0
        self.totalDmgDone = 0
        self.totalCastTime = 0
    
    def generateIndividual(self):
        for value in self.charNeonpewpew.castSpellList.values():
            value.setPriority(random.randint(0,10))
            
    def brEventova(self):
        return len(self.eventList)
    def getTotalDmgDone(self):
        if self.fitness == 0:
            self.fitness = FitnessCalc.getFitness(self)
        return self.fitness
    
    def getTotalCastTime(self):
        totalTime = 0
        for event in self.eventList:
            totalTime+=event.spell.castTime()
        return totalTime
    
class FitnessCalc(object):
    solution = Individual()
    
    def setSolution(self,individual):
        FitnessCalc.solution = individual
    
    def getFitness(self,individual):
        fitness = 0
        for event in FitnessCalc.solution.eventList:
            fitness+=event.spell.damageDone
        return fitness
    
    def getMaxFitness(self):
        return FitnessCalc.solution.getTotalDmgDone()
        