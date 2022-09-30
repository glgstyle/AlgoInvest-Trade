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
        with open('datas/dataset1_Python+P7.csv', newline='') as csvfile:
        # with open('datas/dataset2_Python+P7.csv', newline='') as csvfile:
        # with open('datas/actions.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # skip the header
            next(reader, None)
            for action in reader:
                name = action[0]
                # print(name)
                cost = action[1]
                profit = action[2] 
                act = Action(name, cost, profit)
                if act.cost > 0 and act.profit > 0:
                    self.actions.append(act)
            return self.actions

    def print_matrice(self,matrice,i,j):
        input("print when "+str (i)+","+str(j))
        print("-------------------")
        for row in matrice :
            print(row)
    def OptimizedBruteForce(self, wallet, actions):
        # actions =[("A", 1, 1), ("B", 5, 4), ("C", 2, 1), ("D", 3, 2)]
        # convert float value to int
        wallet = wallet * 100
        # init table
        matrice = [[0 for x in range(wallet + 1)] for x in range(len(actions) + 1)]
        # browse actions
        for i in actions:
            i.profit = (i.cost * i.profit/100) / 100
        for row in range(1, len(actions) + 1):
            for capacity in range(1, wallet + 1):# browse amount wallet  1 2 3 4 5 6 7 8 9 10 jusqu'à 500
                # keep the max value if it's lower to the wallet
                if actions[row-1].cost <= capacity:# actions[0][1] <= 1  the price of action should'nt cost more than capacity
                    matrice[row][capacity] = max(
                        actions[row-1].profit + matrice[row-1][capacity - actions[row-1].cost],   
                        matrice[row-1][capacity])
                else:
                    # keep result of previous line if higher
                    matrice[row][capacity] = matrice[row-1][capacity]
                # self.print_matrice(matrice,row,capacity)
        # return element by sum of them
        # we browse reverse the matrice for find the keeped elements 
        n = len(actions)
        action_selection = []
        # while there is money in wallet and actions
        while wallet >= 0 and n >= 0:
            # take the last action in list
            last_action = actions[n-1]
            # calcul the difference between two last lines to find selected elements
            if matrice[n][wallet] == matrice[n-1][wallet - last_action.cost] + last_action.profit:
                action_selection.append(last_action)
                wallet -= last_action.cost
            n -= 1
        total_cost = 0
        for action in action_selection:
            # generate cost value
            action.cost = action.cost / 100
            action.profit = action.profit / 100
            total_cost += action.cost
        return [action_selection, total_cost, matrice[-1][-1]/100]
