'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType
from allSpells.ArcaneCharge import ArcaneCharge
import random

class ArcaneBarrage(Spell):
    global charNeonpewpew
     
    def __init__(self):
        name = 'Arcane Barrage'
        cooldown = 3
        manaCost = 0.005*charNeonpewpew._mana
        castTime = 0
        duration = 0
        spellType = SpellType.dps
        channelTime = 0
        modifiers = None
        listAffectedSpells = ['Arcane Charge']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True)
        
           
    def getDmg(self):
        d =  5*charNeonpewpew.spellPower*0.747
        d = d+d*charNeonpewpew.masteryP*charNeonpewpew._mana/charNeonpewpew._maxMana
        if ArcaneCharge in charNeonpewpew.buffList.values():
            chargeMulti = charNeonpewpew.buffList['ACharge'].stacks
            d=d+d*chargeMulti*0.5
        return d
    
#     def priority(self):
#         prio = self.getDmg()/super(ArcaneBarrage, self).getCastTime()/1000
#         if ArcaneCharge in charNeonpewpew.buffList.values():
#             if charNeonpewpew.buffList['ACharge'].stacks < 4:
#                 prio * 3

    def cast(self):
        if ArcaneCharge in charNeonpewpew.buffList.values():       
            charNeonpewpew.buffList['ACharge'].removeStacks() = 0
            del charNeonpewpew.buffList['ACharge']