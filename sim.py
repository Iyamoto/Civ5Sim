import civ5

units = []

units.append(civ5.unit('Worker', 105))
units.append(civ5.unit('Warrior', 60))
units.append(civ5.unit('Scout', 37))
#units.append(civ5.unit('Archer', 40))

buildings = []

buildings.append(civ5.building('Monument', 40, 1, (0,0,0,2,0)))

##print(units[0])
##print(buildings[0].getTraits())

print(civ5.multisim(50, 1000, 'Production', 37))
print(civ5.multisim(50, 1000, 'Science', 55))
print(civ5.multisim(50, 1000, 'Citizens', 2))
print(civ5.multisim(50, 1000, 'Citizens', 3))
print(civ5.multisim(50, 1000, 'Citizens', 4))

