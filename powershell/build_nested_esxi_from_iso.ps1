#!/bin/sh

# Server Input Variables
$esxi_server_ip_address = "x.x.x.x"
$esxi_server_username = "root"
$esxi_server_password = "password"
$esxi_server_datastore = "datastore1"
$path_to_iso_on_datastore = "[datastore1] ISO/VMware-ESXi-9.0.0.iso"

# VM Input Variables
$vm_name = "nested-esxi-01"
$vm_cpu = 4
$vm_memoryMB = (40*1024)
$vm_storageMB = (50*1024)
$vm_network = "VM Network"


### * * * * * * Try not to change anything below this point * * * * * * * *

#Ignore https cert errors
Set-PowerCLIConfiguration -InvalidCertificateAction ignore -Confirm:$false

#Connect to the ESXi host and open a session.
$esxi_server_ip_address | Foreach-Object {Connect-VIserver $_ -User $esxi_server_username -Password $esxi_server_password}

# Build Virtual Machine
New-VM -Name $vm_name -NumCPU $vm_cpu -MemoryMB $vm_memoryMB -DiskMB $vm_storageMB -NetworkName $vm_network -Datastore $esxi_server_datastore -DiskStorageFormat "Thin" -GuestID "otherLinux64Guest"
$nested_esxi_vm = Get-VM -Name $vm_name

# VM Config Specs: Enable CPU Hardware Virtualization Passthrough
$vm_config_spec = New-Object VMware.Vim.VirtualMachineConfigSpec
$vm_config_spec.Firmware = [VMware.Vim.GuestOsDescriptorFirmwareType]::efi
$vm_config_spec.NestedHVEnabled = $true

# VM Config Specs: Establish Boot Options
$vm_boot_options = New-Object VMware.Vim.VirtualMachineBootOptions
$vm_boot_options.EfiSecureBootEnabled = $true
$vm_config_spec.BootOptions = $vm_boot_options

# VM Config Specs: Establish Flags
$vm_flags = New-Object VMware.Vim.VirtualMachineFlagInfo
$vm_flags.VbsEnabled = $true
$vm_flags.VvtdEnabled = $true
$vm_config_spec.flags = $flags

# Reconfigure VM to specs
$nested_esxi_vm.ExtensionData.ReconfigVM($vm_config_spec)

# Create CD Drive and attach ESXi ISO
New-CDDrive -VM $nested_esxi_vm.Name
$cd_drive_specs = Get-CDDrive -VM $nested_esxi_vm
Set-CDDrive -CD $cd_drive_specs -IsoPath $path_to_iso_on_datastore -StartConnected:$true -Confirm:$false

# Add Disk for boot process
New-HardDisk -VM $nested_esxi_vm -CapacityGB 40 -Persistence persistent

# Start VM
Start-vm -vm $nested_esxi_vm.Name



