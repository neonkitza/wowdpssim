'''
Created on Jun 27, 2016

@author: Neonkitza
'''
from spells.SpellType import SpellType
from characters.Neonpewpew import charNeonpewpew, totalCastTime
'''from characters.Neonpewpew import charNeonpewpew'''
from abc import ABCMeta, abstractmethod
from allSpells import *
import random

class Spell(object):
    __metaclass__ = ABCMeta
#    global charNeonpewpew
    '''  name = ''
    cooldown = 0
    manaCost = 0
    castTime = 0
    duration = 0
    spellType = None
    channelTime = 0
    modifiers = None
    listAffectedSpells = []'''
    
    def __init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,castable,char):
        self._name=name
        self._cooldown = cooldown
        self._manaCost = manaCost
        self._castTime = castTime
        self._duration = duration
        self._durationRemaining = 0
        self._spellType = spellType
        self._castable = castable
        self._priority = 0
        self.currentCD = 0
        self.damageDone = 0
        self.charNeonpewpew = char
    def getPriority(self):
        return self._priority
    def setPriority(self,pro):
        self._priority = pro
        
    def increasePriority(self):
        self._priority+=1
    def decreasePriority(self):
        self._priority-=1
        
    @abstractmethod
    def getDmg(self):
        pass
    
    def getCastTime(self):
        return self._castTime/(1+charNeonpewpew.hasteP)
    @abstractmethod
    def getDPS(self):
        pass
    def applyCharge(self,indi):
        '''if 
            if random.randint(0,100) <= 30:'''
        if self._name == 'Arcane Blast' or self._name == 'Arcane Missiles':
            if ArcaneCharge in self.charNeonpewpew.buffList.values():
                self.charNeonpewpew.buffList['ACharge'].applyStack()
                print("Arcane Charge stack applied "+str(self.charNeonpewpew.buffList['ACharge'].stacks))
            else:
                a=ArcaneCharge()
                self.charNeonpewpew.buffList['ACharge'] = a
                print("Arcane Charge created")
        elif self._name == 'Arcane Barrage':
            if ArcaneCharge in self.charNeonpewpew.buffList.values():
                del self.charNeonpewpew.buffList['ACharge']
                print("Arcane Charge deleted")
        elif self._name == 'Arcane Explosion':
            if random.randint(0,100) <= 30:
                if ArcaneCharge in self.charNeonpewpew.buffList.values():
                    self.charNeonpewpew.buffList['ACharge'].applyStack()
                    print("Arcane Charge stack applied "+str(self.charNeonpewpew.buffList['ACharge'].stacks))
                else:
                    a=ArcaneCharge()
                    self.charNeonpewpew.buffList['ACharge'] = a
                    print("Arcane Charge created")
    
    
    @abstractmethod
    def cast(self):
        pass
    def applyMissiles(self):
        if random.randint(0,100)<30 and self._spellType==SpellType.dps and self._name!="Arcane Missiles":
            if ArcaneMissilesBuff in self.charNeonpewpew.buffList.values():
                self.charNeonpewpew.buffList['AMissilesBuff'].applyStack()
            else:
                amb = ArcaneMissilesBuff()
                self.charNeonpewpew.buffList['AMissilesBuff'] = amb
    def addToTotalCastTime(self,indi):
        if self._castTime < self.charNeonpewpew.GCDCalc():
            indi.totalCastTime+=self.charNeonpewpew.GCDCalc()
        else:
            indi.stotalCastTime+=self._castTime
    
    def decreaseCD(self):
        if self.currentCD>0:
            self.currentCD-=1
            
    def dmgDone(self,dmg): 
        self.damageDone = dmg
        