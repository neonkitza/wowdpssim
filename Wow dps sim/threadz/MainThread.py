'''
Created on Jun 28, 2016

@author: Neonkitza
'''
import threading
import time
from characters.Neonpewpew import charNeonpewpew, totalCastTime, endTime
from allSpells.ArcaneBarrage import ArcaneBarrage
from allSpells.ArcaneBlast import ArcaneBlast
from allSpells.ArcaneCharge import ArcaneCharge
from allSpells.ArcaneExplosion import ArcaneExplosion
from allSpells.ArcaneMissiles import ArcaneMissiles
from spells.SpellType import SpellType


exitFlag = 0
global charNeonpewpew
global totalCastTime
global endTime
class MainThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        while totalCastTime<endTime:
            self.counter+=1
            print(self.counter)

def neonSpells():
    a = ArcaneBarrage()
    charNeonpewpew.spellList['ABarrage'] = a
    a = ArcaneBlast()
    charNeonpewpew.spellList['ABlast'] = a
    a = ArcaneExplosion()
    charNeonpewpew.spellList['AExplosion'] = a
    a = ArcaneMissiles()
    charNeonpewpew.spellList['AMissiles'] = a
    a = ArcaneCharge()
    charNeonpewpew.spellList['ACharge'] = a
    for key in charNeonpewpew.spellList:
        if charNeonpewpew.spellList[key]._spellType == SpellType.dps:
            charNeonpewpew.castSpellList[key] = charNeonpewpew.spellList[key]

    

# Create new threads
neonSpells()
print(charNeonpewpew.castSpellList)
thread1 = MainThread(1, "Thread-1", 1)

# Start new Threads

thread1.start()
