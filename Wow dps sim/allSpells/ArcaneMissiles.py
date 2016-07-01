'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType

class ArcaneMissiles(Spell):
    global charNeonpewpew
    
    def __init__(self):
        name = 'Arcane Missiles'
        cooldown = 0
        manaCost = 0.02*charNeonpewpew._mana
        castTime = 0
        duration = 0
        spellType = SpellType.dps
        channelTime = 2
        modifiers = None
        listAffectedSpells = []
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime)
        
        self.stacks = 0
            
    def getDmg(self):
        d =  5*charNeonpewpew.spellPower*0.285
        d = d+d*charNeonpewpew.masteryP*charNeonpewpew._mana/charNeonpewpew._maxMana
        return d