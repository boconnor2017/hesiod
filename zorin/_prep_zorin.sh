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
apt update
apt install git net-tools lvm2
# Install python3
apt install python3
apt install python3-pip
python3 --version
# Create drop folder
mkdir /usr/local/drop
# Clone this repository
git clone https://github.com/boconnor2017/hesiod.git /usr/local/hesiod
# Run necessary pip commands
python3 -m ensurepip
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pip setuptools
python3 -m pip install flask-restful
python3 -m pip install docker
python3 -m pip install paramiko
python3 -m pip install cryptography