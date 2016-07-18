
from allSpells.allSpells import *
import copy
import allSpells

class Neonpewpew:
    int = 4380
    str = 642
    agi = 891
    stam = 4738
    spirit = 1155
    spellPower = 5533
    manaRegen = 22893
    critP = 0.1352
    hasteP = 0.1588
    masteryP = 0.3847
    multistrikeP = 0.259
    crit = 937
    haste = 1326
    mastery = 1371
    multistrike = 171
    
    #phase changes to "conserve"
    def __init__(self):
        self._name = "Neonpewpew"
        ''' self.__init_stats__()'''
        self._mana = 168000
        self._maxMana = 168000
        self._baseGCD = 1.5
        self._statsChanged = False
        self._GCD = self.GCDCalc()
        self.spellList = []
        self.castSpellList = []
        self.buffList = {}
        self.phase = "burst"
        
        
        
        
    def GCDCalc(self):
        return self._baseGCD/(1+self.hasteP)
    
    def initSpells(self):
        self.castSpellList.append(ArcaneBarrage(self))
        self.castSpellList.append(ArcaneBlast(self))
        self.castSpellList.append(ArcaneMissiles(self))
        self.castSpellList.append(Evocation(self))
        self.castSpellList.append(ArcanePower(self))
        
    def manaRegen(self):
        self._mana+=2000
        if self._mana>self._maxMana:
            self._mana = self._maxMana
            
    def copySpellList(self,spellList):
        self.castSpellList = copy.deepcopy(spellList)
    def resetChar(self):
        self.buffList = {}
        self._mana = self._maxMana
