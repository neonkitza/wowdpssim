'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
# from characters.Neonpewpew import charNeonpewpew
from spells.SpellType import SpellType
from characters.Neonpewpew import *
from allSpells import ArcaneCharge, ArcaneMissilesBuff
from allSpells.ArcanePower import ArcanePowerBuff

class ArcaneMissiles(Spell):
    
    def __init__(self,char):
        name = 'Arcane Missiles'
        cooldown = 0
        manaCost = 0.02*char._maxMana
        castTime = 0
        duration = 0
        spellType = SpellType.dps
        channelTime = 2
        modifiers = None
        listAffectedSpells = ['Arcane Missiles Buff']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
        # self.stacks = 0
            
    def getDmg(self):
        d =  5*self.charNeonpewpew.spellPower*0.285
        d = d+d*self.charNeonpewpew.masteryP*self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        if ArcaneCharge in self.charNeonpewpew.buffList.values():
            chargeMulti = self.charNeonpewpew.buffList['Arcane Charge'].stacks
            d=d+d*chargeMulti*0.5
        return d
#     def increaseStacks(self):
#         if self.stacks<3:
#             self.stacks+=1
    def cast(self):
        manaC = self._manaCost
        if ArcanePowerBuff in self.charNeonpewpew.buffList:
            manaC *= 0.9
        if ArcaneMissilesBuff in self.charNeonpewpew.buffList.values():
            if self.charNeonpewpew.buffList['Arcane Missiles buff'].stacks>0:
                
                self.charNeonpewpew.buffList['Arcane Missiles buff'].removeStack()
                
                self.damageDone=self.getDmg()
                
                if ArcaneCharge in self.charNeonpewpew.buffList.values():
                    self.charNeonpewpew._mana-=manaC*(1+self.charNeonpewpew.buffList['Arcane Charge'].stacks)
                else:
                    self.charNeonpewpew._mana-=manaC
                
                self.damageDone=self.getDmg(self)
                
                self.currentCD = self._cooldown
                
                self.applyCharge()
#          self.addToTotalCastTime()
            else:
                pass
            #treba valjda addtotalcasttime
        else:
            pass
            
        