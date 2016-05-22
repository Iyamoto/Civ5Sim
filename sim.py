import civ5

units = []

units.append(civ5.unit('Worker', 105))
units.append(civ5.unit('Warrior', 60))
units.append(civ5.unit('Scout', 37))
units.append(civ5.unit('Archer', 40))

buildings = []

t = (0,0,0,2,0)
buildings.append(civ5.building('Monument', 40, 1, t))

print(units[0])
print(buildings[0].getTraits())
