from base64 import urlsafe_b64decode
from base64 import urlsafe_b64encode


#s = 'IzdJOVL8n14AAAAAAAAAIyKp4M61YgF3ZRkxBoJ60L_ZEVRlbGVmb25lIGRlIERpb2dv'
#s = 'IzdJOVL8n14AAAAAAAAAIyLe0ocONEH3GtJSL-NuRXJZEVRlbGVmb25lIGRlIERpb2dv'
s = 'IzlRSkT8n14AAAAAAAAAFwLgZfG9UTrDaojDIMFJjCtcBU1pIEEx'
#s = 'IzlRSkT8n14AAAAAAAAAFwLikXM7S-M1GDWPisM-4C5XBU1pIEEx'
#s = urlsafe_b64encode(s)
# Using base64.urlsafe_b64decode() method
gfg = urlsafe_b64decode(s)
count = 0
namelength = 0
devicename = ""
print(gfg)
bytestr = bytearray(gfg)

for i, bite in enumerate(bytestr):
    #version and mode
    if (i == 0):
        lowfive = bite & 0b00011111
        highthree = bite >> 5
        print ( "Unknown: ", lowfive == 0 ) 
        print ( "Cluster: ", lowfive == 1 ) 
        print ( "Star: ", lowfive == 2 ) 
        print ( "P2P: ", lowfive == 3 ) 
        print("Version", ":",f'{highthree:03b}')
    
    #Endpoint
    if (i == 1):
        print ("Endpoint ID:", end = " ")
    if (i >=1 and i <= 4):
        print (bite, end = " ")


    #Service ID hash
    if (i == 5):
        print()
        print ("Service ID Hash:", end = " ")
    if (i >=5 and i <= 7):
        print (bite, end = " ")

    if (i == 8):
        print()
        print ("WebRTC State:", bite ,end = " ")

    #Reserved bytes, useless per google's code, but shown anyway
    if (i == 9):
        print()
        print ("Reserved:", end = " ")
    if (i >=9 and i <= 14):
        print (bite, end = " ")

    #endpoint info length
    if (i == 15):
        print()
        print ("Endpoint info length:", bite)
 
    #Device name length, byte 34
    if (i == 33):
        namelength = bite
        print ("Device name length: ", namelength)

    if (i > 33 and 33 + namelength >= i):
        character = chr(bite)
        devicename+= character
        if (33 + namelength == i):
            print ("Device name: ", devicename)


    if (i > 15 and i < 33):
        if (i == 16):
            print ("Unknown Bytes:")
        count = count + 1
        print(i, ":", bite)
    


 #bytes after length (defined in byte 15) are for UWB, not relevant for current implementation TODO

 
