'''The brute brute force controller'''

from models.action import Action

class BruteForce:
    def __init__(self):
        '''Has a list of actions and a view'''
        self.actions = []
    
    def recordActions(self):
        liste_of_actions = [
            ["action-1", 20, 5],
            ["action-2", 30, 10],
            ["action-3", 50, 15],
            ["action-4", 70, 20],
            ["action-5", 60, 17],
            ["action-6", 80, 25],
            ["action-7", 22, 7],
            ["action-8", 26, 11],
            ["action-9", 48, 13],
            ["action-10", 34, 27],
            ["action-11", 42, 17],
            ["action-12", 110, 9],
            ["action-13", 38, 23],
            ["action-14", 14, 1],
            ["action-15", 18, 3],
            ["action-16", 8, 8],
            ["action-17", 4, 12],
            ["action-18", 10, 14],
            ["action-19", 24, 21],
            ["action-20", 114, 18],
            ]
        i = 0
        # print(liste_of_actions[0][0])
        for i in range(len(liste_of_actions)):
            # action = Action()
            liste = Action.addAction(liste_of_actions[i][0], liste_of_actions[i][1], liste_of_actions[i][2])
            # print(liste)
            self.actions.append(liste)
            i+=1
        self.findCosts(0, 500)
        return self.actions
        # print le cout de la première action
        # print(self.actions[0].cost)
        # print le cout des actions
        # print(self.actions)
# Tant que somme des actions est inférieur à 500:
#     somme des actions
#     calcul du rendement(cost * %benefices)
#     mettre le résultat dans un tableau ordonné du meilleur au moins bon

    def findCosts(self, total, budget):
        # print(self.actions)
        print(action.cost[0])
        for action in self.actions:
            pass
