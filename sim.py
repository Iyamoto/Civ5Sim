import civ5

#Testing
#TODO check return codes
print('Self testing')
civ5.checksim('Production', 37, 8.5) #Scout
civ5.checksim('Science', 55, 14.0) #First tech
civ5.checksim('Citizens', 2, 10.2) #Population 2
civ5.checksim('Citizens', 3, 21.7)
civ5.checksim('Citizens', 4, 32.4)
print("Test finished\n")

def test0(city=(0,0,0,0,0)):
    print(civ5.multisim(50, 1000, 'Production', 37, city))
    print(civ5.multisim(50, 1000, 'Science', 55, city))
    print(civ5.multisim(50, 1000, 'Citizens', 2, city))

#Given start city position (food, production, gold, culture, science)
#TODO Check Food in civ
print('Grassland') 
test0(civ5.starts['Grassland'])
print('Hill')
test0(civ5.starts['Hill'])
print('Plains') 
test0(civ5.starts['Plains'])

#TODO Compare start positions
#TODO Find best start for given goal

##units = []

##units.append(civ5.unit('Worker', 105))
##units.append(civ5.unit('Warrior', 60))
##units.append(civ5.unit('Scout', 37))
###units.append(civ5.unit('Archer', 40))
##
##buildings = []
##
##buildings.append(civ5.building('Monument', 40, 1, (0,0,0,2,0)))

##print(units[0])
##print(buildings[0].getTraits())
