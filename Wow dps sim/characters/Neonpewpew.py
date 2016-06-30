'''
Created on Jun 27, 2016

@author: Neonkitza
'''
from spells import Spell
from spells import SpellType
class Neonpewpew:
    kind = 'Character'
    def __init__(self):
        self._name = "Neonpewpew"
        self.__init_stats__()
        self._mana = 300000
        self._baseGCD = 1.5
        self._statsChanged = False
        self._GCD = self.GCDCalc()
        
        
        
    def GCDCalc(self):
        return self._baseGCD/(1+self._stats['haste%']*0.01)
    
    def __init_stats__(self):
        self._stats={
                    'int': 4380,
                    'str': 642,
                    'agi': 891,
                    'stam': 4738,
                    'spirit': 1155,
                    'spellPower': 5533,
                    'manaRegen': 22893,
                    'crit%': 13.52,
                    'haste%': 15.88,
                    'mastery%': 38.47,
                    'multistrike%': 2.59,
                    'crit': 937,
                    'haste': 1326,
                    'mastery': 1371,
                    'multistrike': 171
                    }
        
    def __init_spells__(self):
        return 0
        