'''
Created on Jul 15, 2016

@author: Neonkitza
'''
from characters.Neonpewpew import charNeonpewpew
class ArcaneMissilesBuff(Spell):
    global charNeonpewpew
    stacks = 0
    def __init__(self):
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
        
        Spell.__init__(self,name,cooldown,manaCost,castTime,duration,spellType,listAffectedSpells,modifiers,channelTime,False)
        
           
    def getDmg(self):
        pass
    def applyStack(self):
        if ArcaneMissilesBuff.stacks<3:
            ArcaneMissilesBuff.stacks+=1
        #duration = 15
    
    def removeStacks(self):
        stacks = 0
    def removeStack(self):
        stacks-=1
        if stacks==0:
            del charNeonpewpew.buffList['AMissilesBuff']
        