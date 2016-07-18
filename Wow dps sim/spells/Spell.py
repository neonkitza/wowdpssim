
from spells.SpellType import SpellType

'''from characters.Neonpewpew import charNeonpewpew'''
from abc import ABCMeta, abstractmethod
from allSpells import *
from allSpells.ArcaneCharge import ArcaneCharge
from allSpells.ArcaneMissilesBuff import ArcaneMissilesBuff
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
        
        
    def __repr__(self):
        return repr(self._priority)
    
    
    @abstractmethod
    def getDmg(self):
        pass
    
    def getCastTime(self):
        return self._castTime/(1+self.charNeonpewpew.hasteP)
    @abstractmethod
    def getDPS(self):
        pass
    def applyCharge(self,indi):
        '''if 
            if random.randint(0,100) <= 30:'''
        if self._name == 'Arcane Blast' or self._name == 'Arcane Missiles':
            if ArcaneCharge in self.charNeonpewpew.buffList.values():
                self.charNeonpewpew.buffList['Arcane Charge'].applyStack()
#  print("Arcane Charge stack applied "+str(self.charNeonpewpew.buffList['Arcane Charge'].stacks))
            else:
                a=ArcaneCharge(self.charNeonpewpew)
                self.charNeonpewpew.buffList['Arcane Charge'] = a
#  print("Arcane Charge created")
        elif self._name == 'Arcane Barrage':
            if ArcaneCharge in self.charNeonpewpew.buffList.values():
                del self.charNeonpewpew.buffList['Arcane Charge']
#   print("Arcane Charge deleted")
        elif self._name == 'Arcane Explosion':
            if random.randint(0,100) <= 30:
                if ArcaneCharge in self.charNeonpewpew.buffList.values():
                    self.charNeonpewpew.buffList['Arcane Charge'].applyStack()
#      print("Arcane Charge stack applied "+str(self.charNeonpewpew.buffList['Arcane Charge'].stacks))
                else:
                    a=ArcaneCharge(self.charNeonpewpew)
                    self.charNeonpewpew.buffList['Arcane Charge'] = a
                #    print("Arcane Charge created")
    
    
    @abstractmethod
    def cast(self):
        pass
    def decreaseDuration(self):
        if self._durationRemaining>0:
            self._durationRemaining-=1
        if self._durationRemaining==0:
            del self.charNeonpewpew.buffList[self._name]
    def resetDuration(self):
        self._durationRemaining = self._duration
    def applyMissiles(self):
        if random.randint(0,100)<30 and self._spellType==SpellType.dps and self._name!="Arcane Missiles":
            if ArcaneMissilesBuff in self.charNeonpewpew.buffList:
                self.charNeonpewpew.buffList['Arcane Missiles buff'].applyStack()
                self.charNeonpewpew.buffList['Arcane Missiles buff'].resetDuration()
            else:
                amb = ArcaneMissilesBuff(self.charNeonpewpew)
                self.charNeonpewpew.buffList['Arcane Missiles buff'] = amb
    def addToTotalCastTime(self,indi):
        if self._castTime < self.charNeonpewpew.GCDCalc():
            indi.totalCastTime+=self.charNeonpewpew.GCDCalc()
        else:
            indi.totalCastTime+=self._castTime
    def castTime(self):
        if self.getCastTime()<self.charNeonpewpew.GCDCalc():
            return self.charNeonpewpew.GCDCalc()
        else:
            return self.getCastTime()
    def decreaseCD(self):
        if self.currentCD>0:
            self.currentCD-=1
        if self.currentCD <= 0:
            self.currentCD = 0
            
    def dmgDone(self,dmg):
        if ArcanePowerBuff in self.charNeonpewpew.buffList:
            self.damageDone*=1.2
        self.damageDone = dmg
        