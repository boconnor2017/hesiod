#!/bin/sh

# Download script from GitHub
curl https://raw.githubusercontent.com/lamw/vmware-scripts/refs/heads/master/powershell/VMKeystrokes.ps1 >> Set-VMKeystrokes.ps1

# Establish script as a function
. .\Set-VMKeystrokes.ps1