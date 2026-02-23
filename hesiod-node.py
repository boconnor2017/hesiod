# Import Hesiod libraries
from python import lib_general as libgen
from python import lib_json as libjson
from python import lib_logs_and_headers as liblog 
from python import lib_paramiko as libpko 
from lib import run_scripts as runscript

# Import Standard Python libraries
import os
import sys
import subprocess

# Import json configuration parameters
env_json_str = libjson.populate_var_from_json_file("json", "lab_environment.json")
env_json_py = libjson.load_json_variable(env_json_str)
this_script_name = os.path.basename(__file__)
logfile_name = env_json_py["logs"][this_script_name]

# Hesiod Header and Log init
liblog.hesiod_print_header()
liblog.hesiod_log_header(logfile_name)
err = "Successfully imported Hesiod python libraries."
liblog.write_to_logs(err, logfile_name)
err = "Succesfully initialized logs to "+logfile_name
liblog.write_to_logs(err, logfile_name)
err = ""
liblog.write_to_logs(err, logfile_name)

# Local Functions
def _main_(args):
    err = "Retreiving user inputs:"
    liblog.write_to_logs(err, logfile_name)
    arg_len = len(args)
    err = "    "+str(arg_len)+" args passed."
    liblog.write_to_logs(err, logfile_name)

    err = "Initializing default user options."
    liblog.write_to_logs(err, logfile_name)
    user_options = ['n', 'n', 'n']

    err = "Matching user inputs to hesiod menu."
    liblog.write_to_logs(err, logfile_name)
    if '--help' in args:
        err = "    --help found. Initiating HELP menu."
        liblog.write_to_logs(err, logfile_name)
        help_menu()
        sys.exit() 
    if '-build' in args:
        err = "    -build found. Initiating hesiod node deployment."
        liblog.write_to_logs(err, logfile_name)
        build_hesiod_node_v2(env_json_py)
        sys.exit()

def build_hesiod_node_v2(env_json_py):
    i=0
    while i < len(env_json_py["hesiod_nodes"]):
        ovftool_cmd = []
        ovftool_cmd.append("ovftool")
        ovftool_cmd.append("--noSSLVerify")
        ovftool_cmd.append("--acceptAllEulas")
        ovftool_cmd.append("--name="+env_json_py["hesiod_nodes"][i]["vm_name"])
        ovftool_cmd.append("--datastore="+env_json_py["physical_server"]["deploy_vms_to_this_datastore"])
        ovftool_cmd.append("--network=\""+env_json_py["physical_server"]["deploy_vms_to_this_network"]+"\"")
        ovftool_cmd.append(env_json_py["photon_specs"])
        ovftool_cmd.append("vi://"+env_json_py["physical_server"]["username"]+":\""+env_json_py["physical_server"]["password"]+"\"@"+env_json_py["physical_server"]["ip_address"]+"")
        cmdcheck = ""
        c=0
        while c < len(ovftool_cmd):
            cmdcheck = cmdcheck+ovftool_cmd[c]+" "
            c=c+1
        print("Command Check for Hesiod Node"+str(i+1)+": "+cmdcheck)
        runcmd = os.system(cmdcheck)
        print("Creating powershell scripts.")
        runscript.pcli_create_script("Set-VMKeystrokes")
        runscript.pcli_create_script("pcli_init_hesiod_node")
        print("Injecting powershell variables.")
        runscript.pcli_inject_script_with_var("ID:SIV-001", env_json_py["physical_server"]["ip_address"], "pcli_init_hesiod_node.ps1")
        runscript.pcli_inject_script_with_var("ID:SIV-002", env_json_py["physical_server"]["username"], "pcli_init_hesiod_node.ps1")
        runscript.pcli_inject_script_with_var("ID:SIV-003", env_json_py["physical_server"]["password"], "pcli_init_hesiod_node.ps1")
        runscript.pcli_inject_script_with_var("ID:VIV-001", env_json_py["hesiod_nodes"][i]["vm_name"], "pcli_init_hesiod_node.ps1")
        runscript.pcli_inject_script_with_var("ID:CRED-001", env_json_py["hesiod_nodes"][i]["password"], "pcli_init_hesiod_node.ps1")
        runscript.pcli_inject_script_with_var("ID:NET-001", "eth0", "pcli_init_hesiod_node.ps1")
        runscript.pcli_inject_script_with_var("ID:NET-002", env_json_py["hesiod_nodes"][i]["ip_address"], "pcli_init_hesiod_node.ps1")
        runscript.pcli_inject_script_with_var("ID:NET-003", "255.255.255.0", "pcli_init_hesiod_node.ps1")
        runscript.pcli_inject_script_with_var("ID:NET-004", env_json_py["hesiod_nodes"][i]["gateway"], "pcli_init_hesiod_node.ps1")
        print("Running powershell configuration script.")
        runscript.pcli_execute_script("pcli_init_hesiod_node")
        i=i+1


def help_menu():
    print("HELP MENU: hesiod-node.py [options]")
    print("Options are mandatory. You are seeing this menu because you either entered no options or an unknown option.")
    print("Enter options 1x per run, do not add all parameters at once!")
    print("--help option to see this menu.")
    print("-build to deploy Hesiod Nodes. Note: the Hesiod Nodes will be configured based on the parameters in json/lab_environment.json file")
    print("")
    print("")

def setup_ovftool():
    cmd = []
    cmd = ["mv", "ovftool/", "ovftool_old/"]
    err = subprocess.run(cmd, capture_output=True)
    cmd = []
    cmd = ["mkdir", "ovftool"]
    err = subprocess.run(cmd, capture_output=True)
    cmd = []
    cmd = ["mv", "ovftool_old/VMware-ovftool-4.6.3-24031167-lin.x86_64.zip", "ovftool/"]
    err = subprocess.run(cmd, capture_output=True)
    cmd = []
    cmd = ["rm", "-r", "ovftool_old/"]
    err = subprocess.run(cmd, capture_output=True)
    cmd = []
    cmd = ["unzip", "/usr/local/hesiod/ovftool/VMware-ovftool*"]
    err = subprocess.run(cmd, capture_output=True)
    cmd = []
    cmd = ["rm", "/usr/bin/ovftool"]
    err = subprocess.run(cmd, capture_output=True)
    cmd = []
    cmd = ["ln", "-s", "/usr/local/hesiod/ovftool/./ovftool", "/usr/bin/ovftool"]
    err = subprocess.run(cmd, capture_output=True)
    return

_main_(sys.argv)