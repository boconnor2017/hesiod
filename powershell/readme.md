# Getting Started with PowerCLI on Photon
```
cd /usr/local/
```
```
docker pull vmware/powerclicore
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