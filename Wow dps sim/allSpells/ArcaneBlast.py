'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from spells.SpellType import SpellType
from allSpells.ArcaneCharge import ArcaneCharge
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
            chargeMulti = self.charNeonpewpew.buffList['ACharge'].stacks
            d=d+d*chargeMulti*0.5
        return d
    
        '''  def priority(self):
        prio = (self.getDmg()/self.getCastTime())/self._manaCost*(1+charNeonpewpew.buffList['ACharge'].stacks)
        #if ArcaneCharge in charNeonpewpew.buffList.values():
        if charNeonpewpew.buffList['ACharge'].stacks < 4:
            if charNeonpewpew.phase == "burst":
                prio*6
            elif charNeonpewpew.phase == "conserve":
                if charNeonpewpew._mana/charNeonpewpew._maxMana < 0.93:
                    prio *= 4
    '''
    def cast(self):
        self.damageDone=self.getDmg(self)
        # totalDMG+=self.getDmg()
        self.charNeonpewpew._mana-=self._manaCost*(1+self.charNeonpewpew.buffList['ACharge'].stacks)
        
        self.currentCD = self._cooldown
        #   self.addToTotalCastTime()
        
        self.applyCharge(self)
        