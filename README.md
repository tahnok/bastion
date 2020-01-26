# BASTION

Raspberry Pi powered base station for Hummingbird.
Reads and decodes LoRa packets and shows 'em to you.

Uses a RFM95 LoRa module wired to the SPI pins on the Pi. Software setup from this [adafruit guide](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/overview)

Hardware connections:

 - Vin to Raspberry Pi 3.3V
 - GND to Raspberry Pi Ground
 - RFM RST to Raspberry Pi GPIO #25
 - RFM CLK to Raspberry Pi SCK #11
 - RFM MISO to Raspberry Pi MISO #9
 - RFM MOSI to Raspberry Pi MOSI #10
 - RFM CS to Raspberry Pi CE1 #7

Extra maybe?

 - RFM G0 to Raspberry Pi GPIO #5
