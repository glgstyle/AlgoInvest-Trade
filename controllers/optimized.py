'''The optimized version of brute brute force controller'''

from genericpath import exists
from models.action import Action
import csv


class Optimized:
    def __init__(self):
        '''Has a list of actions and a view.'''
        self.actions = []

    def recordActions(self):
        '''Extracting datas from actions csv data folder
           converting in Action objects and return them.'''
        # with open('datas/dataset1_Python+P7.csv', newline='') as csvfile:
        # with open('datas/dataset2_Python+P7.csv', newline='') as csvfile:
        with open('datas/actions.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # skip the header
            next(reader, None)
            for action in reader:
                name = action[0]
                # print(name)
                cost = action[1]
                profit = action[2]
                act = Action(name, cost, profit)
                self.actions.append(act)
            return self.actions

    def findBestRateActions(self):
        """Look for the best profit actions cut list in two,
           and return best upper half."""
        actions = self.recordActions()
        half = len(actions)/2
        actionsList = []
        benefits = 0
        for action in actions:
            actionsList.append((action))
        sorted_by_profit = sorted(actionsList, key=lambda x: -x.profit)
        upperHalf = sorted_by_profit[0:int(half)]
        # print(upperHalf)
        return upperHalf
    
    # def OptimizedBruteForce(self, actions, selection=[]):
    #     """Look for all combinations of actions and choose
    #        the one with the best profit."""
    #     if len(actions) > 0:
    #         first = actions.pop(0)
    #         option1 = self.OptimizedBruteForce(actions.copy(), selection + [first])
    #         option2 = self.OptimizedBruteForce(actions.copy(), selection)
    #         if option1 is not None and option1[0] <= 500 and option1[1] > option2[1]:
    #             return option1
    #         if option2 is not None and option2[0] <= 500:
    #             return option2
    #         elif option1 is None and option2 is None:
    #             return None
    #         else:
    #             return option2
    #     else:
    #         total=0
    #         benefits = 0
    #         for action in selection:
    #             cost = action.cost
    #             rate = action.profit
    #             total = total + cost
    #             benefits = benefits + (cost * rate)/100
    #         if total <= 500:
    #             combo = (total, benefits, selection)
    #             return combo
    #         else:
    #             return None

    # def OptimizedBruteForce(self, actions, selection=[]):
    #         """Look for all combinations of actions and choose
    #         the one with the best profit."""
    #         if len(actions) > 0:
    #             total = 0
    #             first = actions.pop(0)
    #             new_selection = selection + [first]
    #             for action in new_selection:
    #                 cost = action.cost
    #                 total = total + cost
    #             if total > 500:
    #                 option1 = None
    #             else:
    #                 option1 = self.OptimizedBruteForce(actions.copy(), selection + [first])
    #             option2 = self.OptimizedBruteForce(actions.copy(), selection)
    #             if option1 is None and option2 is not None:
    #                 return option2
    #             elif option2 is None and option1 is not None:
    #                 return option1
    #             elif option1 is None and option2 is None:
    #                 return None
    #             elif option1[1] > option2[1]:
    #                 return option1
    #             else:
    #                 return option2
    #         else:
    #             total = 0
    #             benefits = 0
    #             for action in selection:
    #                 cost = action.cost
    #                 rate = action.profit
    #                 total = total + cost
    #                 benefits = benefits + (cost * rate)/100
    #             # print("total, benefits, selection",total, benefits, selection)
    #             if total <= 500:
    #                 return (total, benefits, selection)
    #             else:
    #                 return None
    def OptimizedBruteForce(self, actions):

        combinaisons = []

        # wallet = 500
        # matrice = [capacity for capacity in range(wallet + 1)]
        # for capacity in matrice: 
        #     # print("capacity :", capacity)
        #     combinaisons.append(capacity)
        #     for action in actions:
        #         if action.cost <= capacity:
        #             # print((action.name,action.cost))
        #             combinaisons.append([capacity, (action.name, action.cost)])
        # print(combinaisons)

        actions = [("A", 1), ("B", 5), ("C", 2), ("D", 3)]
        wallet = 5
        matrice = [capacity for capacity in range(wallet + 1)]
        for capacity in matrice: 
            # print("capacity :", capacity)
            for action in actions:
                if action[1] <= capacity:
                    liste = action[0],action[1]
                    # print(liste)
                    print([capacity , liste])
                    combinaisons.append([capacity , liste])
        print(combinaisons)
