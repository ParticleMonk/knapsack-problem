# Creates a list of list that are the items and their values
import knapSack


def main():
    print("Derrick Jennings Program 2 for 461 \n")


    print("Reading in inputs...\n")
    file = open('Program2Input.txt', "r")
    itemSet = []
    for line in file:
        itemData = []
        itemDatatemp = line.split()
        for value in itemDatatemp:
            itemData.append(float(value))
        itemData.append(0)
        itemSet.append(itemData)

    print("Incoming Item Set")
    print(itemSet, sep="\n")

    # In this solution we treat the knapsack like a magical bag that you put items into
    # Inside the knapsack is where the annealing, weighting, and scoring will take place
    print('Creating Initial KnapSack \n')
    initial_knapsack = knapSack.KnapSack(itemSet)

    # The knapsack creates a random selection of 1/20 of the passed items and calculates weight and utility score
    initial_knapsack.initial_randomize()

    #Reports the initial data
    print("Stats of Initial KnapSack with 1/20 of items selected at random.\n")
    print(initial_knapsack.utility, "<<<<< Initial utility score (1000-Raw Utitlity) \n")
    print(initial_knapsack.totalWeight, "<<<<< Initial Weight \n \n")

    #Receives parameters for annealing


    print("Attempting to Simulate Annealing\n")

    #anneals the knapsack
    final_knapsack = initial_knapsack.anneal(90, 0.6, 0.01)

    #Prints report to screen
    print( "Utility Score after Annealing>>>", final_knapsack.utility, "\n")
    print( "Weight after Annealing>>>", final_knapsack.totalWeight, "\n")
