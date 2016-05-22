import civ5
import math

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

units = []

units.append(civ5.unit('Worker', 105))
units.append(civ5.unit('Warrior', 60))
units.append(civ5.unit('Scout', 37))
#units.append(civ5.unit('Archer', 40))

buildings = []

buildings.append(civ5.building('Monument', 40, 1, (0,0,0,2,0)))

##print(units[0])
##print(buildings[0].getTraits())

runs = 10000
data = []
for i in range(runs-1):
    data.append(civ5.simulate(50))

mean = round(sum(data)/float(len(data)),2)
dev = round(stdDev(data),2)
print(mean, dev)
