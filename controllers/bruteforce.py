'''The brute brute force controller'''

from models.action import Action
import csv


class BruteForce:
    def __init__(self):
        '''Has a list of actions.'''
        self.actions = []

    def recordActions(self):
        '''Extracting datas from actions csv data folder
           converting in Action objects and return them.'''
        with open('datas/actions.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # skip the header
            next(reader, None)
            for action in reader:
                name = action[0]
                cost = action[1]
                profit = action[2].replace("%", "")
                act = Action(name, int(cost), int(profit))
                self.actions.append(act)
            return self.actions

    def bruteForce(self, actions, selection=[]):
        """Look for all combinations of actions and choose
           the one with the best profit."""
        if len(actions) > 0:
            first = actions.pop(0)
            option1 = self.bruteForce(actions.copy(), selection + [first])
            option2 = self.bruteForce(actions.copy(), selection)
            if option1 is None and option2 is not None:
                return option2
            elif option2 is None and option1 is not None:
                return option1
            elif option1 is None and option2 is None:
                return None
            elif option1[1] > option2[1]:
                return option1
            else:
                return option2
        else:
            total = 0
            benefits = 0
            for action in selection:
                cost = action.cost
                rate = action.profit
                total = total + cost
                benefits = benefits + (cost * rate)/100
            # print("total, benefits, selection",total, benefits, selection)
            if total <= 500:
                return (total, benefits, selection)
            else:
                return None
