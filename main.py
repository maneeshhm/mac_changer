#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    Parse = optparse.OptionParser()
    Parse.add_option("-i", "--interface", dest="interface", help="interface to change its Mac address")
    Parse.add_option("-m", "--mac", dest="new_mac", help="Enter the new mac address")
    (options,arguments)  = Parse.parse_args()
    if not options.interface:
        Parse.error("[-] please specify an interface , for more informations --help ")
    elif not options.new_mac:
        Parse.error("[-] please specify an mac address, for more informations --help")
    return options


def change_mac(interface,new_mac):
    print("[+]changing mac for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if not mac_address_search_result:
        return "mac address couldn't find"
    else:
        return mac_address_search_result.group(0)

options = get_arguments()
current_mac = get_current_mac(options.interface)
print ("current mac address is " +current_mac)

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print ("mac address change to " + options.new_mac);
else:
    print("mac address didn't change")
