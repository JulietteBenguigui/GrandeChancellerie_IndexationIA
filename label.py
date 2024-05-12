import pandas as pd

liste_decoration = pd.read_csv("Liste_decorations.csv")
qualite = liste_decoration["nom_decoration"].tolist()

# Définition de la fonction label
def label(text):
    for i in qualite:  # Parcourir les termes de la liste des décorations
        if i.lower() in text.lower():  # Vérifier si le terme est présent dans le texte
            print(f'{i} [DEC]')  # Afficher le terme avec le label [DEC]

text = """Médaille militaire 
Numéro d'inscription 204,559
Ducharbonnier François né le 18 décem 1879à Moulin (Allier)
Décret du 29 décem 1916
Rang du 25 déc 1916
Adj. à un dépot d'éclopés.
Décédé le 
Numéro de matricule"""

label(text)
