'''
Created on Jun 27, 2016

@author: Neonkitza
'''
from simulation.Population import Population
from simulation.Algorithm import Algorithm

generationCount = 0
elapsedTime = 0
END_TIME = 60


prvaPopulacija = Population(10,True)
while generationCount < 10:
    generationCount+=1
    print("Generacija: "+generationCount+ " - Najbolji dmg: "+prvaPopulacija.getFittest().getTotalDmgDone())
    prvaPopulacija = Algorithm.evolvePopulation(prvaPopulacija)
    