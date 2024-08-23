# Run this on all Salt Photon machines
sudo rpm --import https://repo.saltproject.io/salt/py3/photon/4.0/x86_64/latest/SALT-PROJECT-GPG-PUBKEY-2023.pub
curl -fsSL https://repo.saltproject.io/salt/py3/photon/4.0/x86_64/latest.repo | sudo tee /etc/yum.repos.d/salt.repo

tdnf clean all