
## Ayoub
import pandas as pd
from hidara import lire_csv_et_afficher_types,exporter_dataframe
# Supposons que vos fonctions soient définies ici ou importées

# Test pour lire_csv_et_afficher_types
def test_lire_csv_et_afficher_types():
    types_attendus = {"colonne1": "int64", "colonne2": "float64"}  # Exemple de types attendus
    fichier_test = "test_data.csv"  # Assurez-vous que ce fichier existe avec les types appropriés
    resultats = lire_csv_et_afficher_types(fichier_test)
    assert resultats == types_attendus, "Les types des colonnes ne correspondent pas aux attentes."




# Test pour exporter_dataframe
def test_exporter_dataframe():
    df = pd.DataFrame({"colonne1": [1, 2, 3], "colonne2": [4.0, 5.5, 6.1]})
    try:
        exporter_dataframe(df)
        print("Test exporter_dataframe exécuté sans erreur.")
    except Exception as e:
        print(f"Test exporter_dataframe a échoué : {e}")


if __name__ == '__main__':
    test_lire_csv_et_afficher_types()
    print("Test lire_csv_et_afficher_types réussi.")
    test_exporter_dataframe()



## Loic
from Rounders import *
from Rotate_for_max import *

#Utilisations des test dexemple basique du site "codewars"

def test_rounders():
    print("Démarrage des tests pour Rounders")
    tests = [(15,20),(1234,1000),(1445,2000),(14,10),(99,100),(10,10)]
    for test in tests:
        result = tail_rounding(test[0])
        print(test[0],"=",test[1],":",result==test[1])
        if result!=test[1]:
            return False
    return True

def test_rotate_for_max():
    print("Démarrage des tests pour Rotate_for_max")
    tests = [(38458215,85821534),(195881031,988103115),(896219342,962193428),(69418307,94183076)]
    for test in tests:
        result = max_rot(test[0])
        print(test[0],"=",test[1],":",result==test[1])
        if result!=test[1]:
            return False
    return True

def main():
    test_rounders()
    test_rotate_for_max()

if __name__ == "__main__":
    main()

