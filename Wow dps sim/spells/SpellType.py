'''
Created on Jun 27, 2016

@author: Neonkitza
'''
from enum import Enum

class SpellType(Enum):
    buff = 2
    debuff = 3
    dps = 1
    CD = 4