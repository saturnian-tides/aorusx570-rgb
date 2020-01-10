# Aorus570-RGB

This is a really barebones interface I cobbled together to allow
access to setting RGB values on Aorus X570 motherboards. It may
work on other Aorus or Gigabyte motherboards as well. In this case
I tested with an Aorus Pro Wifi. **Use at your own risk!**

**License: MIT**

Requirements:
- python3
- cython-hidapi (make sure to install "hid", not "hidapi")
- either root access or permissions to enable regular users to send
SET_REPORTs over HID

The main interface for configuring the RGB values is a USB-HID device 
from ITE. You can find an entry via lsusb similar to this:

`Bus 001 Device 002: ID 048d:8297 Integrated Technology Express, Inc.`

Refer to sample.py for usage, possible zones I've uncovered are enumerated
in the zone_dict in aorusx570_rgb.py. I've only so far been able to confirm
that DLED_1 (5v ARGB), LED_CX (12v RGB, there are two headers but they use the 
same settings) and IO_LED work. I may try out the others as I get more RGB
accessories. 

Only static color changes are supported - it's up to the user to use this to 
implement more interesting patterns in their own wrapper. 

As is this is good enough for my own needs, but I'm leaving this public
in case someone from a larger project such as OpenRGB wants to utilize
these findings.
