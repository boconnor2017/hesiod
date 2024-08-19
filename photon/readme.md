# PhotonOS Quick Start
Step 1: Deploy Photon (photon-ova-4.0-ca7c9e9330.ova)
For downloads visit: https://github.com/vmware/photon/wiki/Downloading-Photon-OS 

The default password is `changeme`. For all labs, use `/usr/local/` as the working directory.
```
cd /usr/local/
```

Step 2: Download controller prep script 
```
curl https://raw.githubusercontent.com/boconnor2017/hesiod/pytorch-01/photon/_prep_photon.sh >> prep-photon.sh
```

Step 3: Download refresher script
```
curl https://raw.githubusercontent.com/boconnor2017/e2e-patterns/main/refresh-e2e-patterns.sh >> refresh-e2e-patterns.sh
```

Step 4: Run E2E lab PhotonOS prep script. (Optional: open a second terminal and watch progress with `tail -f _prep_photon.log`).
```
sh prep-photon.sh >> _prep_photon.log
```

Step 5: Refresh local repo (as needed)
```
sh refresh-e2e-patterns.sh
``` 