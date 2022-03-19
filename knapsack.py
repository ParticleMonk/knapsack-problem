import annealing
import random

class KnapSack:
    """A simple example class"""
    def __init__(self, itemList ):
        self.itemList = itemList
        self.utility = 0
        self.totalWeight = 0

        return None

    #creates the first 1/20 selection of items
    def initial_randomize(self):
        item_count = len(self.itemList)/20
        for list in self.itemList:
            if random.random() > 0.5:
                list[2] = 1
            if item_count == 1:
                break
            else:
                item_count -= 1
        self.calculateUtility()
        self.calculateWeight()
        self.penalize()



        return None

    #Selects a random item and changes its memebership value [2]
    def rearrange(self):
        temp_index = random.randrange(len(self.itemList))
        if self.itemList[temp_index][2] == 0:
            self.itemList[temp_index][2] = 1
            self.calculateUtility()
            self.calculateWeight()
            self.penalize()

        else:
            self.itemList[temp_index][2] = 0
            self.calculateUtility()
            self.calculateWeight()
            self.penalize()
        return None



    def calculateWeight(self):
        temp_weight = 0
        for list in self.itemList:
            if list[2] == 1:
                temp_weight += list[1]

        self.totalWeight = temp_weight

        return None

    def calculateUtility(self):
        temp_utility = 0
        for list in self.itemList:
            if list[2] == 1:
                temp_utility -= list[0]

        self.utility = 1000 + temp_utility

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

