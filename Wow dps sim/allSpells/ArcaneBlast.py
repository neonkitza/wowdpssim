'''
Created on Jul 1, 2016

@author: Neonkitza
'''
from spells.Spell import Spell
from characters.Neonpewpew import charNeonpewpew,totalDMG,totalCastTime
from spells.SpellType import SpellType
from allSpells.ArcaneCharge import ArcaneCharge

class ArcaneBlast(Spell):
    global charNeonpewpew,totalDMG,totalCastTime
    
    def __init__(self):
        name = 'Arcane Blast'
        cooldown = 0
        manaCost = 0.02*charNeonpewpew._mana
        castTime = 2.25
        duration = 0
        spellType = SpellType.dps
        channelTime = 0
        modifiers = None
        listAffectedSpells = ['Arcane Charge']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True)
        
    def getDmg(self):
        d = charNeonpewpew.spellPower*1.21
        d = d+d*charNeonpewpew.masteryP*charNeonpewpew._mana/charNeonpewpew._maxMana
        if ArcaneCharge in charNeonpewpew.buffList.values():
            chargeMulti = charNeonpewpew.buffList['ACharge'].stacks
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
        charNeonpewpew._mana-=self._manaCost*(1+charNeonpewpew.buffList['ACharge'].stacks)
        totalDMG+=self.getDmg()
        
        self.addToTotalCastTime()
        
        self.applyCharge()
        