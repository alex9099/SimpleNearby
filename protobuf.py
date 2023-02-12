#tiny implementation of protobuf


def IntToVarInt(integer):
    bites = bytearray()
    count = 0

    while(integer != 0):
        count+=1
        curbyte = integer&127 # get the 7 LSB bits
        integer=integer>>7 #shift to the right by 7 to get the next byte
        bites.append(curbyte) #add to final byte array 

    #set the continuation bit
    for i,x in enumerate(bites):
        if(i+1<count): #if the current byte is not the last
            bites[i] = bites[i]|128 #set the 8th bit to 1

    return bites
        
def VarIntToInt(varint):
    print(varint) #TODO

print(IntToVarInt(150))

