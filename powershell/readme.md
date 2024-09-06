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