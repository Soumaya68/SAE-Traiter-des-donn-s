import pathlib
import json
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys


# Fonction pour analyser l'arborescence des fichiers
def analyser_fichiers(repertoire_de_base):
    fichiers = []
    # Utilisation de pathlib pour naviguer dans l'arborescence
    for fichier in pathlib.Path(repertoire_de_base).rglob('*'):  # rglob pour la recherche récursive
        if fichier.is_file():  # On s'assure que c'est bien un fichier
            print(f"Fichier trouvé : {fichier}")
            fichiers.append([str(fichier), fichier.stat().st_size])  # Ajouter le chemin et la taille
    return fichiers


# Fonction pour trier les fichiers par taille décroissante
def trier_fichiers(fichiers):
    return sorted(fichiers, key=lambda x: x[1], reverse=True)


# Fonction pour filtrer les fichiers selon la taille et le nombre maximum
def filtrer_fichiers(fichiers, taille_min, nb_max):
    taille_min_en_octets = taille_min * 1024 * 1024  # Conversion de Mo en octets
    fichiers_filtres = [fichier for fichier in fichiers if fichier[1] > taille_min_en_octets]
    return fichiers_filtres[:nb_max]  # On retourne les n premiers fichiers


# Fonction pour sauvegarder la liste filtrée dans un fichier JSON
def sauvegarder_json(fichiers, nom_fichier_json):
    # Remplacer les antislashs dans les chemins de fichiers sous Windows
    for fichier in fichiers:
        print(f"Fichier: {fichier[0]}, Taille: {fichier[1]}")
        fichier[0] = fichier[0].replace('\\', '\\\\')

    with open(nom_fichier_json, 'w') as f:
        json.dump(fichiers, f, indent=4)  # Sauvegarde avec une indentation pour la lisibilité
    print(f"Fichier JSON sauvegardé sous : {nom_fichier_json}")


# Fonction pour ouvrir la boîte de dialogue de sélection de répertoire
def choisir_repertoire():
    app = QApplication(sys.argv)  # Crée une application Qt
    repertoire = QFileDialog.getExistingDirectory(None, "Sélectionner un répertoire")
    return repertoire


# Fonction principale
def main():
    # Ouvrir la boîte de dialogue pour sélectionner le répertoire
    if len(sys.argv) > 1:  # Vérifie si un argument a été passé par PowerShell
        repertoire_de_base = sys.argv[1]
    else:
        repertoire_de_base = choisir_repertoire()  # Ouvre la boîte de dialogue si aucun argument

    # Vérifier si un répertoire a été sélectionné
    if not repertoire_de_base:
        print("Aucun répertoire sélectionné, le script s'arrête.")
        return

    # Analyser, trier et filtrer les fichiers
    fichiers = analyser_fichiers(repertoire_de_base)  # Analyser l'arborescence des fichiers
    fichiers_triees = trier_fichiers(fichiers)  # Trier les fichiers par taille
    fichiers_filtres = filtrer_fichiers(fichiers_triees, 10, 100)  # Filtrer pour > 10 Mo et max 100 fichiers
    sauvegarder_json(fichiers_filtres, 'resultats.json')  # Sauvegarder le résultat dans un fichier JSON


# Exécution du script
if __name__ == "__main__":
    main()

