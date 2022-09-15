# Trouver un algo qui va tester toutes les combinaisons possibles (avec les actions)
# Comparer les résultats pour trouver la combinaison qui va avoir le plus de bénéfices(sortir la meilleure)

# liste [actions]
liste = ["A", "B", "C", "D"]

i = 0
while i < len(liste):
    print("achète", liste[i])
    j = i + 1 
    while j < len(liste):
        print("achète" ,liste[i], liste[j])
        k = j + 1
        while k < len(liste):
            print("achète" ,liste[i], liste[j], liste[k])
            # l = k + 1
            # while l < len(liste):
            #      print("achète" ,liste[i], liste[j], liste[k], liste[l])
            k = k + 1
        j = j + 1
    i = i + 1
    