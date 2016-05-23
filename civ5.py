#Main class lib
#http://civilization.wikia.com/wiki/Game_concepts_%28Civ5%29
#http://civilization.wikia.com/wiki/Mathematics_of_Civilization_V

import random
import math

starts = {}    
starts['Desert'] = (2,4,3,0,3)
starts['Grassland'] = (2,4,3,0,3)
starts['Hill'] = (2,5,3,0,3)
starts['Plains'] = (2,4,3,0,3)
starts['Tundra'] = (2,4,3,0,3)
starts['Forest'] = (2,4,3,0,3)
starts['Jungle'] = (2,3,3,0,3)

def checksim(target='Production', value=37, goodmean=8.5):
    t, v, mean, dev = multisim(50, 1000, target, value)
    if abs(mean-goodmean)<0.05*goodmean:
        print(target, goodmean, mean, '- OK')
        return True
    else:
        print(target, goodmean, mean, '- Bad', )
        return False

def multisim(maxturns=50, runs = 1000, target='Production', value=37, city=(0,0,0,0,0)):
    data = []
    for i in range(runs):
        data.append(simulate(maxturns, target, value, city))

    mean = round(sum(data)/float(len(data)),2)
    dev = round(stdDev(data),2)
    return(target, value, mean, dev)

def simulate(maxturns=10, target='Production', value=37, city=(0,0,0,0,0)):
    """ City (food, production, gold, culture, science) """
    #Initial state
    Food = 0   
    Production = 0
    Gold = 0
    Culture = 0
    Science = 0
    Units = 1
    Citizens = 1
    Cities = 1

    #Modifiers
    dCulture = 1

    #City hex
    if sum(city)==0:
        CityScience = 3
        CityGold = 3
        CityFood = 2
        CityProduction = random.randint(4,5)
        CityCulture = 0
    else:
        CityFood, CityProduction, CityGold, CityCulture, CityScience = city

    #Fill Hexes
    Hex = {}
    Max = 4
    for i in range(10):
        Hex[i,'Food'] = random.randint(1,3)
        Max = Max - Hex[i,'Food']
        if Max<1:
            Hex[i,'Production']=0
            Hex[i,'Gold'] = 0
        else:
            Hex[i,'Production'] = random.randint(0,Max)
            Max = Max - Hex[i,'Production']
            if Max<1:
                Hex[i,'Gold'] = 0
            else:
                Hex[i,'Gold'] = random.randint(0,Max)

    #Let the game begin
    for turn in range(1,maxturns):
        d = {'Production': Production, 'Science': Science, 'Citizens': Citizens }      
        if d[target]>=value:
            return turn-1
        
##        print("Turn:", turn)
##        printState(Citizens, Food, Production, Gold, Culture, Science)
        #Culture
        Culture = Culture + CityCulture + dCulture
        #Gold
        CitizenGold = 0
        for n in range(Citizens):
            CitizenGold = CitizenGold + Hex[n,'Gold']
        Gold = Gold + CityGold +CitizenGold - getUnitMaintenance(turn, Units)
        #Science
        Science = Science + CityScience + Citizens
        #Production
        CitizenProduction = 0
        for n in range(Citizens):
            CitizenProduction = CitizenProduction + Hex[n,'Production']
        Production = Production + CityProduction + CitizenProduction
        #print(getTechCost(Cities))
        #Food
        CitizenFood = 0
        for n in range(Citizens):
            CitizenFood = CitizenFood + Hex[n,'Food']
        Food = Food + CityFood + CitizenFood - Citizens*2
        if Food>=getFoodCost(Citizens):
            Food-=getFoodCost(Citizens)
            Citizens+=1



    return turn

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def getTechCost(cities):
    base = 55
    cost = int(base+(cities-1)*0.05*base)
    return cost

def getFoodCost(n):
    """n - number of citizens"""
    food = int(math.floor(15+6*(n-1)+(n-1)**1.8))
    return food

def getUnitMaintenance(turn, units):
    """units - number of units"""
    if units==0:
        return 0
    if turn<20:
        return int(math.ceil(0.5*units))
    if turn<50:
        return int(math.ceil(0.75*units))
    if turn<100:
        return int(math.ceil(1.3*units))
    
    
def printState(citizens=1, food=0, production=0, gold=0, culture=0, science=0):
    print("Citizens:", citizens, "Food:", food, "Production:", production, "Gold:", gold, "Culture:", culture, "Science:", science)

class unit(object):
    def __init__(self, name='', cost=0):
        self.Name = str(name)
        self.Cost = int(cost)

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.Name

    def getCost(self):
        return self.Cost



class building(object):
    def __init__(self, name='', cost=0, maintenance=1, traits=(0,0,0,0,0)):
        """ Traits (food, production, gold, culture, science) """
        self.Name = str(name)
        self.Cost = int(cost)
        self.Maintenance = int(maintenance)
        self.Traits = traits

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.Name

    def getCost(self):
        return self.Cost

    def getMaintenance(self):
        return self.Maintenance

    def getTraits(self):
        return self.Traits
