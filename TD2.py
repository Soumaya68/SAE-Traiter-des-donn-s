import csv

# Liste des étudiants
etudiants = [
    {"ID": 1, "Nom": "Schmitt", "Prenom": "Albert", "Note": 9},
    {"ID": 2, "Nom": "Al-Hakim", "Prenom": "Yasmine", "Note": 17},
    {"ID": 3, "Nom": "Tran", "Prenom": "Sebastien", "Note": 12},
    {"ID": 4, "Nom": "Meyer", "Prenom": "Claire", "Note": 16},
    {"ID": 5, "Nom": "Kobayashi", "Prenom": "Kaito", "Note": 11}
]

# 1. Création du fichier donnees.csv avec les données brutes
with open("donnees.csv", mode="w", newline="", encoding="utf-8") as fichier_donnees:
    champs = ["ID", "Nom", "Prenom", "Note"]
    writer = csv.DictWriter(fichier_donnees, fieldnames=champs)
    writer.writeheader()
    writer.writerows(etudiants)


# 2. Création du fichier resultats.csv avec le champ Résultat (Admis/Refusé)
with open("resultats.csv", mode="w", newline="", encoding="utf-8") as fichier_resultats:
    champs_resultats = ["Nom", "Prenom", "Resultat"]
    writer = csv.DictWriter(fichier_resultats, fieldnames=champs_resultats)
    writer.writeheader()

    for etudiant in etudiants:
        resultat = "Admis" if etudiant["Note"] >= 10 else "Refusé"
        writer.writerow({"Nom": etudiant["Nom"], "Prenom": etudiant["Prenom"], "Resultat": resultat})


# 3. Lecture du fichier donnees.csv et conversion en liste de listes
donnees_liste = []
with open("donnees.csv", mode="r", encoding="utf-8") as fichier_lu:
    reader = csv.reader(fichier_lu)
    header = next(reader)  # Lire l'en-tête et l'ignorer
    for row in reader:
        donnees_liste.append([int(row[0]), row[1], row[2], int(row[3])])

# Affichage des données lues
print(donnees_liste)
