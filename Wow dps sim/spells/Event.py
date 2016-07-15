'''
Created on Jul 2, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters import Neonpewpew
class Event(object):
    def __init__(self,spell,char):
        self.spell = spell
        self.buffList = char.buffList.deepcopy()
        self.currentMana = char._mana
    