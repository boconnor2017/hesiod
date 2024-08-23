# Run this on Salt Minion Photon Machine
# Input parameter is the ip address of the master
echo "Registering Salt Minion to $1"
rm /etc/salt/minion
curl https://raw.githubusercontent.com/boconnor2017/hesiod/main/saltstack/salt_minion_config >> /etc/salt/minion