'''
Created on Jun 27, 2016

@author: Neonkitza
'''
from spells.SpellType import SpellType
from characters.Neonpewpew import Neonpewpew
from abc import ABCMeta, abstractmethod

class Spell(object):
    __metaclass__ = ABCMeta
    
    '''  name = ''
    cooldown = 0
    manaCost = 0
    castTime = 0
    duration = 0
    spellType = None
    channelTime = 0
    modifiers = None
    listAffectedSpells = []'''
    
    def __init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime):
        self._name=name
        self._cooldown = cooldown
        self._manaCost = manaCost
        self._castTime = castTime
        self._duration = duration
        self._spellType = spellType
        
    @abstractmethod
    def getDmg(self):
        pass
        
        