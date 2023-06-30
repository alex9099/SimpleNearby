count = 0
namelength = 0
devicename = ""
endpointID = ""
firstserviceID = bytearray()
secondserviceID = bytearray()
bytestr = bytearray(b'H\xfc\x9f^\x00\x00\x00(#\xfc\x9f^17J4\x17"\x83G\x1e\xde, \x83x\xa1\xa5>6\x85\x15\xfcW\x05Mi A1\x18\xf0\xe4<\x07\x8b\x00\x00Wk')

for i, bite in enumerate(bytestr):
    
    if (i >= 1 and i < 4):
        firstserviceID.append(bite)

    if (i==4):
        print("reserved bytes (4-6): ", end = "")
    if (i >= 4 and i <= 6 ):
        print(bite, end = "")

    if (i >= 9 and i <= 11):
        secondserviceID.append(bite)

    if (i == 12):
        print ("\nfirst and second service id equal: ", firstserviceID == secondserviceID)
        print ("service IDs: ", firstserviceID, secondserviceID)


    #Endpoint (supposed to be a string)
    if (i == 12):
        print ("Endpoint ID:", end = " ")
    if (i >= 12 and i <= 15): 
        endpointID+= chr(bite)
        if (i==15):
            print (endpointID)


    #this seems to always be 34, which is where the device name lenght is, perhaps there could be some extra information that would shift the device name?
    if (i == 17):
        print("Device name position?: byte", bite)

    #Device name length, byte 34
    if (i == 34):
        namelength = bite
        print ("Device name length: ", namelength)


    #device name
    if (i > 34 and 34 + namelength >= i):
        character = chr(bite)
        devicename+= character
        if (34 + namelength == i):
            print ("Device name: ", devicename)

    #mac address
    if (34 + namelength == i):
        print("bt mac address: ", end = "")
    if (34 + namelength < i and 34 + namelength + 6 >= i):
        print(format(bite, '02X'), end = " ")
 