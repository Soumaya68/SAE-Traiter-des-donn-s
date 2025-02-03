import subprocess
import json
import sys
import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor
from Creation_Onglets import Onglets
from Creation_Camembert import Camembert
from Creation_Legendes import Legendes
from Creation_Boutons import Boutons

NB_LEGENDES_PAR_PAGE = 25
NB_MAXI_FICHIERS = 100
FICHIER_JSON = "resultats.json"

# Exécuter analyse_fichiers.py AVANT de continuer
subprocess.run(["python3", "analyse_fichiers.py"], check=True)

def charger_fichiers_json(nom_fichier):
    """ Charge les données du fichier JSON et retourne une liste de tuples (nom, taille). """
    with open(nom_fichier, "r") as f:
        return json.load(f)

def generer_couleurs(nb):
    """ Génère une liste de couleurs aléatoires en format QColor. """
    return [QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(nb)]

def creation_script_suppression():
    """ Génère un script PowerShell pour supprimer les fichiers sélectionnés. """
    fichiers_a_supprimer = []
    for legende in liste_legende:
        etats = legende.recupere_etats_cases_a_cocher()
        fichiers_a_supprimer.extend([f[0] for f, etat in zip(liste_fichiers, etats) if etat])

    if not fichiers_a_supprimer:
        print("Aucun fichier sélectionné pour la suppression.")
        return

    with open("supprimer_fichiers.ps1", "w") as f:
        f.write("Write-Output \"Script PowerShell pour supprimer des fichiers sans confirmation\"\n")
        f.write("Write-Output \"Attention : cette suppression est définitive...\"\n")
        f.write("$reponse = Read-Host \"Confirmer la suppression ? (OUI)\"\n")
        f.write("if ($reponse -eq 'OUI') {\n")
        f.write("    $confirmation = Read-Host \"Êtes-vous sûr(e) ? (OUI)\"\n")
        f.write("    if ($confirmation -eq 'OUI') {\n")
        for fichier in fichiers_a_supprimer:
            f.write(f"        Remove-Item -Path \"{fichier}\" -Force\n")
        f.write("    } else { Write-Output \"Opération annulée...\" }\n")
        f.write("} else { Write-Output \"Opération annulée...\" }\n")
    print("Script PowerShell généré : supprimer_fichiers.ps1")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Onglets()

    liste_fichiers = charger_fichiers_json(FICHIER_JSON)
    liste_couleurs = generer_couleurs(len(liste_fichiers))

    fromage = Camembert(liste_fichiers, liste_couleurs)
    fenetre.add_onglet("Camembert", fromage.dessine_camembert())

    liste_legende = []
    for num_page in range((len(liste_fichiers) // NB_LEGENDES_PAR_PAGE) + 1):
        legende = Legendes(liste_fichiers, liste_couleurs, num_page * NB_LEGENDES_PAR_PAGE, NB_LEGENDES_PAR_PAGE)
        liste_legende.append(legende)
        fenetre.add_onglet(f"Légende {num_page+1}", legende.dessine_legendes())

    ihm = Boutons("./", creation_script_suppression)
    fenetre.add_onglet("IHM", ihm.dessine_boutons())

    fenetre.show()
    sys.exit(app.exec_())

