# -*- coding: utf-8 -*-
import os
import re

os.system("mkdir /tmp/HostLanUsers")
os.system("ifconfig | grep UP > /tmp/HostLanUsers/devices.temp")

devices = open("../devices.temp", 'r')
devices_string = ""
for device in devices:
    devices_string += device

devices = re.findall("(.+:\s)", devices_string)
clean_devices = []
for item in devices:
    clean_devices.append(item.split(":")[0])

for device in clean_devices:
    os.system("sudo arp-scan --interface={0} --localnet >> /tmp/HostLanUsers/scan_id.temp".format(device))

file_ips = open('/tmp/HostLanUsers/scan_id.temp', "r")
ip_string = ""
for ip in file_ips:
    ip_string += ip

ips = re.findall("([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", ip_string)

for ip in ips:
    os.system("sudo nmap -T4 -A -v -O -p 15-10000 {0} > /tmp/HostLanUsers/{0}.ip_scan".format(ip))

    host_fil = open("/tmp/HostLanUsers/{0}.ip_scan".format(ip), "r")
    host_string = ""
    for host_line in host_fil:
        host_string += host_line

    ports_open = re.findall("(\d{2,4}\/.{2,4}\s)(.*\s(\|.*\s?)+)", host_string)
    print ("--------------------------------------------")
    print (" Find Host {}".format(ip))
    print ("{}".format(ports_open))
    print ("--------------------------------------------")
