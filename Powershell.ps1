# Vérification de l'installation de Python
$python = Get-Command python3 -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command python -ErrorAction SilentlyContinue
}

if (-not $python) {
    Write-Host "❌ Python n'est pas installé. Veuillez l'installer avant de continuer." -ForegroundColor Red
    exit
}

# Définition du chemin du script Python (chemin relatif)
$chemin_python = Join-Path -Path $PSScriptRoot -ChildPath "main.py"

# Vérification de l'existence du fichier main.py
if (-Not (Test-Path $chemin_python)) {
    Write-Host "❌ Erreur : Le fichier main.py est introuvable à l'emplacement suivant : $chemin_python" -ForegroundColor Red
    exit
}

# Exécution du script Python
Write-Host "▶️ Lancement de main.py..." -ForegroundColor Cyan
& $python.Path "$chemin_python"

# Vérification du statut d'exécution
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Une erreur s'est produite lors de l'exécution du script Python." -ForegroundColor Red
} else {
    Write-Host "✅ Exécution terminée avec succès !" -ForegroundColor Green
}
