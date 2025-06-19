#!/bin/sh

# Server Input Variables
$esxi_server_ip_address = "x.x.x.x"
$esxi_server_username = "root"
$esxi_server_password = "VMware1!"
$esxi_server_datastore = "datastore1"
$path_to_iso_on_datastore = "["+$esxi_server_datastore+"] Folder\iso_filename.iso"

# VM Input Variables
$vm_name = "vm1"
$vm_cpu = 2
$vm_memoryMB = (4*1024)
$vm_storageMB = (50*1024)
$vm_network = "VM Network"


### * * * * * * Try not to change anything below this point * * * * * * * *

#Ignore https cert errors
Set-PowerCLIConfiguration -InvalidCertificateAction ignore -Confirm:$false

#Connect to the ESXi host and open a session.
$esxi_server_ip_address | Foreach-Object {Connect-VIserver $_ -User $esxi_server_username -Password $esxi_server_password}

# Build Virtual Machine
New-VM -Name $vm_name -NumCPU $vm_cpu -MemoryMB $vm_memoryMB -DiskMB $vm_storageMB -NetworkName $vm_network

# Attach ISO
$cd = New-CDDrive -VM $vm_name -ISOPath $path_to_iso_on_datastore
Set-CDDrive -CD $cd -StartConnected:$true -Confirm:$false

# Start VM
Start-vm -vm $vm_name