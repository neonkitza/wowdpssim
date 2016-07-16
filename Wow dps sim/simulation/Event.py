'''
Created on Jul 2, 2016

@author: Neonkitza
'''
from allSpells.allSpells import Spell
from characters.Neonpewpew import Neonpewpew
import copy
class Event(object):
    def __init__(self,spell,char):
        self.spell = spell
        self.buffList = copy.deepcopy(char.buffList)
        self.currentMana = char._mana
    