import argparse
import asyncio

from bleak import BleakScanner
from bleak import BleakClient

rcvdevices = []

async def main(args: argparse.Namespace):
    print("scanning for 5 seconds, please wait...")


    devices = await BleakScanner.discover(
        return_adv=True, cb=dict(use_bdaddr=args.macos_use_bdaddr)
    )
    for key, value in devices.items():
        if "0000fe2c-0000-1000-8000-00805f9b34fb" in value[1].service_data:
            print(key + " is doing nearby share thingies (likely sharing)")
            print(value[1].service_data["0000fe2c-0000-1000-8000-00805f9b34fb"])
        
        if "0000fef3-0000-1000-8000-00805f9b34fb" in value[1].service_data:
            print(key + " is doing nearby share thingies (likely recieving)")
            print(value[1].service_data["0000fef3-0000-1000-8000-00805f9b34fb"])
            rcvdevices.append(key)

    #this errors for devices not sharing to everyone
    for mac in rcvdevices:
        async with BleakClient(mac) as client:
            model_number = await client.read_gatt_char("00000000-0000-3000-8000-000000000000")
            print(model_number)
            print(''.join(format(x, '02x') for x in model_number))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--macos-use-bdaddr",
        action="store_true",
        help="when true use Bluetooth address instead of UUID on macOS",
    )

    args = parser.parse_args()

    asyncio.run(main(args))
