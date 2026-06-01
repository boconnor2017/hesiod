# Prerequisite: Getting Started (Hesiod Main) on Ubuntu
Step 1: Deploy an Ubuntu Server 64-bit from ISO to your ESXi host (recommended vm size: 4x16x100). Use default settings.
```
sudo apt install net-tools 
```
```
sudo apt install openssh-server -y
```

Step 2: SSH into the appliance. Recommended: `sudo -i`. For all Modules, use `/usr/local/` as the working directory.
```
cd /usr/local/
```

Step 3: Download the Install Script
```
curl https://raw.githubusercontent.com/boconnor2017/hesiod/refs/heads/main/ubuntu/build_hesiod_main_ubuntu.sh >> build_hesiod_main_ubuntu.sh
```

Step 4: Install the Hesiod Binaries and create Hesiod Main using the following command
```
sh build_hesiod_main_ubuntu.sh
```