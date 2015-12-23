#Stated all the queries as functions (WMI based on WQL for getting the device details).

import wmi
import data
import gc

def getnicinfo():
    c = wmi.WMI()
    wql = "SELECT * FROM Win32_NetworkAdapter WHERE PhysicalAdapter=true AND Manufacturer != 'Microsoft' AND NOT PNPDeviceID LIKE 'ROOT\\%'"
    temp = c.query(wql)
    deviceList = list()
    gc.enable()
    print("\nreturns physical NIC")
    for J in temp:
        x = data.device()
        x.ProductName = J.ProductName
        x.PNPDeviceID = J.PNPDeviceID
        x.Manufacturer = J.Manufacturer
        x.Name = J.Name
        deviceList.append(x)
    return deviceList

def getPnpDeviceInfo():
    c = wmi.WMI()
    wql = "SELECT * FROM Win32_PnPEntity WHERE Manufacturer != 'Microsoft' AND NOT PNPDeviceID LIKE 'ROOT\\%'"
    temp = c.query(wql)
    deviceList = list()
    print("\n returns physical PNP device")
    gc.enable()
    for J in temp:
        x = data.device()
        x.PNPDeviceID = J.PNPDeviceID
        x.Manufacturer = J.Manufacturer
        x.Name = J.Name
        x.Caption = J.Caption
        deviceList.append(x)
    return deviceList

def getUnknownPnpDeviceInfo():
    c = wmi.WMI()
    wql = "SELECT * FROM Win32_PnPEntity WHERE Manufacturer != 'Microsoft' AND (Status != 'OK' AND Status !='') AND NOT PNPDeviceID LIKE 'ROOT\\%'"
    temp = c.query(wql)
    deviceList = list()
    gc.enable()
    print("\n returns physical unknown PNP dervice")
    for J in temp:
        x = data.device()
        x.PNPDeviceID = J.PNPDeviceID
        x.Manufacturer = J.Manufacturer
        x.Name = J.Name
        x.Caption = J.Caption
        deviceList.append(x)
    return deviceList

def getUnknownNetworkAdapterInfo():
    c = wmi.WMI()
    wql =  "SELECT * FROM Win32_NetworkAdapter WHERE Manufacturer != 'Microsoft' AND Installed = FALSE AND NOT PNPDeviceID LIKE 'ROOT\\%'"
    temp = c.query(wql)
    deviceList = list()
    gc.enable()
    print("\n returns unknown physical NIC")
    for J in temp:
        x = data.device()
        x.ProductName = J.ProductName
        x.PNPDeviceID = J.PNPDeviceID
        x.Manufacturer = J.Manufacturer
        x.Name = J.Name
        deviceList.append(x)
    return deviceList
