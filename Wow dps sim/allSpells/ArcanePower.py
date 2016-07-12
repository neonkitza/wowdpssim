'''
Created on Jul 11, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType

class ArcanePower(Spell):
    global charNeonpewpew

    def __init__(self):
        name = 'Arcane Power'
        cooldown = 90
        manaCost = 0
        castTime = 0
        duration = 15
        spellType = SpellType.CD
        channelTime = 0
        modifiers = None
        listAffectedSpells = ['Arcane Blast', 'Arcane Missiles', 'Arcane Explosion', 'Arcane Barrage']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True)
        
    