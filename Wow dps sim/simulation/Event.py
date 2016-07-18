
import copy
class Event(object):
    def __init__(self,spell,char):
        self.spell = copy.deepcopy(spell)
        self.buffList = copy.deepcopy(char.buffList)
        self.currentMana = copy.deepcopy(char._mana)
        self.dmgDone = self.spell.damageDone
    