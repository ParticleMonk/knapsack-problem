import knapsack


file = open("Program2Input.txt", "r")
itemSet = []
for line in file:
    itemData = []
    itemDatatemp = line.split()
    for value in itemDatatemp:
        itemData.append(float(value))
    itemData.append(0)
    itemSet.append(itemData)

test_knapsack = knapsack.KnapSack(itemSet)

test_knapsack.initial_randomize()

test_knapsack.calculateWeight()
test_knapsack.calculateUtility()
print(test_knapsack.utility)

test_knapsack.rearrange()

print(test_knapsack.utility)

test_knapsack.anneal(90, .6, 0.01)

print(test_knapsack.utility)
print(test_knapsack.totalWeight)
print('knapsack created')

exit()