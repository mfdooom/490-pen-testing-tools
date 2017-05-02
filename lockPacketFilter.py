#!/usr/bin/python

"""
NAME
    lockPacketFilter.py - Packet filtering tool

SYNOPSIS
    lockPacketFilter [-h|-help|filePath]

DESCRIPTION
    This script expedites the process of finding password interactions
    inside the communications of the Quicklock Bluetooth low energy
    padlock. 

REQUIREMENTS
    This script is intended to be run with Python2.7. It should be compatible
    with all Unix operating systems, but was most extensively tested on
    Mac OS X. 

OPTIONS
    The options are as follows:

        -h              This will display the help message.

        -help           This will display the help message.

        filePath        This is the path to the JSON file.
    
EXAMPLES
    lockPacketFilter.py -h
    lockPacketFilter.py -help
    lockPacketFilter.py Desktop/CaptureFiles/lockCapture.json

AUTHORS
    Patrick Knight
    Logan Smith
"""



import json
import sys
from pprint import pprint


def findPasswordInteraction():
    
    # Attribute that indicate the packet deals with password
    desired_handle = "0x0000002d"
    desired_serviceUUID = "65488"
    desired_uuid = "65494"

    filePath = sys.argv[1]

    with open(filePath) as data_file:
        data = json.load(data_file)

    for dataPoint in data:
        try:
            if (dataPoint["_source"]["layers"]["btatt"]["btatt.handle"] ==
                desired_handle and dataPoint["_source"]["layers"]["btatt"]["btatt.handle_tree"]["btatt.service_uuid16"]
                == desired_serviceUUID and dataPoint["_source"]["layers"]["btatt"]["btatt.handle_tree"]["btatt.uuid16"]
                == desired_uuid):
                
                btattValue = dataPoint["_source"]["layers"]["btatt"]["btatt.value"] 
                packetNumber = dataPoint["_source"]["layers"]["frame"]["frame.number"]
                btattValue = str(btattValue)
                opcode = btattValue.split(':')[0]
                oldPassword = "".join(btattValue.split(':')[1:4])
                newPassword = "".join(btattValue.split(':')[5:])


                if opcode == "01":
                    print("Password Change Captured!" +"\nPacket Number: " + packetNumber + "\nOpcode: " + opcode +  "\nOld Password: " + oldPassword + "\nNew Password: " + newPassword + "\n")
                elif opcode == "00":
                    print("Password Transmission Captured!" +"\nPacket Number: " + packetNumber + "\nOpcode: " + opcode +  "\nPassword: " + newPassword + "\n")

        except Exception as e:
            pass
            #print(e)


def main():
    helpMessage = ("This is a python script that when provided a path to a " +
                  "JSON file will scour \nthat JSON file for any password " +
                  "interaction. This script is compatible with \nthe Quicklock " +
                  "BLE Padlock. To invoke it, please use the following format:\n\n" +
                  "\tpython lockPacketFilter.py some/File/Path.json\n" +
                  "\nEnter 'help', '-h', or 'h' as the parameter to see " +
                  "this message again.\n" )

    if (sys.argv[1] == "-h" or sys.argv[1] == "-help"
        or len(sys.argv) != 2):

        print(helpMessage)
    else:
        findPasswordInteraction()


if __name__ == "__main__":
    main()

