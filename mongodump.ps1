# Fonction pour faire un dump MongoDB via mongodump
function Invoke-MongoDump {
    $username = "admin"
    $password = "secretpassword"
    $authDb = "admin"
    $dbName = "TPNoSQL"
    $outputDir = ".\dump_powershell"

    $mongodumpPath = "mongodump"  # Assure-toi que mongodump est dans le PATH

    $args = @(
        "--username", $username,
        "--password", $password,
        "--authenticationDatabase", $authDb,
        "--db", $dbName,
        "--out", $outputDir
    )

    Write-Host "🚀 Lancement de la sauvegarde MongoDB..."

    $process = Start-Process -FilePath $mongodumpPath -ArgumentList $args -NoNewWindow -Wait -PassThru -RedirectStandardOutput stdout.txt -RedirectStandardError stderr.txt

    if ($process.ExitCode -eq 0) {
        Write-Host "✅ Sauvegarde réussie dans $outputDir"
    }
    else {
        Write-Host "❌ Erreur lors de la sauvegarde :"
        Get-Content stderr.txt
    }
}

Invoke-MongoDump
