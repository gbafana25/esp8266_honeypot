# ESP8266 honeypot project

# About this project #

This is a honeypot programmed in Micropython for the ESP8266

The honeypot is set up to act as a telnet server.
Original inspiration for this came from the arduino-powered honeypot, found [here.](https://www.reddit.com/r/arduino/comments/5ngt87/this_is_my_arduinopowered_honeypot_if_you_want_to/)

The esp8266 handles all of the socket functions and the terminal prompt.  The access point is disabled in the custom `boot.py` file.  The `boot.py` file must have the WiFi SSID, Wifi password, static IP, subnet mask, router IP, and DNS server address changed as needed.  The ampy config file (whichever one applies to your system) must be edited to point ampy to the right port (COMx for Windows, /dev/ttyUSB* for Linux, /dev/tty.* for Mac)

# What is a honeypot #

A honeypot is a device designed to lure/attract hackers into exploring your device as if it was a legitamte piece of infrastructure or private property that is unprotected.  Many open source honeypots, such as the ones found [here](https://github.com/paralax/awesome-honeypots) are designed to report attacks and gather information about hackers' activity on your network

This honeypot started as a fun thing to do and see how many people still attack Telnet devices.  This honeypot can not be as advanced as the ones linked above, since it is being run on a microcontroller.  This is why it emulates Telnet.  Telnet is a simple protocol that is easy to emulate on microcontroller, due to their being no encryption to worry about.

## The hardware and software ##
   - An ESP8266 microcontroller
   - A Windows, Linux, or MacOS computer :computer:
   - If you have the bare ESP8266 module, you will also need a USB to Serial converter board, and the additional drivers to go with it
   - If you have a board with the USB to Serial chip already on it, you still need the appropriate drivers and a micro USB cable :electric_plug:

