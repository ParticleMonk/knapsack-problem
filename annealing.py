import knapsack
import random
import math

#Defines the function for generating the "next" knapsack
def get_newKnapsack(oldItemList):
    new_knapsack_arrangement = knapsack.KnapSack(oldItemList)
    new_knapsack_arrangement.rearrange()
    return new_knapsack_arrangement

#This is where the annealing is taking place.
def report(knapsackIncoming, initialTemp, finalTemp=.1, alpha=0.01):
    initial_temp = initialTemp
    final_temp = finalTemp
    alpha = alpha
#initializes the variables for the annealing while loop
    current_temp = initial_temp
    currentKnapsack = knapsackIncoming
    current_arrangement = knapsackIncoming.itemList
    change_count = 0
    attempt_count = 0

#Makes sure that the currentKnapsack has a weight and a utility score
    currentKnapsack.calculateWeight()
    currentKnapsack.calculateUtility()


#Annealing while loop
    while current_temp > final_temp:

        #gets next knapsack
        newknapsack = get_newKnapsack(current_arrangement)


        #compares next knapasck with old one
        utility_diff = currentKnapsack.utility - newknapsack.utility
        print()
        #If the new one has a better (lower) utility score then it replaces the current knapsack
        if utility_diff > 0:
            current_arrangement = newknapsack.itemList
            currentKnapsack = newknapsack
            change_count += 1
        #If not we do the main calculation in our annealing which is e^(-delta/temp) if its higher than a random number
        else:
            try:
                if random.uniform(0, 1) < math.exp(-utility_diff / current_temp):
                    current_arrangement = newknapsack.itemList
                    currentKnapsack = newknapsack
                    change_count += 1
            except OverflowError:
                print('math.exp() Over flowed')

        attempt_count += 1

        #Stops annealing if no changes over 40000 loops
        if attempt_count > 40000 and change_count == 0:
            break

        #lowers temp every 40000 loops
        if attempt_count > 40000:
            print(current_temp, '<< current_temp from attempt\n')
            current_temp -= alpha
            attempt_count = 0
            continue

        #lowers temp every 4000 changes
        if change_count > 4000:
            current_temp -= alpha
            change_count = 0
            print(current_temp, '<< current_temp from change \n')
            print(currentKnapsack.totalWeight, "Weight", currentKnapsack.utility, 'Utility')

            continue



    return currentKnapsack.utility, currentKnapsack.totalWeight, currentKnapsack.itemList
