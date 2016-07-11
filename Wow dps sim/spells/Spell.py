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
    global charNeonpewpew
    '''  name = ''
    cooldown = 0
    manaCost = 0
    castTime = 0
    duration = 0
    spellType = None
    channelTime = 0
    modifiers = None
    listAffectedSpells = []'''
    
    def __init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,castable):
        self._name=name
        self._cooldown = cooldown
        self._manaCost = manaCost
        self._castTime = castTime
        self._duration = duration
        self._spellType = spellType
        self._castable = castable
        self._priority = priority()
        
    @abstractmethod   
    def priority(self):
        pass
        
    @abstractmethod
    def getDmg(self):
        pass
    
    def getCastTime(self):
        return self._castTime/(1+charNeonpewpew.hasteP)
    @abstractmethod
    def getDPS(self):
        pass
    def applyCharge(self):
        '''if 
            if random.randint(0,100) <= 30:'''
        if self._name == 'Arcane Blast' or self._name == 'Arcane Missiles':
            if ArcaneCharge in charNeonpewpew.buffList.values():
                buffList['ACharge'].applyStack()
                print("Arcane Charge stack applied"+str(buffList['ACharge'].stacks))
            else:
                a=ArcaneCharge()
                buffList['ACharge'] = a
                print("Arcane Charge created")
        elif self._name == 'Arcane Barrage':
            if ArcaneCharge in charNeonpewpew.buffList.values():
                del buffList['ACharge']
                print("Arcane Charge deleted")
        elif self._name == 'Arcane Explosion':
            if random.randint(0,100) <= 30:
                if ArcaneCharge in charNeonpewpew.buffList.values():
                    buffList['ACharge'].applyStack()
                    print("Arcane Charge stack applied"+str(buffList['ACharge'].stacks))
                else:
                    a=ArcaneCharge()
                    buffList['ACharge'] = a
                    print("Arcane Charge created")
    
    
    @abstractmethod
    def cast(self):
        pass
    def missiles(self):
        if random.randint(0,100)<40:
            charNeonpewpew.castSpellList['AMissiles'].increaseStacks()
    def addToTotalCastTime(self):
        if self._castTime == 0:
            totalCastTime+=charNeonpewpew.GCDCalc()
        else:
            totalCastTime+=self._castTime
            
        