# Analyse_Gros_fichiers.ps1

# Chemin vers ton fichier Python (mettez ici le chemin complet de ton fichier Python)
$chemin_python = "/Users/ton_nom/chemin/vers/ton/script/analyse_fichiers.py"

# Répertoire de base à analyser (remplace par ton répertoire d'analyse)
$repertoire_de_base = "/Users/soumaya/Documents/BUT 1ère année"

# Exécute le script Python avec le répertoire de base comme argument
python3 $chemin_python $repertoire_de_base
