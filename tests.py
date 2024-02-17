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