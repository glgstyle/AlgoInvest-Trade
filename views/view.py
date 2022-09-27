'''Base view'''


class View:
    '''AlgoInvest.'''

    def __init__(self):
        '''Define the view.'''

    def showThebestActionsCombo(resultat):
        print("Voici le combo d'actions qui a le meilleur profit :\n", resultat[0],
              "\n Pour un total de :", resultat[1],"€",
              "\n Et un profit de :", resultat[2], "€")
    
    def showTimeOfExecution(start, end):
        print("\nTemps d'éxécution :", end - start, "secondes\n")
