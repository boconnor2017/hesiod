# ESXCLI GENERAL (enable ssh from ESXi console)
esxcli esxcli command list #Returns available list of esxcli commands
esxcli hardware memory get #Sample syntax hardware.memory (namespace) get (command)
esxcli hardware #Sample syntax to find all of the namespaces

# PREPARING SECURITY REQUIREMENTS FOR RUNNING VALIDATION (PRE-CHECK)
# To resolve SSL errors, the FQDN configuration in the ESXi console must match the self-signed cert.
# Once the FQDN has been added to DNS Configuration in ESXi console, run below on the ESXi host terminal.
# Recommended: ssh from cloudbuilder
/sbin/generate-certificates
/etc/init.d/hostd restart && /etc/init.d/vpxa restart && /etc/init.d/rhttpproxy restart

# ESXI HOST CONFIGURATION VALIDATION (PRE-CHECK)
# To resolve time synch issues, NTP needs to be running and policy="Start and Stop with host"
# If the below command doesnt work, use the UI: ESXi > Manage > System > Time and Date
esxcli system ntp set --enabled=yes
