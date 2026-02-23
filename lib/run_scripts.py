# Description: Runs Scripts in a Python Wrapper
# Author: Brendan O'Connor
# Date: February 2026
# Version: 1.0

# Base imports
import os
import stat 
import shutil
import urllib
import requests
import docker 
import subprocess

def delete_script_file(script_file_name):
    if os.path.exists(script_file_name):
        os.remove(script_file_name)

def pcli_create_script(pcli_script_name):
    pcli_script_str = populate_var_from_file("lib/scripts/"+pcli_script_name+".script")
    pcli_script_raw = pcli_script_str.splitlines() 
    write_script_to_script_file(pcli_script_raw, pcli_script_name+".ps1")

def pcli_execute_script(script_file_name):
    cmd = []
    cmd = ["pwsh", script_file_name+".ps1"]
    err = subprocess.run(cmd, capture_output=True)
    return err

def pcli_inject_script_with_var(searchtext, replacewithtext, filename):
    line = populate_var_from_file(filename)
    newline = line.replace(searchtext, replacewithtext)
    delete_script_file(filename)
    filename = open(filename, "a")
    for line in newline:
        filename.writelines(line)
    filename.close()

def populate_var_from_file(file_name):
    with open(file_name) as file:
        file_txt = file.read()
        return file_txt

def write_script_to_script_file(script_raw, script_file_name):
    delete_script_file(script_file_name)
    script_file_name = open(script_file_name, "a")
    for line in script_raw:
        script_file_name.writelines(line+'\n')
    script_file_name.close()