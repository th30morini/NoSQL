function Invoke-MongoRestore {
    $username = "admin"
    $password = "secretpassword"
    $authDb = "admin"
    $dbName = "TPNoSQL"
    $dumpDir = ".\dump_powershell\TPNoSQL"  # dossier contenant les fichiers dump BSON

    $mongorestorePath = "mongorestore"  # Assure-toi que mongorestore est dans le PATH

    $args = @(
        "--username", $username,
        "--password", $password,
        "--authenticationDatabase", $authDb,
        "--db", $dbName,
        "--drop",                   # Supprime la base avant de restaurer
        $dumpDir
    )

    Write-Host "🚀 Lancement de la restauration MongoDB..."

    $process = Start-Process -FilePath $mongorestorePath -ArgumentList $args -NoNewWindow -Wait -PassThru -RedirectStandardOutput stdout_restore.txt -RedirectStandardError stderr_restore.txt

    if ($process.ExitCode -eq 0) {
        Write-Host "✅ Restauration réussie depuis $dumpDir"
    }
    else {
        Write-Host "❌ Erreur lors de la restauration :"
        Get-Content stderr_restore.txt
    }
}

Invoke-MongoRestore
