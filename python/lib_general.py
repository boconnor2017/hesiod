# Hesiod General Python Library 2024
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

def api_get(api_url):
    api_response = requests.get(api_url)
    return api_response

def api_post(api_url):
    api_response = requests.post(api_url)
    api_response.headers['Content-Type: application/json']
    return api_response

def append_text_to_file(text, file_name):
    new_file = open(file_name, "a")
    new_file.writelines(text)
    new_file.close()

def download_content_from_url_into_var(url):
    web_content = urllib.request.urlopen(url)
    return(web_content)

def download_file_from_url(url, filename):
    urllib.request.urlretrieve(url, filename)

def pause_python_for_duration(seconds):
    time.sleep(seconds)

def populate_var_from_file(file_name):
    with open(file_name) as file:
        file_txt = file.read()
        return file_txt

def run_local_shell_cmd(cmd):
    err = subprocess.run(cmd, capture_output=True)
    return err

