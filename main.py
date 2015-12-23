#functions calling in the queries.py class, which lists the functions with the WQL queries>

import queries

#get real NIC info
deviceList = queries.getnicinfo()
for i in deviceList:
    print("\nProduct Name " + i.ProductName)
    print("Device ID " + i.PNPDeviceID)
    print("Silly Name " + i.Name)
    print("Brand name " + i.Manufacturer)

#get real PNP device info
deviceList = queries.getPnpDeviceInfo()
for i in deviceList:
    print("\nProduct Name " + i.Caption)
    print("Device ID " + i.PNPDeviceID)
    print("Silly Name " + i.Name)
    print("Brand name " + i.Manufacturer)

#get real undetected  NIC info
deviceList = queries.getUnknownNetworkAdapterInfo()
for i in deviceList:
    print("\nProduct Name " + i.Caption)
    print("Device ID " + i.PNPDeviceID)
    print("Silly Name " + i.Name)
    print("Brand name " + i.Manufacturer)

#get real undetected PNP device info
deviceList = queries.getUnknownPnpDeviceInfo()
for i in deviceList:
    print("\nProduct Name " + i.ProductName)
    print("Device ID " + i.PNPDeviceID)
    print("Silly Name " + i.Name)
    print("Brand name " + i.Manufacturer)
