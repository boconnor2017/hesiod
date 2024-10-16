#!/bin/sh

$usrname = "administrator@vsphere.local"
$passwrd = "VMware123!VMware123!"
$sddcmgr_fqdn = "hesvcf-vcf01.hesiod.local"

Request-VCFToken -fqdn $sddcmgr_fqdn -username $usrname -password $passwrd
Get-VCFHost