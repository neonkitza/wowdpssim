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

        
#     apb = EvocationBuff(self.charNeonpewpew)
#     self.charNeonpewpew.buffList[apb._name] = apb
        
#        self._durationRemaining = self._duration
        self.currentCD = self._cooldown
  
        self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.15
        
        faliMane = 1-self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        kolikoTraje = faliMane//(self.charNeonpewpew._maxMana*0.075)
        if kolikoTraje < self._duration:
            self._duration = kolikoTraje
            
        self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.075*self._duration
#             
            
#         if i<self.charNeonpewpew.GCDCalc():
#             totalCastTime+=self.charNeonpewpew.GCDCalc()
#         else:
#             totalCastTime+=i


class EvocationBuff(Spell):
    def __init__(self,char):
        name = 'Evocation buff'
        cooldown = 0
        manaCost = 0
        castTime = 0
        duration = 6
        spellType = SpellType.buff
        channelTime = 0
        modifiers = None
        listAffectedSpells = []
        self.relativeDuration = 0
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False,char)
    
    def decreaseDuration(self):
        
        if self.charNeonpewpew._mana<self.charNeonpewpew._maxMana and self.relativeDuration<self._durationRemaining:
            self.relativeDuration+=1
            self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.075
            