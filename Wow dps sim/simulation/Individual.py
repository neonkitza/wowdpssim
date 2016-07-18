
from characters.Neonpewpew import Neonpewpew
from simulation.Event import Event

import random
import copy
from allSpells.allSpells import Evocation, ArcanePower, ArcaneMissilesBuff,\
    ArcaneBarrage, ArcaneBlast, ArcaneCharge
from allSpells.allSpells import ArcaneMissiles
class Individual():
    def __init__(self):
        n = Neonpewpew()
        self.triggers = []
        self.charNeonpewpew = n
        self.charNeonpewpew.initSpells()
        self.eventList = []
        self.fitness = 0
        self.totalDmgDone = 0
        self.totalCastTime = 0

    def setcastSpellList(self,spellList):
        self.charNeonpewpew.castSpellList = copy.deepcopy(spellList)
        
    
    def generateIndividual(self):
        for value in self.charNeonpewpew.castSpellList:
            value.setPriority(random.randint(0,10))
        self.runIndi()
    
    def runIndi(self):
        bacio = False
        self.totalCastTime = 0
        while self.totalCastTime<300:
#self.prioUpdate()
            sortiranaLista = sorted(self.charNeonpewpew.castSpellList,key=lambda spell: (spell._priority,spell.kolikoBitan),reverse=True)
            buffoviZaBrisanje = []
            
            self.charNeonpewpew.manaRegen()
            for spell in self.charNeonpewpew.buffList.values():
                spell.decreaseDuration()
                if spell._durationRemaining <= 0:
                    buffoviZaBrisanje.append(spell._name)
            for ime in buffoviZaBrisanje:
                del self.charNeonpewpew.buffList[ime]
                
            for spell in self.charNeonpewpew.castSpellList:
                spell.decreaseCD
                spell.charNeonpewpew = self.charNeonpewpew
            
            for spell in sortiranaLista:
                if spell.applyCast():
                    spell.cast()
                    event = Event(spell,self.charNeonpewpew)
                    bacio = True
                    self.totalCastTime+=spell.castTime()
                    self.eventList.append(event)
                    #prolazi kroz listu triggera OVDE!
                    #provera da li postoji aktivan prioupdate stvari
                    
                    for trigger in self.triggers:
                        if trigger.triggerType == 1:
                            if self.charNeonpewpew._mana/self.charNeonpewpew._maxMana < 0.5:
                                if trigger.increase:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].increasePriority()
                                else:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].decreasePriority()
                            
                        if trigger.triggerType == 2:
                            if 'Arcane Missiles buff' in self.charNeonpewpew.buffList.keys():
                                if self.charNeonpewpew.buffList['Arcane Missiles buff']==3:
                                    if trigger.increase:
                                        self.charNeonpewpew.castSpellList[trigger.spellId].increasePriority()
                                    else:
                                        self.charNeonpewpew.castSpellList[trigger.spellId].decreasePriority()
                        if trigger.triggerType == 3:
                            if 'Arcane Charge' in self.charNeonpewpew.buffList.keys():
                                if self.charNeonpewpew.buffList['Arcane Charge']==4:
                                    if trigger.increase:
                                        self.charNeonpewpew.castSpellList[trigger.spellId].increasePriority()
                                    else:
                                        self.charNeonpewpew.castSpellList[trigger.spellId].decreasePriority()
                        if trigger.triggerType == 4:
                            if self.charNeonpewpew._mana/self.charNeonpewpew._maxMana < 0.3:
                                if trigger.increase:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].increasePriority()
                                else:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].decreasePriority()
                        if trigger.triggerType == 5:
                            if self.charNeonpewpew._mana/self.charNeonpewpew._maxMana < 0.6:
                                if trigger.increase:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].increasePriority()
                                else:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].decreasePriority()
                        if trigger.triggerType == 6:
                            if self.charNeonpewpew._mana/self.charNeonpewpew._maxMana < 0.9:
                                if trigger.increase:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].increasePriority()
                                else:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].decreasePriority()
                    
                        if trigger.triggerType == 7:
                            if self.charNeonpewpew.castSpellList[3].applyCast() and self.charNeonpewpew.castSpellList[4].applyCast():
                                if trigger.increase:
                                    self.charNeonpewpew.castSpellList[4].increasePriority()
                                    self.charNeonpewpew.castSpellList[3].increasePriority()
                                else:
                                    self.charNeonpewpew.castSpellList[4].decreasePriority()    
                                    self.charNeonpewpew.castSpellList[3].decreasePriority()    
                        
                        if trigger.triggerType == 8:
                            if self.charNeonpewpew.castSpellList[trigger.spellId].applyCast():
                                if trigger.increase:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].increasePriority()
                                else:
                                    self.charNeonpewpew.castSpellList[trigger.spellId].decreasePriority()    
                        
                    break
                    
            if not bacio:
                self.totalCastTime+=1
                
         
        print("runIndi brEventova: "+str(self.brEventova())+" i totalDmg: " + str(self.getTotalDmgDone()))
        
        
    def prioUpdate(self):
        for i in range(len(self.charNeonpewpew.castSpellList)):
            if self.charNeonpewpew.castSpellList[i]._name == 'Evocation':
                evoIndex = i
            elif self.charNeonpewpew.castSpellList[i]._name == 'Arcane Power':
                apIndex = i
            elif self.charNeonpewpew.castSpellList[i]._name == 'Arcane Missiles':
                amIndex = i
            elif self.charNeonpewpew.castSpellList[i]._name == 'Arcane Barrage':
                abIndex = i
            elif self.charNeonpewpew.castSpellList[i]._name == 'Arcane Blast':
                ablastIndex = i
                
        staIma = []
        for buff in self.charNeonpewpew.buffList.values():
            staIma.append(buff._name)
       
        #evocation stuff
        if self.charNeonpewpew._mana/self.charNeonpewpew._maxMana < 0.5 and self.charNeonpewpew.phase=="burst" and self.charNeonpewpew.castSpellList[evoIndex].applyCast():
            self.charNeonpewpew.castSpellList[evoIndex].increasePriority()
        else:
            self.charNeonpewpew.castSpellList[evoIndex].decreasePriority()
            
        #phase stuff
        if 'Arcane Charge' in staIma and self.charNeonpewpew.castSpellList[apIndex].applyCast() and self.charNeonpewpew.castSpellList[evoIndex].applyCast() and self.charNeonpewpew.phase!="burst":
            if self.charNeonpewpew.buffList['Arcane Charge'].stacks == 4:
                self.charNeonpewpew.phase = "burst"
               
                print("Usao u burst phase")
        if not self.charNeonpewpew.castSpellList[evoIndex].applyCast() and self.charNeonpewpew.phase!="conserve":
            self.charNeonpewpew.phase = "conserve"
            
            print("Usao u conserve phase")
             
        
        #arcane missiles stuff
        if 'Arcane Missiles buff' in staIma:
            if self.charNeonpewpew.buffList['Arcane Missiles buff'].stacks == 3:
                self.charNeonpewpew.castSpellList[amIndex].increasePriority()
                self.charNeonpewpew.castSpellList[ablastIndex].decreasePriority()
            elif 'Arcane Charge' in staIma:
                if self.charNeonpewpew.castSpellList[amIndex].applyCast() and self.charNeonpewpew.buffList['Arcane Charge'].stacks == 4:
                    self.charNeonpewpew.castSpellList[amIndex].increasePriority()
                    
                    
                    self.charNeonpewpew.castSpellList[ablastIndex].decreasePriority()
            else:
                self.charNeonpewpew.castSpellList[amIndex].decreasePriority()
        else:
            self.charNeonpewpew.castSpellList[amIndex].decreasePriority()
        
        #phaseDo stuff
        if self.charNeonpewpew.phase == "burst":
            if self.charNeonpewpew.castSpellList[apIndex].applyCast():
                self.charNeonpewpew.castSpellList[apIndex].increasePriority()
            else:
                self.charNeonpewpew.castSpellList[apIndex].decreasePriority()
                 
            if self.charNeonpewpew.castSpellList[apIndex].applyCast():
                self.charNeonpewpew.castSpellList[apIndex].increasePriority()
            self.charNeonpewpew.castSpellList[abIndex].decreasePriority()
            self.charNeonpewpew.castSpellList[ablastIndex].increasePriority()
            if self.charNeonpewpew._mana/self.charNeonpewpew._maxMana < 0.5 and self.charNeonpewpew.castSpellList[evoIndex].applyCast():
                self.charNeonpewpew.castSpellList[evoIndex].increasePriority()
            else:
                self.charNeonpewpew.castSpellList[evoIndex].decreasePriority()
        else:
            if self.charNeonpewpew._mana/self.charNeonpewpew._maxMana < 0.93:
                self.charNeonpewpew.castSpellList[ablastIndex].decreasePriority()
            else: 
                self.charNeonpewpew.castSpellList[ablastIndex].increasePriority()
            if 'Arcane Charge' in staIma:
                if self.charNeonpewpew.buffList['Arcane Charge'].stacks == 4:
                    self.charNeonpewpew.castSpellList[abIndex].increasePriority()
            self.charNeonpewpew.castSpellList[evoIndex].decreasePriority()
            
            
        
    def brEventova(self):
        return len(self.eventList)
    def getTotalDmgDone(self):
        self.fitness = 0
        for event in self.eventList:
            self.fitness+=event.spell.damageDone
#            print("Spell: "+event.spell._name+" dmg: "+ str(event.spell.damageDone))
#             if event.spell._name == 'Arcane Blast':
#                 print("Arcane Charge stacks: "+str(event.buffList['Arcane Charge'].stacks))
#             if 'Arcane Missiles buff' in event.buffList.keys():
#                print("Missiles buff stacks: "+str(event.buffList['Arcane Missiles buff'].stacks))
        return self.fitness
 #   def generateTriggers(self):
        
    def resetIndi(self):
        self.eventList = []
        self.charNeonpewpew.resetChar()
        self.fitness = 0
        self.totalDmgDone = 0
        self.totalCastTime = 0
    def getTotalCastTime(self):
        totalTime = 0
        for event in self.eventList:
            totalTime+=event.spell.castTime()
        self.totalCastTime = totalTime
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
        