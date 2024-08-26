# https://williamlam.com/2020/06/full-ova-ovf-property-support-coming-to-terraform-provider-for-vsphere.html
terraform {
  required_providers {
    vsphere = {
      source  = "hashicorp/vsphere"
      version = ">= 2.0.2"
    }
  }
  required_version = ">= 1.0.10"
}

provider "vsphere" {
  user           = "*protected email*"
  password       = "VMware1!"
  vsphere_server = "192.168.30.3"
  allow_unverified_ssl = true
}

data "vsphere_datacenter" "datacenter" {
  name = "Primp-Datacenter"
}

data "vsphere_datastore" "datastore" {
  name          = "sm-vsanDatastore"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_compute_cluster" "cluster" {
  name          = "Supermicro-Cluster"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_resource_pool" "default" {
  name          = format("%s%s", data.vsphere_compute_cluster.cluster.name, "/Resources/Workload")
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_host" "host" {
  name          = "192.168.30.5"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "network" {
  name          = "VM Network"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_folder" "folder" {
  path = "/${data.vsphere_datacenter.datacenter.name}/vm/Workloads"
}

## Remote OVF/OVA Source
data "vsphere_ovf_vm_template" "ovfRemote" {
  name              = "foo"
  disk_provisioning = "thin"
  resource_pool_id  = data.vsphere_resource_pool.default.id
  datastore_id      = data.vsphere_datastore.datastore.id
  host_system_id    = data.vsphere_host.host.id
  remote_ovf_url    = "https://download3.vmware.com/software/vmw-tools/nested-esxi/Nested_ESXi7.0u3_Appliance_Template_v1.ova"
  ovf_network_map = {
      "VM Network" : data.vsphere_network.network.id
  }
}

## Local OVF/OVA Source
data "vsphere_ovf_vm_template" "ovfLocal" {
  name              = "foo"
  disk_provisioning = "thin"
  resource_pool_id  = data.vsphere_resource_pool.default.id
  datastore_id      = data.vsphere_datastore.datastore.id
  host_system_id    = data.vsphere_host.host.id
  local_ovf_path    = "/Volumes/Storage/Software/Nested_ESXi7.0u3c_Appliance_Template_v1.ova"
  ovf_network_map = {
      "VM Network" : data.vsphere_network.network.id
  }
}

## Deployment of VM from Remote OVF
resource "vsphere_virtual_machine" "vmFromRemoteOvf" {
  name                 = "Nested-ESXi-7.0-Terraform-Deploy-1"
  folder               = trimprefix(data.vsphere_folder.folder.path, "/${data.vsphere_datacenter.datacenter.name}/vm")
  datacenter_id        = data.vsphere_datacenter.datacenter.id
  datastore_id         = data.vsphere_datastore.datastore.id
  host_system_id       = data.vsphere_host.host.id
  resource_pool_id     = data.vsphere_resource_pool.default.id
  num_cpus             = data.vsphere_ovf_vm_template.ovfRemote.num_cpus
  num_cores_per_socket = data.vsphere_ovf_vm_template.ovfRemote.num_cores_per_socket
  memory               = data.vsphere_ovf_vm_template.ovfRemote.memory
  guest_id             = data.vsphere_ovf_vm_template.ovfRemote.guest_id
  scsi_type            = data.vsphere_ovf_vm_template.ovfRemote.scsi_type
  nested_hv_enabled    = data.vsphere_ovf_vm_template.ovfRemote.nested_hv_enabled
  dynamic "network_interface" {
      for_each = data.vsphere_ovf_vm_template.ovfRemote.ovf_network_map
      content {
          network_id = network_interface.value
      }
  }
  wait_for_guest_net_timeout = 0
  wait_for_guest_ip_timeout  = 0

  ovf_deploy {
      allow_unverified_ssl_cert = false
      remote_ovf_url            = data.vsphere_ovf_vm_template.ovfRemote.remote_ovf_url
      disk_provisioning         = data.vsphere_ovf_vm_template.ovfRemote.disk_provisioning
      ovf_network_map           = data.vsphere_ovf_vm_template.ovfRemote.ovf_network_map
  }

vapp {
  properties = {
      "guestinfo.hostname" = "tf-nested-esxi-1.primp-industries.com",
      "guestinfo.ipaddress" = "192.168.30.180",
      "guestinfo.netmask" = "255.255.255.0",
      "guestinfo.gateway" = "192.168.30.1",
      "guestinfo.dns" = "192.168.30.1",
      "guestinfo.domain" = "primp-industries.com",
      "guestinfo.ntp" = "pool.ntp.org",
      "guestinfo.password" = "VMware1!23",
      "guestinfo.ssh" = "True"
      }
  }

  lifecycle {
      ignore_changes = [
      annotation,
      disk[0].io_share_count,
      disk[1].io_share_count,
      disk[2].io_share_count,
      vapp[0].properties,
      ]
  }
}

## Deployment of VM from Local OVF
resource "vsphere_virtual_machine" "vmFromLocalOvf" {
  name                 = "Nested-ESXi-7.0-Terraform-Deploy-2"
  folder               = trimprefix(data.vsphere_folder.folder.path, "/${data.vsphere_datacenter.datacenter.name}/vm")
  datacenter_id        = data.vsphere_datacenter.datacenter.id
  datastore_id         = data.vsphere_datastore.datastore.id
  host_system_id       = data.vsphere_host.host.id
  resource_pool_id     = data.vsphere_resource_pool.default.id
  num_cpus             = data.vsphere_ovf_vm_template.ovfLocal.num_cpus
  num_cores_per_socket = data.vsphere_ovf_vm_template.ovfLocal.num_cores_per_socket
  memory               = data.vsphere_ovf_vm_template.ovfLocal.memory
  guest_id             = data.vsphere_ovf_vm_template.ovfLocal.guest_id
  scsi_type            = data.vsphere_ovf_vm_template.ovfLocal.scsi_type
  nested_hv_enabled    = data.vsphere_ovf_vm_template.ovfLocal.nested_hv_enabled
  dynamic "network_interface" {
      for_each = data.vsphere_ovf_vm_template.ovfLocal.ovf_network_map
      content {
      network_id = network_interface.value
      }
  }
  wait_for_guest_net_timeout = 0
  wait_for_guest_ip_timeout  = 0

  ovf_deploy {
      allow_unverified_ssl_cert = false
      local_ovf_path            = data.vsphere_ovf_vm_template.ovfLocal.local_ovf_path
      disk_provisioning         = data.vsphere_ovf_vm_template.ovfLocal.disk_provisioning
      ovf_network_map           = data.vsphere_ovf_vm_template.ovfLocal.ovf_network_map
  }

  vapp {
      properties = {
          "guestinfo.hostname" = "tf-nested-esxi-2.primp-industries.com",
          "guestinfo.ipaddress" = "192.168.30.181",
          "guestinfo.netmask" = "255.255.255.0",
          "guestinfo.gateway" = "192.168.30.1",
          "guestinfo.dns" = "192.168.30.1",
          "guestinfo.domain" = "primp-industries.com",
          "guestinfo.ntp" = "pool.ntp.org",
          "guestinfo.password" = "VMware1!23",
          "guestinfo.ssh" = "True"
      }
  }

  lifecycle {
      ignore_changes = [
      annotation,
      disk[0].io_share_count,
      disk[1].io_share_count,
      disk[2].io_share_count,
      vapp[0].properties,
      ]
  }
}