#tiny implementation of protobuf

from bitstring import BitArray


def IntToVarInt(integer):
    bites = bytearray()
    totalbytes = 0

    while(integer != 0):
        totalbytes+=1
        curbyte = integer&127 # get the 7 LSB bits
        integer=integer>>7 #shift to the right by 7 to get the next byte
        bites.append(curbyte) #add to final byte array 

    #set the continuation bit
    for i,x in enumerate(bites):
        if(i+1<totalbytes): #if the current byte is not the last
            bites[i] = bites[i]|128 #set the 8th bit to 1

    return bites

#Converts Varint to Int
#This is an abomination, but it works
def VarIntToInt(varint):
    varint.reverse() #Put it into little endian
    varintarray = BitArray(varint) 
    intarray = BitArray(7*len(varint))

    pos = 0

    for i, x in enumerate(varintarray):
        if (i + 1) % 8: #check if we are not on the 8th bit (continuation bit) of any byte
            intarray[pos] = varintarray[i+1] #if we are not then this bit is important, put it on the binary int array
            pos+=1

    #convert bits to integer
    i = 0
    for bit in intarray:
        i = (i << 1) | bit
    return (i)


print(VarIntToInt(IntToVarInt(1231)))
