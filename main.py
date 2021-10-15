#!/usr/bin/env python

import subprocess

# interface = input("interface ")
# new_mac = input("enter mac address")

interface = input("enter interface name >")
new_mac = input("enter mac address >")

subprocess.call("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+new_mac, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)

