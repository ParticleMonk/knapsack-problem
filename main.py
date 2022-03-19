
#Creates a list of list that are the items and their values


file = open("Program2Input.txt", "r")
itemSet = []
for line in file:
    itemData = []
    itemDatatemp = line.split()
    for value in itemDatatemp:
        itemData.append(float(value))
    itemData.append(0)
    itemSet.append(itemData)


print(itemSet)

#In this solution we treat the knapsack like a magical bag that you put items into
#Inside the knapsack is where the annealing, weighting, and scoring will take place


