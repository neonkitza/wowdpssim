'''
Created on Jun 27, 2016

@author: Neonkitza
'''
from spells.SpellType import SpellType
from characters.Neonpewpew import Neonpewpew

class Spell:
    def __init__(self,name,cooldown,manaCost,spellCast,duration,spellType,damage,listAffectedSpells,modifiers,channelTime,character):
        self._name=name
        self._cooldown = cooldown
        self._manaCost = manaCost
        self._spellCast = spellCast
        self._duration = duration
        self._spellType = spellType
        self._damage = damage
        self._character = character
        
    def arcaneBlastDmg(self):
        return self._character._stats['spellPower']
    def spellDmg(self):
        options = {'Arcane Blast' : arcaneBlastDmg,
                   }
        