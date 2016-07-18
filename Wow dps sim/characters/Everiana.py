
import wowapi

class Everiana:
    kind = 'Character'
    def __init__(self, name, stats, spells):
        self._name = name
        self.__init_spells__()
    
    def __init_stats__(self):
        self._stats = {
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