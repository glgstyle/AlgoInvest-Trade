'''The brute brute force controller'''
from itertools import chain, product
from math import nextafter
from models.action import Action
import csv
liste=[ ('a',10),('b',20),('c',10),('d',40)]
actions = [1,2,3,4]
class BruteForce:
    def __init__(self):
        '''Has a list of actions and a view'''
        self.actions = []
    
    def recordActions(self):
        '''Extracting datas from actions csv data folder
           converting in Action objects and return them.'''
        with open('datas/actions.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            # skip the header
            next(reader, None)
            for action in reader:
                act = Action(action[0], action[1], action[2])
                self.actions.append(act)
            # print(self.actions)
        return self.actions

    # def bruteForce(self,actions, selection=[]):
    #     # actionsList= []
    #     # for action in actions:
    #     #     actionsList.append((action.name, action.cost))
    #     # # print(actionsList)
    #     # if len(actions) > 0:
    #     #     first = actionsList.pop(0)
    #     #     print(actionsList)
    #     #     print(first)

    #     # costs= []
    #     # for action in actions:
    #     #     costs.append(action)
    #     # print(costs)
    #     # print(actions)
    #     actionsCopy = actions
    #     if len(actions) > 0:
    #         print(actions)
    #         first = actions.pop(0)
    #         # print(first)
    #         # print(actions.copy())
    #         # # print(first)
    #         for i in actions:
    #             # result1 = self.bruteForce(actions.copy(), selection + [first])
    #             result1 = self.bruteForce(actionsCopy, selection + [first])
    #             print(result1)
            # print(actions)
            # result1 = self.bruteForce(actions.copy(), selection + [first])
            # print(result1)

            # while result1 != None:
            #     print(result1)
            #     return result1

            # print(len(actions))
            # if len(actions) == 0 and len(selection == 0):
            #     return result1
            
            # result2 = self.bruteForce(actions.copy(), selection)
            # if result1 !=None and result1 != result2:
            #     print("result1", result1)
            #     print("result2", result2)
            #     if result1[0] == result2[0]:
            #         return result1
            #     else:
            #         return result2
        # else:
        #     cost = 0
        #     print(selection)
        #     for s in selection:
        #         cost = cost + s[1]
        #     return cost, selection

    # def bruteForce(actions, selection=[]):


    def bruteForce(self, actions, selection=[]):
        for action in actions:
            selection.append(action)
            print(','.join(map(str,selection)))
            if len(selection) == len(actions):
                if len(actions)>1:
                    actions.pop(1)
                    selection=[]
                    self.bruteForce(actions,selection)
controller = BruteForce()
# controller.bruteForce(controller.recordActions())
controller.bruteForce(actions)


# print(controller.actions)
# print (controller.combinaison(liste))

# Tant que somme des actions est inférieur à 500:
#     somme des actions
#     calcul du rendement(cost * %benefices)
#     mettre le résultat dans un tableau ordonné du meilleur au moins bon

# Créer un fichier csv pour importer les données que python doit lire et transformer en objet
 