$ProgressPreference = 'SilentlyContinue'
$downloadDir = "$env:USERPROFILE\Downloads"
$zipFile = "$downloadDir\lockstep_arcade_0.1.0.zip"
$extractDir = "$downloadDir\lockstep_arcade_0.1.0"

Write-Host "Downloading Lockstep Arcade 0.1.0..."
Invoke-WebRequest -Uri "https://locksteparcade.com/lockstep_arcade_0.1.0.zip" -OutFile $zipFile

Write-Host "Extracting..."
Expand-Archive -Path $zipFile -DestinationPath $extractDir -Force

Write-Host "Cleaning up..."
Remove-Item $zipFile

Write-Host "Opening folder..."
Start-Process explorer.exe $extractDir

Write-Host "Done! Run LockstepArcade.exe to play."
