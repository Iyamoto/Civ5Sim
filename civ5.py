#Main class lib

class unit(object):
    def __init__(self, name='', cost=0, maintenance=0.5):
        self.Name = str(name)
        self.Cost = int(cost)
        self.Maintenance = float(maintenance)

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.Name

    def getCost(self):
        return self.Cost

    def getMaintenance(self):
        return self.Maintenance



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
