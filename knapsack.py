import annealing
import random

class KnapSack:
    """A simple example class"""
    def __init__(self, itemList ):
        self.itemList = itemList
        self.utility = 1000
        self.totalWeight = 0

        return None

    #creates the first 1/20 selection of items
    def initial_randomize(self):
        item_count = self.itemList.size()/20
        for list in self.itemList:
            if random() > 0.5:
                list[2] = 1
            if item_count == 1:
                break
            else:
                item_count -= 1



        return None

    #Selects a random item and changes its memebership value [2]
    def rearrange(self):
        temp_index = random.randrange(self.itemList.size)
        if self.itemList[temp_index][2] == 0:
            self.itemList[temp_index][2] = 1
        else:
            self.itemList[temp_index][2] = 0

        return None



    def calculateWeight(self):
        for list in self.itemList:
            if list[2] == 1:
                self.totalWeight += list[1]
        return self.totalWeight

    def calculateUtility(self):
        totalUtility = 0
        for list in self.itemList:
            totalUtility -= list[0]
        return None

    def penalize(self):
        if self.totalWeight > 500:
            self.utility += (self.totalWeight-500)*20
        return None

    def weight(self):
        return self.totalWeight

    def utility(self):
        return self.utility

    #performs the annealing funtion from the anneal file
    def anneal(self, initialTemp, finalTemp, alpha):
        #This might be able to be replaced and pull the annealing function inside the knapsack
        self.utility, self.totalWeight = annealing.report(self, initialTemp, finalTemp, alpha)
        return None

