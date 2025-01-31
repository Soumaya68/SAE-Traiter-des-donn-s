from pathlib import Path

def lister_fichiers(repertoire_de_base):
    fichiers = []  # Liste qui stockera les fichiers et leur taille

    # On parcourt récursivement tous les fichiers du répertoire
    for fichier in Path(repertoire_de_base).rglob('*'):
        if fichier.is_file():  # Vérifier qu'il s'agit bien d'un fichier (et non d'un dossier)
            fichiers.append([str(fichier), fichier.stat().st_size])  # Ajouter le chemin et la taille

    # Trier les fichiers par taille décroissante
    fichiers_tries = sorted(fichiers, key=lambda x: x[1], reverse=True)

    # Sélectionner les 10 plus gros fichiers (par exemple)
    fichiers_plus_grands = fichiers_tries[:10]

    return fichiers_plus_grands  # Retourner les fichiers triés

# Test
repertoire_test = "/Users/soumaya/Documents/BUT 1ère année"
print(lister_fichiers(repertoire_test))
