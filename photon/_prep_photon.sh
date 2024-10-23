# Hesiod Photon Prep Script
# Author: Brendan O'Connor
# Date: September 2023

# The purpose of this script is to prepare a PhotonOS appliance (Linux with Docker) for development. 
# PhotonOS is the primary OS of choice for Project Hesiod. Other Operating Systems such as Windows
# CentOS, RedHat, etc are fully supported. Please note that this script will need to be edited to 
# execute properly on non-Photon operating systems (for example: yum vs apt-install or .sh vs .ps1). 
#
# Preparation includes the following:
#     1. Basic Linux Tools: git, bindutils, lvm2
#     2. Python3
#     3. A drop folder (for sftp and other binaries)
#     4. Project Hesiod repo is cloned from Git
#     5. Docker is started
#     6. resolv.conf is edited to enable public nslookup
#     7. Python modules (pip): setuptools, flask-restful, docker, paramiko, VMware Python SDK, cryptography

# Update/install basic Linux tools
yum -y update --nogpgcheck
yum -y install git bindutils lvm2 sudo powershell unzip
yum -y install https://repo.ius.io/ius-release-el$(rpm -E '%{rhel}').rpm
# Install python3
yum -y install python3
python3 --version
# Create drop folder
mkdir /usr/local/drop
# Clone this repository
git clone https://github.com/boconnor2017/hesiod.git /usr/local/hesiod
# Start Docker
systemctl start docker
#systemctl status docker
# Pause 10 seconds before running pip commands
sleep 10
# Run necessary pip commands
python3 -m ensurepip
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pip setuptools
python3 -m pip install flask-restful
python3 -m pip install docker
python3 -m pip install paramiko
python3 -m pip install cryptography
python3 -m pip install httpimport
python3 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
python3 -m pip install pandas
python3 -m pip install matplotlib
python3 -m pip install pygame
python3 -m pip install openpyxl
