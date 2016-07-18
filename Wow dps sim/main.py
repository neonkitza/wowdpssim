
from simulation.Population import Population
from simulation.Algorithm import Algorithm

generationCount = 0
elapsedTime = 0
END_TIME = 60


prvaPopulacija = Population(20,True)
while generationCount < 20:
    print("Generacija: "+str(generationCount)+ " - Najbolji dmg: "+str(prvaPopulacija.getFittest().getTotalDmgDone()))
    generationCount+=1
    prvaPopulacija = Algorithm.evolvePopulation(Algorithm,prvaPopulacija)
    

print("Generacija: "+str(generationCount)+ " - Najbolji dmg: "+str(prvaPopulacija.getFittest().getTotalDmgDone()))