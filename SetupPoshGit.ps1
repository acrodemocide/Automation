# This should set up posh-git for powershell
# This comes from the README for posh-git on github
# https://github.com/dahlbyk/posh-git#installation

Write-Host "Setting up Execution Policy"
$executionPolicy = Get-ExecutionPolicy
Write-Host "Current execution policy is $executionPolicy"
if ($executionPolicy -eq "Restricted")
{
    Write-Host "Updating execution policy to RemoteSigned"
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Confirm
}

Write-Host "Installing posh-git"
PowerShellGet\Install-Module posh-git -Scope CurrentUser -AllowPrerelease -Force

Write-Host "Importing posh-git to current powershell session"
Import-Module posh-git

Write-Host "Adding posh git to powershell profile for all hosts"
Add-PoshGitToProfile -AllHosts