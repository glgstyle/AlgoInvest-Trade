


# <h1 align="center">AlgoInvest-Trade</h1>
</br>
<p align="center">
    <img src="https://user.oc-static.com/upload/2020/09/18/1600429119334_P6.png" 
            alt="le logo d'AlgoInvest&Trade" 
            width="250" 
            height="200"/>
</p>


AlgoInvest&Trade est un programme qui permet d'optimiser des stratégies d'investissement à l'aide d'algorithmes, afin de dégager davantage de bénéfices pour ses clients. 

# Installation :

1. Placez-vous dans le répertoire qui contiendra le projet 
  
2. Récupérer le code venant de GitHub (faire un clone) :  
    ```
    git clone https://github.com/glgstyle/AlgoInvest-Trade.git
    cd AlgoInvest&Trade
    ```
3. Créer un environnement virtuel : 

    ```python -m venv env```

    ou avec powershell:

    ```virtualenv env```

4. Activer l'environnement :  

    ```source env/bin/activate ```

    ou avec powershell:
    
    ```env\bin\activate```

5. Installer les packages :

    ```pip install -r requirements.txt```  
    ```pip freeze``` (pour vérifier que les packages se sont bien installés)

# Utilisation

- Pour démarrer le programme, exécutez simplement la commande suivante :
    ```python leNomDuFichier.py suivi du fichier csv à traiter```
- Pour valider chaque commande dans le terminal appuyez sur la touche  entrée 

## Utilisation de l'algorithme bruteForce :
- Dans le terminal écrire la ligne de commande python bruteforce.py suivi du chemin du fichier csv, exemple :  
    - Pour le dossier actions.csv:
    ```python controllers/bruteforce.py datas/actions.csv```

## Utilisation de l'algorithme optimisé :
- Dans le terminal écrire la ligne de commande python bruteforce.py suivi du chemin du fichier csv, exemple :  
    - Pour le dossier actions.csv:
    ```python controllers/optimized.py datas/actions.csv```
    - Pour le dossier dataset1_Python+P7.csv:
    ```python controllers/optimized.py datas/dataset1_Python+P7.csv```
    - Pour le dossier datas/dataset2_Python+P7.csv:
    ```python controllers/optimized.py datas/dataset2_Python+P7.csv```


