'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from spells.SpellType import SpellType
from allSpells.ArcaneCharge import ArcaneCharge
from allSpells.ArcanePower import ArcanePowerBuff
#from simulation.Individual import Individual

class ArcaneBlast(Spell):
  #  global charNeonpewpew,totalDMG,totalCastTime
    
    def __init__(self,char):
        name = 'Arcane Blast'
        cooldown = 0
        manaCost = 0.02*char._maxMana
        #*indi.charNeonpewpew._mana
        castTime = 2.25
        duration = 0
        spellType = SpellType.dps
        channelTime = 0
        modifiers = None
        listAffectedSpells = ['Arcane Charge']
        
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
    def getDmg(self):
        d = self.charNeonpewpew.spellPower*1.21
        d = d+d*self.charNeonpewpew.masteryP*self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        if ArcaneCharge in self.charNeonpewpew.buffList.values():
            chargeMulti = self.charNeonpewpew.buffList['Arcane Charge'].stacks
            d=d+d*chargeMulti*0.5
        return d
    
    def cast(self):
        self.damageDone=self.getDmg(self)
        # totalDMG+=self.getDmg()
        manaC = self._manaCost
        if ArcanePowerBuff in self.charNeonpewpew.buffList:
            manaC *= 0.9
        if ArcaneCharge in self.charNeonpewpew.buffList:
            self.charNeonpewpew._mana-=manaC*(1+self.charNeonpewpew.buffList['Arcane Charge'].stacks)
        else:
            self.charNeonpewpew._mana-=manaC
            
        
        
        self.currentCD = self._cooldown
        #   self.addToTotalCastTime()
        
        self.applyCharge(self)
        