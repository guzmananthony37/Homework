#Anthony Guzman         CIS2348             1503239
lemonJuice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))

agaveNectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', servings, 'servings')
print(lemonJuice, 'cup(s) lemon juice')
print(water, 'cup(s) water')
print(agaveNectar, 'cup(s) agave nectar\n')

desiredNumberOfServings = float(input('How many servings would you like to make?\n'))

print('\nLemonade ingredients - yields', desiredNumberOfServings, 'servings')
serving = desiredNumberOfServings / servings

lemonJuice = lemonJuice * serving
water = water * serving
agaveNectar = agaveNectar * serving

print(lemonJuice, 'cup(s) lemon juice')
print(water, 'cup(s) water')
print(agaveNectar, 'cup(s) agave nectar\n')

print('Lemonade ingredients - yields', desiredNumberOfServings, 'servings')
lemonGallon = lemonJuice / 16
waterGallon = water / 16
agaveGallon = agaveNectar / 16

print(lemonGallon, 'gallon(s) lemon juice')
print(waterGallon, 'gallon(s) water')
print(agaveGallon, 'gallon(s) agave nectar')