# Analyse_Gros_fichiers.ps1

# Chemin vers le fichier Python
$chemin_python = "/Users/soumaya/PycharmProjects/SAE-Traiter-des-donn-s/analyse_fichiers.py"

# Demander le répertoire à analyser
$repertoire_de_base = Read-Host "Entrez le chemin du répertoire à analyser"

# Demander la taille minimale des fichiers en Mo
$taille_min = Read-Host "Entrez la taille minimale des fichiers à inclure (en Mo)"

# Exécuter le script Python avec les arguments
python3 "$chemin_python" "$repertoire_de_base" "$taille_min"

