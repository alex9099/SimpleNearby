from bluetooth import *
import sys

if sys.version < '3':
    input = raw_input

addr = "18:F0:E4:3C:07:8B"

if len(sys.argv) < 2:
    print("no device specified.  Searching all nearby bluetooth devices for")
    print("the NearbyShare service")
else:
    addr = sys.argv[1]
    print("Searching for NearbyShare on %s" % addr)

# search for the NearbyShare service
uuid = "a82efa21-ae5c-3dde-9bbc-f16da7b16c5a"

service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
    print("couldn't find the NearbyShare service =(")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

print("connected.  type stuff")
while True:
    data = input()
    if len(data) == 0: break
    sock.send(data)
