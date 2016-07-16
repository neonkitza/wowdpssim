'''
Created on Jul 11, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType
from characters.Neonpewpew import charNeonpewpew, totalCastTime
class Evocation(Spell):
 #   global charNeonpewpew

    def __init__(self,char):
        name = 'Evocation'
        cooldown = 90
        manaCost = 0
        castTime = 0
        duration = 6
        spellType = SpellType.CD
        channelTime = 0
        modifiers = None
        listAffectedSpells = []
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
    def cast(self):
#       currentMana = charNeonpewpew._mana/charNeonpewpew._maxMana
        self.currentCD = self._cooldown
        i = 0
        self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.15
        while self.charNeonpewpew._mana<self.charNeonpewpew._maxMana and i<self._duration:
            i+=1
            self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.075
        if i<self.charNeonpewpew.GCDCalc():
            totalCastTime+=self.charNeonpewpew.GCDCalc()
        else:
            totalCastTime+=i