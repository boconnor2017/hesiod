#!/bin/sh

$usrname = "administrator@vsphere.local"
$passwrd = "<enter password here>"
$sddcmgr_fqdn = "<enter fqdn here>"

Request-VCFToken -fqdn $sddcmgr_fqdn -username $usrname -password $passwrd
Get-VCFHost