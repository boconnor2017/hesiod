# Run this on all Salt Photon machines
systemctl enable salt-master && systemctl start salt-master
systemctl enable salt-minion && systemctl start salt-minion
systemctl enable salt-syndic && systemctl start salt-syndic
systemctl enable salt-api && systemctl start salt-api