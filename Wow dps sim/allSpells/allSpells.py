
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
        self.kolikoBitan = 0
    def getPriority(self):
        return self._priority
    def setPriority(self,pro):
        self._priority = pro
        
    def increasePriority(self):
        if self._priority <10:
            self._priority+=1
    def decreasePriority(self):
        if self._priority>0:
            self._priority-=1
        
        
    def __repr__(self):
        return repr(self._priority)
    
    def applyCast(self):
        castable = True
        if self.charNeonpewpew._mana <= 0:
            castable = False
        if self._name == "Arcane Missiles" and "Arcane Missiles buff" not in self.charNeonpewpew.buffList.keys(): 
                castable = False
        if self.currentCD != 0:
            castable = False
        return castable
        
    
    @abstractmethod
    def getDmg(self):
        pass
    
    def getCastTime(self):
        return self._castTime/(1+self.charNeonpewpew.hasteP)
    @abstractmethod
    def getDPS(self):
        pass
    def applyCharge(self):
        '''if 
            if random.randint(0,100) <= 30:'''
        staIma = []
        for buff in self.charNeonpewpew.buffList.values():
            staIma.append(buff._name)
        if self._name == 'Arcane Blast' or self._name == 'Arcane Missiles':
            if 'Arcane Charge' in staIma:
                self.charNeonpewpew.buffList['Arcane Charge'].applyStack()
            else:
                a=ArcaneCharge(self.charNeonpewpew)
                self.charNeonpewpew.buffList['Arcane Charge'] = a
        elif self._name == 'Arcane Barrage':
            if 'Arcane Charge' in staIma:
                del self.charNeonpewpew.buffList['Arcane Charge']
        elif self._name == 'Arcane Explosion':
            if random.randint(0,100) <= 30:
                if 'Arcane Charge' in staIma:
                    self.charNeonpewpew.buffList['Arcane Charge'].applyStack()
                else:
                    a=ArcaneCharge(self.charNeonpewpew)
                    self.charNeonpewpew.buffList['Arcane Charge'] = a
    
    
    @abstractmethod
    def cast(self):
        pass
    def decreaseDuration(self):
        if self._durationRemaining>0:
            self._durationRemaining-=1
    def resetDuration(self):
        self._durationRemaining = self._duration
    def applyMissiles(self):
        if random.randint(0,100)<30 and self._spellType==SpellType.dps and self._name!="Arcane Missiles":
            if 'Arcane Missiles buff' in self.charNeonpewpew.buffList.keys():
                self.charNeonpewpew.buffList['Arcane Missiles buff'].applyStack()
                self.charNeonpewpew.buffList['Arcane Missiles buff'].resetDuration()
            else:
                amb = ArcaneMissilesBuff(self.charNeonpewpew)
                self.charNeonpewpew.buffList['Arcane Missiles buff'] = amb
#         if 'Arcane Missiles buff' in self.charNeonpewpew.buffList.keys():
#             print("applyMissiles stacks ="+str(self.charNeonpewpew.buffList['Arcane Missiles buff'].stacks))
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
        if "Arcane Power buff" in self.charNeonpewpew.buffList.keys():
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
        if 'Arcane Charge' in self.charNeonpewpew.buffList.keys():
            chargeMulti = self.charNeonpewpew.buffList['Arcane Charge'].stacks
            d=d+d*chargeMulti*0.5
        return d
    
    def cast(self):
        self.damageDone=self.getDmg()
        # totalDMG+=self.getDmg()
        manaC = self._manaCost
        if 'Arcane Power buff' in self.charNeonpewpew.buffList.keys():
            manaC *= 0.9
        if 'Arcane Charge' in self.charNeonpewpew.buffList.keys():
            self.charNeonpewpew._mana-=manaC*(1+self.charNeonpewpew.buffList['Arcane Charge'].stacks)
        else:
            self.charNeonpewpew._mana-=manaC
            
        
        
        self.currentCD = self._cooldown
        #   self.addToTotalCastTime()
        self.applyMissiles()
        self.applyCharge()
        
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
        if 'Arcane Charge' in self.charNeonpewpew.buffList.keys():
            chargeMulti = self.charNeonpewpew.buffList['Arcane Charge'].stacks
            d=d+d*chargeMulti*0.5
        return d
    

    def cast(self):
        
        self.damageDone=self.getDmg()
        self.currentCD = self._cooldown
        manaC = self._manaCost
        if 'Arcane Power buff' in self.charNeonpewpew.buffList.keys():
            manaC *= 0.9
        self.charNeonpewpew._mana-=manaC
        self.applyMissiles()
        if 'Arcane Charge' in self.charNeonpewpew.buffList.keys():       
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
        if 'Arcane Charge' in self.charNeonpewpew.buffList.keys():
            chargeMulti = self.charNeonpewpew.buffList['Arcane Charge'].stacks
            d=d+d*chargeMulti*0.5
        return d
    def cast(self):
        manaC = self._manaCost
        if 'Arcane Power buff' in self.charNeonpewpew.buffList.keys():
            manaC *= 0.9
        self.charNeonpewpew.buffList['Arcane Missiles buff'].removeStack()
        
        self.damageDone=self.getDmg()
        
        if 'Arcane Charge' in self.charNeonpewpew.buffList.keys():
            self.charNeonpewpew._mana-=manaC*(1+self.charNeonpewpew.buffList['Arcane Charge'].stacks)
        else:
            self.charNeonpewpew._mana-=manaC
        
        self.damageDone=self.getDmg()
        
        self.currentCD = self._cooldown
        
        self.applyCharge()

            
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
        self.damageDone=self.getDmg()
        manaC = self._manaCost
        if 'Arcane Power buff' in self.charNeonpewpew.buffList.keys():
            manaC *= 0.9
       
        self.charNeonpewpew._mana-=manaC     
        self.currentCD = self._cooldown
        #   self.addToTotalCastTime()
        self.applyMissiles()
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
        
        self.kolikoBitan = 3
    def cast(self):
        self.currentCD = self._cooldown
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
        
        self._durationRemaining = self._duration
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
        
        self._durationRemaining = self._duration
           
    def getDmg(self):
        pass
    def applyStack(self):
        self._durationRemaining = self._durationRemaining
        if self.stacks<3:
            self.stacks+=1
        
    
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
        
        self._durationRemaining = self._duration
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
        
        self.kolikoBitan = 2
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,True,char)
        
    def cast(self):
        self.currentCD = self._cooldown
  
        self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.15
        
        faliMane = 1-self.charNeonpewpew._mana/self.charNeonpewpew._maxMana
        kolikoTraje = faliMane//(self.charNeonpewpew._maxMana*0.075)
        if kolikoTraje < self._duration:
            self._duration = kolikoTraje
            
        self.charNeonpewpew._mana+=self.charNeonpewpew._maxMana*0.075*self._duration
             
            
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
            