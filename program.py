#Code for game inventory/item list
#Sets a number to each item
iN = ['Pocket Lint', 'Dagger', 'Potion', 'Ragged Clothes']
#Sets a sell amount to each item
iNW = {'iN(0)': 0, 'iN(1)': 12, 'iN(2)': 24, 'iN(3)': 30}
#Sets a buy amount to each item
iNB = {'iN(0)': 2, 'iN(1)': 32, 'iN(2)': 35, 'iN(3)': 45}
money = 500
inventory = ['iN(1)']
#Prints what you have in your inventory and how much each item is worth wether buying or selling, and how much money you have
for key in inventory:
    print key
    print "Your money: " money
    print "Sell: %s" % iNW[key]
    print "Buy: %s" % iNB[key]
