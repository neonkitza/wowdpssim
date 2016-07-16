'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from spells.SpellType import SpellType

class ArcaneCharge(Spell):
  
    def __init__(self,char):
        name = 'Arcane Charge'
        cooldown = 0
        manaCost = 0
        castTime = 0
        duration = 15
        spellType = SpellType.buff
        channelTime = 0
        modifiers = None
        self.stacks = 1
        listAffectedSpells = ['Arcane Blast', 'Arcane Missiles', 'Arcane Explosion', 'Arcane Barrage','Evocation']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False,char)
        
           
    def getDmg(self):
        d =  5*self.charNeonpewpew.spellPower*0.747
        d = d+d*self.charNeonpewpew.masteryP*self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        return d
    def applyStack(self):
        self._durationRemaining = self._duration
        if self.stacks<4:
            self.stacks+=1
        #duration = 15
    
    def removeStacks(self):
        self.stacks = 0
        del self.charNeonpewpew.buffList['Arcane Charge']