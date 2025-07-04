#!/bin/sh

# Server Input Variables
$vmhosts="x.x.x.x", "x.x.x.x", "x.x.x.x", "x.x.x.x"
$ntp="pool.ntp.org"
$esxi_user="root"
$esxi_pwd="password"
$vSwitch="vSwitch0" 
$pg="VM Network"
$vlanId="0" 
$fwExceptions="NTP Client"

# Main
Import-Module VMware.VimAutomation.Core
Set-PowerCLIConfiguration -InvalidCertificateAction ignore -Confirm:$false
$vmhosts | Foreach-Object {Connect-VIserver $_ -User $esxi_user -Password $esxi_pwd}
$vmhosts | Foreach-Object {Get-VMHost -Name $_ | Set-VMHost -State Connected}

Add-VMHostNtpServer -NtpServer $ntp -ErrorAction "SilentlyContinue"
Get-VMHostService | Where-Object {$_.key -eq "ntpd"} | Set-VMHostService -policy "on" -Confirm:$false | Start-VMHostService -Confirm:$false 
Get-VMHostService | Where-Object {$_.key -eq "TSM-SSH"} | Set-VMHostService -policy "on" -Confirm:$false | Restart-VMHostService -Confirm:$false
$vss = Get-VirtualSwitch -Name $vSwitch -VMHost (Get-VMHost)
Set-VirtualSwitch $vss -Mtu 9000 -Confirm:$false  -ErrorAction "SilentlyContinue"
Get-VMHost | Get-VirtualPortGroup -Name $pg | Set-VirtualPortGroup -VLanId $vlanId

Foreach ($svc in $fwExceptions){
    Get-VMHostFirewallException | where {$_.name -eq $svc} | Set-VMhostFirewallException -Enabled:$true
	}
