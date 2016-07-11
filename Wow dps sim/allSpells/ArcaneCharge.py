'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType

class ArcaneCharge(Spell):
    global charNeonpewpew
    stacks = 0
    def __init__(self):
        name = 'Arcane Charge'
        cooldown = 0
        manaCost = 0
        castTime = 0
        duration = 15
        spellType = SpellType.buff
        channelTime = 0
        modifiers = None
        stacks = 1
        listAffectedSpells = ['Arcane Blast', 'Arcane Missiles', 'Arcane Explosion', 'Arcane Barrage','Evocation']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False)
        
           
    def getDmg(self):
        d =  5*charNeonpewpew.spellPower*0.747
        d = d+d*charNeonpewpew.masteryP*charNeonpewpew._mana/charNeonpewpew._maxMana
        return d
    def applyStack(self):
        if stacks<4:
            stacks+=1
        duration = 15
    
        