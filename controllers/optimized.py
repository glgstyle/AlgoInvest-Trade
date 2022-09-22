'''The optimized version of brute brute force controller'''

from models.action import Action
import csv


class Optimized:
    def __init__(self):
        '''Has a list of actions and a view.'''
        self.actions = []

    def recordActions(self):
        '''Extracting datas from actions csv data folder
           converting in Action objects and return them.'''
        with open('datas/actions.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            # skip the header
            next(reader, None)
            for action in reader:
                name = action[0]
                cost = action[1]
                profit = action[2].replace("%", "")
                act = Action(name, int(cost), int(profit))
                self.actions.append(act)
            return self.actions

    def findBestRateActions(self):
        """Look for the best profit actions cut list in two,
           and return best upper half."""
        actions = self.recordActions()
        half = len(actions)/2
        actionsList = []
        for action in actions:
            actionsList.append((action))
        sorted_by_profit = sorted(actionsList, key=lambda x: -x.profit)
        upperHalf = sorted_by_profit[0:int(half)]
        return upperHalf
    
    def bruteForce(self, actions, selection=[], total=0):
        """Look for all combinations of actions and choose
           the one with the best profit."""
        if len(actions) > 0:
            first = actions.pop(0)
            option1 = self.bruteForce(actions.copy(), selection + [first], total)
            option2 = self.bruteForce(actions.copy(), selection, total)
            if option1 is not None and option1[0] <= 500 and option1[1] > option2[1]:
                return option1
            if option2 is not None and option2[0] <= 500:
                return option2
            elif option1 is None and option2 is None:
                return None
            else:
                return option2
        else:
            benefits = 0
            for action in selection:
                cost = action.cost
                rate = action.profit
                total = total + cost
                benefits = benefits + (cost * rate)/100
            if total <= 500:
                return (total, benefits, selection)
            else:
                return None
# optimized = Optimized()
# actions = optimized.findBestRateActions()
# print(optimized.bruteForce(actions))

