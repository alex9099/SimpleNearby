# OfflineFrame{
#     version: 1,
#     v1, 2{
#         type: 1, #(CONNECTION_REQUEST)
#         connection_request, 2{
#             endpoint_id, 1: "ABCD",
#             endpoint_name, 2: "My device",
#             endpoint_info, 6: bytes, #those unknown bytes from BT name?
#             nonce, 4: random 32bit int,
#             medium_metadata, 7{
#                 supports_5_ghz, 1: true or false,
#                 bssid, 2: mac addr,
#                 ap_frequency, 6: Freq in MHz,
#                 ip_address, 3: ip in bytes,   
#             }
#             mediums, 5 (repeated){
#                 #let's assume there's wifi_hotspot and bluetooth
#                 BLUETOOTH 2,
#                 WIFI_HOTSPOT 3
#             },
#             keep_alive_interval_millis, 8: ?
#             keep_alive_timeout_millis, 9: ?
#         }
#     }
# }

import protobuf 
import random

endpoint_id = "ABCD"
endpoint_name = "My device"
endpoint_info = "whatever"
offline_frame = {
    1: 1, #V1
    2: {
        1: 1, #(CONNECTION_REQUEST)
        2: {
            1: endpoint_id,
            2: endpoint_name,
            6: endpoint_info,
            4: random.getrandbits(32),
            7: {
                1: True,
                2: "de:ad:be:ee:ee:ef",
                6: 2450,
                3: "127.0.0.1"
            },
            5: [2, 3],
            8: 1000, #keep_alive_interval_millis
            9: 10000 #keep_alive_timeout_millis
        }
    }
}


protobuf.getbinarypacket(offline_frame)


