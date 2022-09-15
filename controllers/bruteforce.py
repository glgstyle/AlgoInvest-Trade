'''The brute brute force controller'''

from models.action import Action
import csv

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

    
# Tant que somme des actions est inférieur à 500:
#     somme des actions
#     calcul du rendement(cost * %benefices)
#     mettre le résultat dans un tableau ordonné du meilleur au moins bon

# Créer un fichier csv pour importer les données que python doit lire et transformer en objet
