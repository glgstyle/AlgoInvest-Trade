'''The brute brute force controller'''
import time
from models.action import Action
import csv
liste=[ ('a',10),('b',20),('c',10),('d',40)]
actions = [1,2,3,4, 5, 6]

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
                act = Action(action[0], action[1], action[2].replace("%", ""))
                self.actions.append(act)
            # print(self.actions)
            return self.actions

    def getActionCostList(self):
        actionsList = self.recordActions()
        actions = []
        for action in actionsList:
            actions.append((action.name, action.cost, action.profit))
        return actions

    def bruteForce(self, actions, selection=[]):
        if len(actions) > 0:
            first = actions.pop(0)
            option1 = self.bruteForce(actions.copy(), selection + [first])
            option2 = self.bruteForce(actions.copy(), selection)
            if option1 == None and option2 != None:
                return option2
            elif option2 == None and option1 != None:
                return option1
            elif option1 == None and option2 == None:
                return None
            if option1[1] > option2[1]:
                return option1
            else:
                return option2
        else:
            total = 0
            benefits = 0
            for action in selection:
                cost = int(action[1])
                rate = int(action[2])
                total = total + cost
                benefits = benefits + (cost * rate)/100
            # print("total, benefits, selection",total, benefits, selection)
            if total <= 500:
                return (total, benefits, selection)
            else:
                return None
                    
controller = BruteForce()
# start timer
start = time.time()
# print("start : ",start)
# controller.bruteForce(controller.recordActions())
resultat = controller.bruteForce(controller.getActionCostList())
# stop timer
end = time.time()
print("Temps d'éxécution :", end - start, "secondes")
print("resultat :", resultat)

# controller.bruteForce(actions)
# print(controller.actions)
# print (controller.combinaison(liste))

# Tant que somme des actions est inférieur à 500:
#     somme des actions
#     calcul du rendement(cost * %benefices)
#     mettre le résultat dans un tableau ordonné du meilleur au moins bon

# Créer un fichier csv pour importer les données que python doit lire et transformer en objet

# conditionner les 500euros le plus tot possible