# PowerShell Template
# Author: Brendan O'Connor 
# Date: August 2023
#
# The purpose of this program is to provide enough of a starting point 
# to write powershell scrtipts without needing to do too much research
# on syntax. 
#
# To run this script, use the following in the command line:
#   .\_template.ps1 "Enter something interesting"

# Capture input from command line 
param(
[string]$a
)

# Send output to command line
Write-Host $a

# Parse a string into an array 
$b = $a.Split(" ") 
$d = 0

# Loop through the array
foreach($c in $b){
    Write-Host [$d] $c 
    $d= $d+1
}

# If then statement
if ($a -ne ""){
    Write-Host "Not blank"
}

if ($a -eq ""){
    Write-Host "Blank"
}

if($d -le 10){
    Write-Host "Number of words is less than or equal to 10"
}

if ($d -ge 5){
    Write-Host "Number of words is greater than or equal to 5"
}

# Functions
Function E {
[cmdletbinding()]
    Param (
       [String]$f, [Decimal]$g, [Decimal]$h
    )
    $i = $g+$h
    $j = $i.ToString()
    Return $f+$j
}

$k = E -f "Simple Calculator: 5+6= " -g 5 -h 6
Write-Host $k

# Parse a string by character 
$l = $k.ToCharArray()

foreach ($m in $l){
    Write-Host $m
} 

# tail -f equivalent in PowerShell
# -Tail 30 >> show last 30 lines 
# -Wait >> waits for new lines to be created
Get-Content filename -Tail 30 -Wait

# Run ESXCLI commands through PowerCLI
$esxcli = Get-EsxCli -V2