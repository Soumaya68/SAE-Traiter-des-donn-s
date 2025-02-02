import pathlib
import json
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

def obtenir_fichiers(repertoire, taille_min, nb_max=100):
    """ Récupère, trie et filtre les fichiers du répertoire donné """
    taille_min = taille_min * 1024 * 1024  # Conversion Mo → octets
    fichiers = [(str(f), f.stat().st_size) for f in pathlib.Path(repertoire).rglob('*') if f.is_file()]
    return sorted([f for f in fichiers if f[1] > taille_min], key=lambda x: x[1], reverse=True)[:nb_max]

def sauvegarder_json(data, fichier):
    """ Sauvegarde les données dans un fichier JSON """
    with open(fichier, 'w') as f:
        json.dump(data, f, indent=4)

def choisir_repertoire():
    """ Ouvre une boîte de dialogue pour choisir un répertoire """
    app = QApplication(sys.argv)
    return QFileDialog.getExistingDirectory(None, "Sélectionner un répertoire")

def main():
    """ Fonction principale """
    if len(sys.argv) > 2:
        repertoire = sys.argv[1]
        taille_min = float(sys.argv[2])
    else:
        repertoire = choisir_repertoire()
        taille_min = float(input("Entrez la taille minimale des fichiers à inclure (en Mo) : "))

    if not repertoire:
        print("Aucun répertoire sélectionné, arrêt du script.")
        return

    fichiers = obtenir_fichiers(repertoire, taille_min)
    sauvegarder_json(fichiers, 'resultats.json')

    print("Le fichier JSON a été sauvegardé sous 'resultats.json'")

if __name__ == "__main__":
    main()
