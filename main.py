#!/usr/bin/env python

import subprocess
import optparse

Parse = optparse.OptionParser()
Parse.add_option("-i", "--interface", dest="interface", help="interface to change its Mac address")
Parse.add_option("-m", "--mac", dest="new_mac", help="Enter the new mac address")

(options, arguments) = Parse.parse_args()

interface = options.interface
new_mac = options.new_mac

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

