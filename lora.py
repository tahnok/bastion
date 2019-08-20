"""
Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
"""
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import the RFM9x radio module.
import adafruit_rfm9x
import struct
from datetime import datetime
import sys


# Configure RFM9x LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23

prev_packet = None
print("RFM9x: detected")


while True:
    packet = rfm9x.receive()
    if packet is not None:
        now = datetime.now().strftime('%H:%M:%S')
        try:
            temperature, pressure, battery_voltage, packet_number, flight_number = struct.unpack('fifII', packet)
        except struct.error:
            print("Invalid packet")
            print(packet)
            continue
        print("%d, %s, %d, %fC, %d Pa, %fV" % (flight_number, now, packet_number, temperature, pressure, battery_voltage))
        time.sleep(1)
    else:
        print("nothin")
    sys.stdout.flush()

    time.sleep(0.1)
