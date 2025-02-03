# Vérifie si Python est installé
$python = Get-Command python3 -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Output "❌ Python3 n'est pas installé. Veuillez l'installer avant de continuer."
    exit
}

# Définir le chemin relatif du script Python
$chemin_python = "$PSScriptRoot\main.py"

# Vérifie si le fichier existe
if (-Not (Test-Path $chemin_python)) {
    Write-Output "❌ Erreur : Le fichier main.py est introuvable !"
    exit
}

# Exécute le script Python
Write-Output "▶️ Lancement de main.py..."
python3 "$chemin_python"

# Vérifie si l'exécution a échoué
if ($LASTEXITCODE -ne 0) {
    Write-Output "❌ Une erreur s'est produite lors de l'exécution du script Python."
} else {
    Write-Output "✅ Exécution terminée avec succès !"
}
