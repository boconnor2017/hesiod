# Getting Started with PowerCLI on Photon
```
cd /usr/local/
```

To install PowerCli via Docker:
```
docker pull vmware/powerclicore
```
To install PowerCLI directly on the OS:
```
pwsh
```
```
Install-Module VMware.PowerCLI
```

## Syntax for using PowerCLI container (Docker)
To run PowerCLI interactively
```
docker run --rm -it vmware/powerclicore
```

To run a script
```
docker run --rm --entrypoint="/usr/bin/pwsh" -v ${PWD}:/tmp vmware/powerclicore /tmp/my_pcli_script.ps1
```
*Note: all PowerCLI scripts need to start with the following header*
```
#!/bin/sh
```
*otherwise Docker will throw a `exec format error` message.*

## Syntax for using PowerCLI on OS
To run PowerCLI interactively
```
pwsh
```

To run a script
```
pwsh /foo/bar/my_pcli_script.ps1
```
*Note: all PowerCLI scripts need to start with the following header*
```
#!/bin/sh
```

## Using PowerVCF 
After installing PowerCLI, run the following commands to get started with PowerVCF.
```
pwsh
```
```
Set-PSRepository -Name PSGallery -InstallationPolicy Trusted
```
```
Install-Module -Name VMware.PowerCLI -MinimumVersion 12.3.0 -Repository PSGallery
```
```
Install-Module -Name PowerVCF -Repository PSGallery
```

To begin interacting with your VCF environment, run the following command to obtain a security token.
```
Request-VCFToken -fqdn <SDDC Manager FQDN> -username administrator@vsphere.local -password <password>
```

