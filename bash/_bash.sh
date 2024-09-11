# Bash Template
# Author: Brendan O'Connor 
# Date: August 2023
#
# The purpose of this program is to provide enough of a starting point 
# to write bash (sh) scrtipts without needing to do too much research
# on syntax. 

# Capture and output args from the command line
echo "You passed: $1"

# Change Subnet info on the host
# If the following were pasted into test.sh:
#    $1 = IP address
#    $2 = Subnet mask
#    $3 = Default Gateway
ifconfig eth0 $1 netmask $2
route add default gateway $3

# Terminal Messaging
wall -n "This is another test" #Broadcasts to all users
mesg #Turns on write


# Write a message to a user over CLI

# Displays available space for filesystems of a certain type 
df -BM 
df -BM -t ext4

# CLI tool for checking storage partitions
fdisk /dev/sda 
Command (m for help): p #p command lists partitions

Disk /dev/sda: 16 GiB, 17179869184 bytes, 33554432 sectors #<<< Notice "16 GiB" (Hard Disk)
Disk model: Virtual disk
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: BCD02BCE-03D6-4E10-9262-F621432E1DC7

Device     Start      End  Sectors Size Type
/dev/sda1   2048    10239     8192   4M BIOS boot
/dev/sda2  30720 33554398 33523679  16G Linux filesystem 
/dev/sda3  10240    30719    20480  10M EFI System

# FDISK single line commands
fdisk -l /dev/sda #equivalent to p command

# Rescan storage
echo 1 > /sys/class/block/sda/device/rescan

Command (m for help): p #List partitions

Disk /dev/sda: 50 GiB, 53687091200 bytes, 104857600 sectors #Notice the size has changed to 50GB
Disk model: Virtual disk
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: BCD02BCE-03D6-4E10-9262-F621432E1DC7

Device     Start      End  Sectors Size Type
/dev/sda1   2048    10239     8192   4M BIOS boot
/dev/sda2  30720 33554398 33523679  16G Linux filesystem #Remember "End" value (A)
/dev/sda3  10240    30719    20480  10M EFI System

# Resize the filesystem
fdisk /dev/sda
p #List partitions 
d #Delete partition
2 #Number 2 (sda2 Linux Filesystem)
n #New partition
2 #Number 2 (recreates sda2)
30720 #This is the start value next to sda2 from original partition
(default) #Use the default - will be something like 104857566
N #Partition 2 should contain ext4 signature, if so do not remove signature
p #List partitions - you should see new size next to Linux filesystem
q #Quit fdisk
resize2fs /dev/sda2

# Run multiple commands from one line 
(echo "this"; echo "that"; echo "the other thing")

# Create new user
useradd -r hesiod #creates a system user account (omit the -r for standard user account)
passwd hesiod #will prompt for password change

# List all users
cat /etc/passwd 

# Switch users
su - hesiod
sudo su # to switch to root

# Add user to sudoers file (gives sudo privileges)
usermod -aG sudo hesiod

# Disable ssh root login
vi /etc/ssh/sshd_config # uncomment PermitRootLogin no

# chmod
#
# There are three sets of permissions (i.e. actions that can be performed on the file or directory):
#   1. For the owner of the file
#   2. For the members of the file's group
#   3. For everyone else
#
# Use ls -l to see the permissions
root@photon-machine [ /usr/local ]# ls -l
total 92
-rw-r-----  1 root root   106 Aug 20 11:49 clone_dev_branch.sh
drwxr-x--- 10 root root  4096 Aug 20 13:09 hesiod-dev

# On each line the first character identifies the TYPE:
# - means a file
# d means a directory
#
# The next three characters show permissions for the user who owns the file (user permissions)
# The middle three characters show permissions for the members of the file's group (group permissions)
# The last three characters show permissions for everyone else (other permissions)
#
# There are three characters in each set of permissions:
# - means that a permission has not been granted
# r means read permissions have been granted
# w means write permissions have been granted
# x means execute permissions have been granted
#
# There are two names (root in the example above):
# The first name (root) refers to the owner of the file or directory
# The second name (also root) refers to the name of the group that the file or directory belong to
# In the example below, notice how the values are the same even though the user has changed:
hesiod@photon-machine [ /usr/local ]$ ls -l
total 92
-rw-r-----  1 root root   106 Aug 20 11:49 clone_dev_branch.sh
drwxr-x--- 10 root root  4096 Aug 20 13:09 hesiod-dev

# See the sessions/users that are using the OS
hesiod@photon-machine [ /usr/local/hesiod-dev ]$ who
hesiod   pts/0        2024-08-23 11:58 (172.16.0.4)
hesiod   pts/1        2024-08-23 17:52 (172.16.0.4)

# Kick a user out of the OS
sudo pkill -HUP -u hesiod

# Lists active daemons running on the OS
systemctl --type=service --state=running

# List ports that are listening
netstat -tunlp

# Reboots and shutdowns
shutdown -r #Reboot
shutdown -r 10:00 #Reboot at 10am
shutdown -r +5 #Reboot 5min from now
shutdown -r now #Shut down immediately

# SFTP
sftp remote_username@server_ip_or_hostname

# Makes executable file available everywhere (ovftool example below)
ln -s /usr/local/ovftool/./ovftool /usr/bin/ovftool