import knapsack
import random
import math


def get_newKnapsack(oldItemList):
    new_knapsack_arrangement = knapsack(oldItemList)
    new_knapsack_arrangement.rearrange()

    return new_knapsack_arrangement

class annealing:
    """A simple example class"""

    def report(self, knapsackIncoming, initialTemp, finalTemp = .1, alpha = 0.01):
        initial_temp = initialTemp
        final_temp = finalTemp
        alpha = alpha

        current_temp = initial_temp
        currentKnapsack = knapsackIncoming
        current_arrangement = knapsackIncoming.itemList
        change_count = 0
        attempt_count = 0

        currentKnapsack.calculateWeight()
        currentKnapsack.penalize()
        currentKnapsack.calculateUtility()

        while current_temp > final_temp:
            newknapsack = get_newKnapsack(current_arrangement)
            newknapsack.calculateWeight()
            newknapsack.calculateUtility()
            newknapsack.penalize()

            utility_diff = currentKnapsack.utility - newknapsack.utility

            if utility_diff > 0:
                current_arrangement = newknapsack.itemList
                currentKnapsack = newknapsack
                change_count += 1

            else:
                if random.uniform(0, 1) < math.exp(-utility_diff / current_temp):
                    current_arrangement = newknapsack.itemList
                    currentKnapsack = newknapsack
                    change_count += 1

            attempt_count += 1
            if change_count == 4000:
                current_temp -= alpha
            if attempt_count == 40000 and change_count == 0:
                break
            elif attempt_count == 40000:
                current_temp -= alpha

        return currentKnapsack.utility, currentKnapsack.weight
