# PhotonOS Quick Start
Step 1: Deploy Photon (photon-ova-X.Y-zzzzzzzzzz.ova)
For downloads visit: https://github.com/vmware/photon/wiki/Downloading-Photon-OS 

The default password is `changeme`. For all labs, use `/usr/local/` as the working directory.
```
cd /usr/local/
```

Step 2: Download controller prep script 
```
curl https://raw.githubusercontent.com/boconnor2017/hesiod/main/photon/_prep_photon.sh >> prep-photon.sh
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
