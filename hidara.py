import pandas as pd
from datetime import datetime

def exporter_dataframe(df):
    # Vérifier si le DataFrame est vide (aucune ligne) ou pas
    if df.empty:
        print("Le DataFrame est vide. Aucun fichier n'a été créé.")
        return

    # Générer le nom du fichier basé sur la date et l'heure actuelles pour éviter les doublons
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    fichier_sortie = f'dataframe_export_{timestamp}.csv'
    
    # Exporter le DataFrame en fichier CSV
    df.to_csv(fichier_sortie, index=False)
    print(f"Le DataFrame a été exporté avec succès vers {fichier_sortie}.")

def lire_csv_et_afficher_types(fichier_csv):
    # Lire le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(fichier_csv)
    
    # Initialiser un dictionnaire pour stocker les types des colonnes non vides
    types_colonnes_non_vides = {}
    
    # Itérer sur chaque colonne pour vérifier si elle n'est pas vide et obtenir son type
    for colonne in df.columns:
        if df[colonne].dropna().empty:
            # Si la colonne est vide après avoir supprimé les NA, ne rien faire
            pass
        else:
            # Si la colonne n'est pas vide, stocker son nom et son type
            types_colonnes_non_vides[colonne] = df[colonne].dtype
    
    return types_colonnes_non_vides