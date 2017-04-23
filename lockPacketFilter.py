import json
from pprint import pprint


desired_handle = "0x0000002d"
desired_serviceUUID = "65488"
desired_uuid = "65494"

with open("lockPacketInfo.json") as data_file:
    data = json.load(data_file)


for dataPoint in data:
    try:
        if (dataPoint["_source"]["layers"]["btatt"]["btatt.handle"] ==
            desired_handle and dataPoint["_source"]["layers"]["btatt"]["btatt.handle_tree"]["btatt.service_uuid16"]
            == desired_serviceUUID and dataPoint["_source"]["layers"]["btatt"]["btatt.handle_tree"]["btatt.uuid16"]
            == desired_uuid):
            


            #print("######FOUND IT########")
            #pprint(dataPoint["_source"]["layers"]["frame"]["frame.number"])
            pprint(dataPoint["_source"]["layers"]["btatt"]["btatt.value"])
    except Exception as e:
        pass
        #print(e)
    



