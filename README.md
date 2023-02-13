# SimpleNearby
An attempt at understanding and documenting google's nearby (share) protocol

Check BT_Discovery_Protocol for some documentation and the corresponding bluetooth_name_parse.py script

Offline_Wire_Protocol has description on the protocol used to communicate between devices, this is protobuf but we don't really want many external dependencies
protobuf.py has this implementation 

Bluetooth_connect.py has the implementation of the socket to the nearby (share) service using regular bluetooth
