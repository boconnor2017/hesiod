# Hesiod JSON Python Library 2024
# Author: Brendan O'Connor
# Date: August 2024
# Version: 1.0

"""
Syntax for this library:

Option 1: use this if you need to save a local copy of the json file.
Option 2: use this if you want to return the contents of a json source. 

OPTION 1 FLOW:
Step 1: the JSON needs to be downloaded into a file.
Step 2: the JSON needs to be populated into a variable.
Step 3: the JSON needs to be converted into a python object. 
Step 4: parse the data as needed using the python object. 

OPTION 2 FLOW:
Step 1: the JSON needs to be downloaded directly into a variable.
Step 2: the JSON needs to be converted into a python object.
Step 3: parse the data as needed using the python object.

OPTION 1 SAMPLE:

import lib_json as libjson 
import os

url = "https://raw.githubusercontent.com/boconnor2017/e2e-patterns/main/json/vcf-5-bringup-template.json"
json_filename = "sample_json.json"
json_file = libjson.download_json_file_from_url(url, json_filename)
json_stringvar = libjson.populate_var_from_json_file(os.getcwd(), json_filename)
json_pyvar = libjson.load_json_variable(json_stringvar)
print("DNS Servers: "+json_pyvar["dnsSpec"]["nameserver"]+", "+json_pyvar["dnsSpec"]["secondaryNameserver"])

OPTION 2 SAMPLE:

import lib_json as libjson 
import os

url = "https://raw.githubusercontent.com/boconnor2017/e2e-patterns/main/json/vcf-5-bringup-template.json"
json_stringvar = libjson.download_json_to_var_from_url(url)
json_pyvar = libjson.load_json_variable(json_stringvar)
print("DNS Servers: "+json_pyvar["dnsSpec"]["nameserver"]+", "+json_pyvar["dnsSpec"]["secondaryNameserver"])

PARSING THE OUTPUT:

The variable json_pyvar is a python object. 
Use the structure of the json file to produce the output. 
For example, in the sample above the json looks as follows:
{
    ...
    "dnsSpec" : {
      "subdomain" : "vrack.vsphere.local",
      "domain" : "vsphere.local",
      "nameserver" : "10.0.0.250",
      "secondaryNameserver" : "10.0.0.250"
    },
    ...
}

and produces the following output:
DNS Servers: 10.0.0.250, 10.0.0.250

"""

# Base imports
import os
import shutil
import json 
import urllib 

# Hesiod Library imports
# import lib_general as libgen

# Downloads json as a file
def download_json_file_from_url(url, json_filename):
    # Syntax url: "https://domain.com/foo/bar/something.json"
    # Syntax json_filename: "what_I_want_to_call_it.json"
    urllib.request.urlretrieve(url, json_filename)

def download_json_to_var_from_url(url):
    # Syntax url: "https://domain.com/foo/bar/something.json"
    json_web = urllib.request.urlopen(url)
    # Converts the raw binary into a string
    json_binvar = json_web.read()
    json_stringvar = json_binvar.decode("utf-8")
    return json_stringvar

# Dump converts a JSON python object to string
def dump_json(json_python_obj):
    json_stringvar = json.dumps(json_python_obj)
    return json_stringvar

# Dump converts a JSON python object and writes it to JSON file
def dump_json_to_file(json_python_obj, json_filename):
    json_file = open(json_filename, "w")
    json_dump = json.dump(json_python_obj, json_file, indent = 6)

# Returns the keys from a JSON python object
def get_keys_from_json(json_python_obj):
    json_keys = []
    for key, value in json_python_obj.items():
        json_keys.append(key)
    return json_keys

# Loading converts a JSON string to a python object
def load_json_variable(json_stringvar):
    json_python_obj = json.loads(json_stringvar)
    return json_python_obj

# Populates variable from contents of JSON file
def populate_var_from_json_file(json_dir, json_filename):
    # Syntax json_dir: "/foo/bar"
    # Syntax json_filename: "something.json"
    # Syntax json_file_full: "/foo/bar/something.json"
    json_file_full = json_dir+"/"+json_filename
    # Creates variable vcf_json_raw with contents from json file
    #json_raw = libgen.populate_var_from_file(json_file_full)
    with open(json_file_full) as file:
        json_stringvar = file.read()
        return json_stringvar
