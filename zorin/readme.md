# Zorin OS Quick Start
Step 1: Deploy Zorin (Zorin-OS-17.1-Core-64-bit-r2.iso)
For downloads visit: https://zorin.com/os/download/ 
For installation instructions visit: https://help.zorin.com/docs/getting-started/install-zorin-os/ 

*Note: when installing on vSphere select ***Linux*** as the guest os family and ***Ubuntu Linux 64-bit*** as the guest os version.*

Using a vSphere terminal, login to the desktop, open a terminal and enable ssh:
```
sudo apt update
sudo apt install openssh-server
```

The remaining steps can use ssh via PuTTY. 

Step 2: Download controller prep script 
```
curl https://raw.githubusercontent.com/boconnor2017/hesiod/main/zorin/_prep_zorin.sh >> prep-zorin.sh
```

Step 3: Download refresher script
```
curl https://raw.githubusercontent.com/boconnor2017/hesiod/main/photon/_refresh_photon.sh >> refresh-hesiod.sh
```

Step 4: Run E2E lab PhotonOS prep script. (Optional: open a second terminal and watch progress with `tail -f _prep_photon.log`).
```
sh prep-photon.sh >> _prep_photon.log
```

Step 5: Refresh local repo (as needed)
```
sh refresh-hesiod.sh
``` 

Step 6: Clone dev branch (optional)
```
curl https://raw.githubusercontent.com/boconnor2017/hesiod/main/photon/clone_dev_branch.sh >> clone_dev_branch.sh
```
```
sh clone_dev_branch.sh
```
