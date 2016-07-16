'''
Created on Jul 16, 2016

@author: Neonkitza
'''
import random
from abc import ABCMeta, abstractmethod
from spells.SpellType import SpellType
class Spell(object):
    __metaclass__ = ABCMeta
#    global charNeonpewpew
    '''  name = ''
    cooldown = 0
    manaCost = 0
    castTime = 0
    duration = 0
    spellType = None
    channelTime = 0
    modifiers = None
    listAffectedSpells = []'''
    
    def __init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,castable,char):
        self._name=name
        self._cooldown = cooldown
        self._manaCost = manaCost
        self._castTime = castTime
        self._duration = duration
        self._durationRemaining = 0
        self._spellType = spellType
        self._castable = castable
        self._priority = 0
        self.currentCD = 0
        self.damageDone = 0
        self.charNeonpewpew = char
    def getPriority(self):
        return self._priority
    def setPriority(self,pro):
        self._priority = pro
        
    def increasePriority(self):
        self._priority+=1
    def decreasePriority(self):
        self._priority-=1
        
        
    def __repr__(self):
        return repr(self._priority)
    
    
    @abstractmethod
    def getDmg(self):
        pass
    
    def getCastTime(self):
        return self._castTime/(1+self.charNeonpewpew.hasteP)
    @abstractmethod
    def getDPS(self):
        pass
    def applyCharge(self,indi):
        '''if 
            if random.randint(0,100) <= 30:'''
        if self._name == 'Arcane Blast' or self._name == 'Arcane Missiles':
            if ArcaneCharge in self.charNeonpewpew.buffList.values():
                self.charNeonpewpew.buffList['Arcane Charge'].applyStack()
#                print("Arcane Charge stack applied "+str(self.charNeonpewpew.buffList['Arcane Charge'].stacks))
            else:
                a=ArcaneCharge(self.charNeonpewpew)
                self.charNeonpewpew.buffList['Arcane Charge'] = a
#                print("Arcane Charge created")
        elif self._name == 'Arcane Barrage':
            if ArcaneCharge in self.charNeonpewpew.buffList.values():
                del self.charNeonpewpew.buffList['Arcane Charge']
#                print("Arcane Charge deleted")
        elif self._name == 'Arcane Explosion':
            if random.randint(0,100) <= 30:
                if ArcaneCharge in self.charNeonpewpew.buffList.values():
                    self.charNeonpewpew.buffList['Arcane Charge'].applyStack()
#                    print("Arcane Charge stack applied "+str(self.charNeonpewpew.buffList['Arcane Charge'].stacks))
                else:
                    a=ArcaneCharge(self.charNeonpewpew)
                    self.charNeonpewpew.buffList['Arcane Charge'] = a
#                    print("Arcane Charge created")
    
    
    @abstractmethod
    def cast(self):
        pass
    def decreaseDuration(self):
        if self._durationRemaining>0:
            self._durationRemaining-=1
#         if self._durationRemaining==0:
#             del self.charNeonpewpew.buffList[self._name]
    def resetDuration(self):
        self._durationRemaining = self._duration
    def applyMissiles(self):
        if random.randint(0,100)<30 and self._spellType==SpellType.dps and self._name!="Arcane Missiles":
            if ArcaneMissilesBuff in self.charNeonpewpew.buffList:
                self.charNeonpewpew.buffList['Arcane Missiles buff'].applyStack()
                self.charNeonpewpew.buffList['Arcane Missiles buff'].resetDuration()
            else:
                amb = ArcaneMissilesBuff(self.charNeonpewpew)
                self.charNeonpewpew.buffList['Arcane Missiles buff'] = amb
    def addToTotalCastTime(self,indi):
        if self._castTime < self.charNeonpewpew.GCDCalc():
            indi.totalCastTime+=self.charNeonpewpew.GCDCalc()
        else:
            indi.totalCastTime+=self._castTime
    def castTime(self):
        if self.getCastTime()<self.charNeonpewpew.GCDCalc():
            return self.charNeonpewpew.GCDCalc()
        else:
            return self.getCastTime()
    def decreaseCD(self):
        if self.currentCD>0:
            self.currentCD-=1
        if self.currentCD <= 0:
            self.currentCD = 0
            
    def dmgDone(self,dmg):
        if ArcanePowerBuff in self.charNeonpewpew.buffList:
            self.damageDone*=1.2
        self.damageDone = dmg
        
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
        self.damageDone=self.getDmg()
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
        self.damageDone=self.getDmg()
        self.currentCD = self._cooldown
        manaC = self._manaCost
        if ArcanePowerBuff in self.charNeonpewpew.buffList:
            manaC *= 0.9
        self.charNeonpewpew._mana-=manaC
       
        if ArcaneCharge in self.charNeonpewpew.buffList:       
            self.charNeonpewpew.buffList['Arcane Charge'].removeStacks()
    
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
        
class ArcanePower(Spell):

    def __init__(self,char):
        name = 'Arcane Power'
        cooldown = 90
        manaCost = 0
        castTime = 0
        duration = 0
        spellType = SpellType.CD
        channelTime = 0
        modifiers = None
        listAffectedSpells = ['Arcane Blast', 'Arcane Missiles', 'Arcane Explosion', 'Arcane Barrage']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
    def cast(self):
        apb = ArcanePowerBuff(self.charNeonpewpew)
        self.charNeonpewpew.buffList[apb._name] = apb
    
class ArcanePowerBuff(Spell):
    def __init__(self,char):
        name = 'Arcane Power buff'
        cooldown = 0
        manaCost = 0
        castTime = 0
        duration = 15
        spellType = SpellType.buff
        channelTime = 0
        modifiers = None
        listAffectedSpells = []
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False,char)

class ArcaneMissilesBuff(Spell):

    def __init__(self,char):
        name = 'Arcane Missiles buff'
        cooldown = 0
        manaCost = 0
        castTime = 0
        duration = 15
        spellType = SpellType.buff
        channelTime = 0
        modifiers = None
        ArcaneCharge.stacks = 1
        listAffectedSpells = ['Arcane Missiles']
        self.stacks = 1
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False,char)
        
           
    def getDmg(self):
        pass
    def applyStack(self):
        self._durationRemaining = self._durationRemaining
        if ArcaneMissilesBuff.stacks<3:
            ArcaneMissilesBuff.stacks+=1
        #duration = 15
    
    def removeStacks(self):
        self.stacks = 0
        del self.charNeonpewpew.buffList['Arcane Missiles buff']
    def removeStack(self):
        self.stacks-=1
        if self.stacks==0:
            self.removeStacks()
        
class ArcaneCharge(Spell):
  
    def __init__(self,char):
        name = 'Arcane Charge'
        cooldown = 0
        manaCost = 0
        castTime = 0
        duration = 15
        spellType = SpellType.buff
        channelTime = 0
        modifiers = None
        self.stacks = 1
        listAffectedSpells = ['Arcane Blast', 'Arcane Missiles', 'Arcane Explosion', 'Arcane Barrage','Evocation']
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False,char)
        
           
    def getDmg(self):
        d =  5*self.charNeonpewpew.spellPower*0.747
        d = d+d*self.charNeonpewpew.masteryP*self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        return d
    def applyStack(self):
        self._durationRemaining = self._duration
        if self.stacks<4:
            self.stacks+=1
        #duration = 15
    
    def removeStacks(self):
        self.stacks = 0
        del self.charNeonpewpew.buffList['Arcane Charge']
        
class Evocation(Spell):
#   global charNeonpewpew

    def __init__(self,char):
        name = 'Evocation'
        cooldown = 90
        manaCost = 0
        castTime = 0
        duration = 6
        spellType = SpellType.CD
        channelTime = 0
        modifiers = None
        listAffectedSpells = []
    
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
    def cast(self):
#       currentMana = charNeonpewpew._mana/charNeonpewpew._maxMana

        
#     apb = EvocationBuff(self.charNeonpewpew)
#     self.charNeonpewpew.buffList[apb._name] = apb
        
#        self._durationRemaining = self._duration
        self.currentCD = self._cooldown
  
        self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.15
        
        faliMane = 1-self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        kolikoTraje = faliMane//(self.charNeonpewpew._maxMana*0.075)
        if kolikoTraje < self._duration:
            self._duration = kolikoTraje
            
        self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.075*self._duration
#             
            
#         if i<self.charNeonpewpew.GCDCalc():
#             totalCastTime+=self.charNeonpewpew.GCDCalc()
#         else:
#             totalCastTime+=i


# class EvocationBuff(Spell):
#     def __init__(self,char):
#         name = 'Evocation buff'
#         cooldown = 0
#         manaCost = 0
#         castTime = 0
#         duration = 6
#         spellType = SpellType.buff
#         channelTime = 0
#         modifiers = None
#         listAffectedSpells = []
#         self.relativeDuration = 0
#         Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False,char)
#     
#     def decreaseDuration(self):
#         
#         if self.charNeonpewpew._mana<self.charNeonpewpew._maxMana and self.relativeDuration<self._durationRemaining:
#             self.relativeDuration+=1
#             self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.075
            