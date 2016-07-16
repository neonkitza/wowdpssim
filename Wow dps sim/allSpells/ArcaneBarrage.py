'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType
from allSpells.ArcaneCharge import ArcaneCharge
import random
from allSpells.ArcanePower import ArcanePowerBuff

class ArcaneBarrage(Spell):
    global charNeonpewpew
     
    def __init__(self,char):
        name = 'Arcane Barrage'
        cooldown = 3
        manaCost = 0.005*char._maxMana
        castTime = 0
        duration = 0
        spellType = SpellType.dps
        channelTime = 0
        modifiers = None
        listAffectedSpells = ['Arcane Charge']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
           
    def getDmg(self):
        d =  5*self.charNeonpewpew.spellPower*0.747
        d = d+d*self.charNeonpewpew.masteryP*self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        if ArcaneCharge in self.charNeonpewpew.buffList.values():
            chargeMulti = self.charNeonpewpew.buffList['Arcane Charge'].stacks
            d=d+d*chargeMulti*0.5
        return d
    
#     def priority(self):
#         prio = self.getDmg()/super(ArcaneBarrage, self).getCastTime()/1000
#         if ArcaneCharge in charNeonpewpew.buffList.values():
#             if charNeonpewpew.buffList['Arcane Charge'].stacks < 4:
#                 prio * 3

    def cast(self):
        self.damageDone=self.getDmg(self)
        self.currentCD = self._cooldown
        manaC = self._manaCost
        if ArcanePowerBuff in self.charNeonpewpew.buffList:
            manaC *= 0.9
        self.charNeonpewpew._mana-=manaC
       
        if ArcaneCharge in charNeonpewpew.buffList:       
            self.charNeonpewpew.buffList['Arcane Charge'].removeStacks()
            
            
            
    