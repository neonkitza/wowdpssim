'''
Created on Jun 27, 2016

@author: Neonkitza
'''
from characters.Neonpewpew import Neonpewpew, charNeonpewpew
from allSpells.ArcaneBlast import ArcaneBlast
from allSpells.ArcaneMissiles import ArcaneMissiles

global charNeonpewpew

a = ArcaneBlast()
am = ArcaneMissiles()
b = a.getDmg()
print(a.getDmg())
print(am.getDmg())