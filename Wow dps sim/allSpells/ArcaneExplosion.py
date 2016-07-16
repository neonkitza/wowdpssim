'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
#from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType
from allSpells.ArcanePower import ArcanePowerBuff

class ArcaneExplosion(Spell):
#    global charNeonpewpew
     
    def __init__(self,char):
        name = 'Arcane Explosion'
        cooldown = 0
        manaCost = 0.03*char._maxMana
        castTime = 0
        duration = 0
        spellType = SpellType.dps
        channelTime = 0
        modifiers = None
        listAffectedSpells = ['Arcane Charge']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
    def getDmg(self):
        d =  5*self.charNeonpewpew.spellPower*0.545
        d = d+d*self.charNeonpewpew.masteryP*self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        return d
    def cast(self):
        self.damageDone=self.getDmg(self)
        manaC = self._manaCost
        if ArcanePowerBuff in self.charNeonpewpew.buffList:
            manaC *= 0.9
       
        self.charNeonpewpew._mana-=manaC     
        self.currentCD = self._cooldown
        #   self.addToTotalCastTime()
        
        self.applyCharge(self)
        