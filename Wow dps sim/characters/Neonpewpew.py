'''
Created on Jun 27, 2016

@author: Neonkitza
'''

from spells.SpellType import SpellType
from allSpells import *


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
#     spellList = {}
#     castSpellList = {}
#     castedSpellList = []
#     buffList = {}
    phase = "burst"
    #phase changes to "conserve"
    def __init__(self):
        self._name = "Neonpewpew"
        ''' self.__init_stats__()'''
        self._mana = 168000
        self._maxMana = 168000
        self._baseGCD = 1.5
        self._statsChanged = False
        self._GCD = self.GCDCalc()
#         self.haste = 1326
#         self.hasteP = 0.1588
        self.spellList = []
        self.castSpellList = []
        self.castedSpellList = []
        self.buffList = {}
        
        self.initSpells()
        
        
        
        
    def GCDCalc(self):
        return self._baseGCD/(1+self.hasteP)
    
    def initSpells(self):
        self.castSpellList.append(ArcaneBarrage(self))
        self.castSpellList.append(ArcaneBlast(self))
        self.castSpellList.append(ArcaneExplosion(self))
        self.castSpellList.append(ArcaneMissiles(self))
        self.castSpellList.append(Evocation(self))
        self.castSpellList.append(ArcanePower(self))
        
        
charNeonpewpew = Neonpewpew()
totalDMG = 0
endTime = 90
totalCastTime = 0

        