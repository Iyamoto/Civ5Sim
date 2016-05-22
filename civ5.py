#Main class lib

import random
import math

def simulate(maxturns=10):
    #Initial state
    Food = 0   
    Production = 0
    Gold = 0
    Culture = 1
    Science = 4
    Units = 0
    Citizens = 1
    Cities = 1

    #Modifiers
    dCulture = 1
    CityScience = 3
    CityGold = 3
    CityFood = random.randint(2,4)
    CityProduction = random.randint(3,5)

    #Let the game begin
    for turn in range(2,maxturns):
        #print("Turn:", turn)
        #printState(Citizens, Food, Production, Gold, Culture, Science)
        #Culture
        Culture += dCulture
        #Gold
        Gold = Gold + CityGold - getUnitMaintenance(turn, Units)
        #Science
        Science = Science + CityScience + Citizens
        #Production
        CitizenProduction = 0
        for n in range(1,Citizens):
            CitizenProduction = CitizenProduction + random.randint(1,3)
        Production = Production + CityProduction + CitizenProduction
        #print(getTechCost(Cities))
        #Food
        CitizenFood = 0
        for n in range(1,Citizens):
            CitizenFood = CitizenFood + random.randint(1,3)
        Food = Food + CityFood + CitizenFood - Citizens*2
        if Food>=getFoodCost(Citizens):
            Food-=getFoodCost(Citizens)
            Citizens+=1
        
        if Production>=37:
            return turn

##        if Science>=55:
##            return turn

    return turn

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
