# About: The script below configures the ESXi host in preparation for VCF bringup. 
# Date: September 2024

#Required Input variables
$vmhosts="<IP of management cluster host 1>","<IP of management cluster host 2>","<IP of management cluster host 3>","<IP of management cluster host 4>"
$ntp="<IP or FQDN of NTP server>"
$user="root"
$pwd="<ESXi Host Password>"

#Optional Input variables
$vSwitch="vSwitch0"
$pg="VM Network"
$vlanId="0"
$fwExceptions="NTP Client"

# # # # # CAUTION: TRY NOT TO CHANGE ANYTHING BEYOND THIS POINT # # # # # # #

#Ignore https cert errors
Set-PowerCLIConfiguration -InvalidCertificateAction ignore

#Connect to hosts and open a session.
$vmhosts | Foreach-Object {Connect-VIserver $_ -User $user -Password $pwd}

#Open NTP firewall ports on ESXi host(s)
Foreach ($svc in $fwExceptions){
	Get-VMHostFirewallException | where {$_.name -eq $svc} | Set-VMhostFirewallException -Enabled:$true
	}

#Set NTP service and turn the policy on. Then start NTP
Add-VMHostNtpServer -NtpServer $ntp -ErrorAction "SilentlyContinue"
Get-VMHostService | Where-Object {$_.key -eq "ntpd"} | Set-VMHostService -policy "on" | Start-VMHostService

#Set the SSH service and turn the policy on.
Get-VMHostService | Where-Object {$_.key -eq "TSM-SSH"} | Set-VMHostService -policy "on" -Confirm:$false | Restart-VMHostService -Confirm:$false
	
#Set vSwitch MTU size to 9000
$vss = Get-VirtualSwitch -Name $vSwitch -VMHost (Get-VMHost)
Set-VirtualSwitch $vss -Mtu 9000 -Confirm:$false  -ErrorAction "SilentlyContinue"

#Set VM Network port group VLAN ID to same as Management
Get-VMHost | Get-VirtualPortGroup -Name $pg | Set-VirtualPortGroup -VLanId $vlanId

Disconnect-Viserver "*" -Confirm:$false