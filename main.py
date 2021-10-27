#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    Parse = optparse.OptionParser()
    Parse.add_option("-i", "--interface", dest="interface", help="interface to change its Mac address")
    Parse.add_option("-m", "--mac", dest="new_mac", help="Enter the new mac address")
    (options, arguments)  = Parse.parse_args()
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


options = get_arguments()
change_mac(options.interface, options.new_mac)

