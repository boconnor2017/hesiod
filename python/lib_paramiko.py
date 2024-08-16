# Hesiod Paramiko Python Library 2024
# Author: Brendan O'Connor
# Date: January 2024
# Version: 3.0

import requests
import urllib3
import urllib
import shutil
import time
import json
import os
import docker 
import paramiko
import docker
import subprocess
import sys
from datetime import datetime

def paramiko_delete_file_from_remote_photon_vm(ip, un, pw, filepath, filename):
    # filepath format: /foo/bar/
    # filename format: somefile.xyz
    cmd = "rm "+filepath+filename
    paramiko_send_command_over_ssh(cmd, ip, un, pw)

def paramiko_download_file_to_remote_photon_vm(ip, un, pw, url, filepath, filename):
    # filepath format: /foo/bar/
    # filename format: somefile.xyz
    cmd = "curl "+url+" >> "+filepath+filename
    paramiko_send_command_over_ssh(cmd, ip, un, pw)

def paramiko_run_sh_on_remote_photon_vm(ip, un, pw, entrypoint, shscript):
    # entrypoint format: /foo/bar/
    # shscript format: shfile.sh
    cmd = "sh "+entrypoint+shscript
    paramiko_send_command_over_ssh(cmd, ip, un, pw)

def paramiko_move_file_to_remote_photon_vm(ip, un, pw, file_as_var, filepath, filename):
    # file_as_var: read contents of file into a variable
    # filepath format: /foo/bar/
    # filename format: somefile.xyz
    cmd = "echo \'"+file_as_var+"\' >> "+filepath+filename
    paramiko_send_command_over_ssh(cmd, ip, un, pw)

def paramiko_send_command_over_ssh(cmd, ip, un, pw):
    pclient = paramiko.SSHClient()
    pclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pclient.connect(hostname=ip, username=un, password=pw)
    stdin, stdout, stderr = pclient.exec_command(cmd, timeout=None)
    stdout=stdout.readlines()
    pclient.close()
    return stdout