'''
Created on Jul 15, 2016

@author: Neonkitza
'''
from characters.Neonpewpew import Neonpewpew
from simulation.Event import Event
#from allSpells.allSpells import Spell
import random
from _operator import attrgetter
class Individual():
    def __init__(self):
        n = Neonpewpew()
        self.charNeonpewpew = n
        self.eventList = []
        self.fitness = 0
        self.totalDmgDone = 0
        self.totalCastTime = 0
    
    def generateIndividual(self):
        for value in self.charNeonpewpew.castSpellList:
            value.setPriority(random.randint(0,10))
        self.runIndi()
    
    def runIndi(self):
        bacio = False
        self.totalCastTime = 0
        while self.totalCastTime<60:
            sorted(self.charNeonpewpew.castSpellList,key=attrgetter('_priority'))
            buffoviZaBrisanje = []
            
            self.charNeonpewpew.manaRegen()
            for spell in self.charNeonpewpew.buffList.values():
                spell.decreaseDuration()
                if spell._durationRemaining<=0:
                    buffoviZaBrisanje.append(spell._name)
            for ime in buffoviZaBrisanje:
                del self.charNeonpewpew.buffList[ime]
            for spell in self.charNeonpewpew.castSpellList:
                spell.decreaseCD
            for spell in self.charNeonpewpew.castSpellList:
                if self.charNeonpewpew._mana > 0:
                    if spell.currentCD == 0:
                        event = Event(spell,self.charNeonpewpew)
                        event.spell.cast()
                        bacio = True
                        self.totalCastTime+=event.spell.castTime()
                        self.eventList.append(event)
                        break
            if not bacio:
                self.totalCastTime+=1
    def brEventova(self):
        return len(self.eventList)
    def getTotalDmgDone(self):
#         if self.fitness == 0:
#             self.fitness = FitnessCalc.getFitness(self,self)
            
        if self.fitness == 0:
            for event in self.eventList:
                self.fitness+=event.spell.damageDone
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
        