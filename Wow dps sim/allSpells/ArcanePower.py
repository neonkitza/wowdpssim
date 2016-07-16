'''
Created on Jul 11, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType

class ArcanePower(Spell):

    def __init__(self,char):
        name = 'Arcane Power'
        cooldown = 90
        manaCost = 0
        castTime = 0
        duration = 0
        spellType = SpellType.CD
        channelTime = 0
        modifiers = None
        listAffectedSpells = ['Arcane Blast', 'Arcane Missiles', 'Arcane Explosion', 'Arcane Barrage']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
    def cast(self):
        apb = ArcanePowerBuff(self.charNeonpewpew)
        self.charNeonpewpew.buffList[apb._name] = apb
    
class ArcanePowerBuff(Spell):
    def __init__(self,char):
        name = 'Arcane Power buff'
        cooldown = 0
        manaCost = 0
        castTime = 0
        duration = 15
        spellType = SpellType.buff
        channelTime = 0
        modifiers = None
        listAffectedSpells = []
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False,char)
    