# THE ESP8266 HONEYPOT: A PROJECT TO TRAP SCRIPT KIDDIES EVERYWHERE!! 

:stuck_out_tongue_winking_eye: :stuck_out_tongue_winking_eye: :stuck_out_tongue_winking_eye:

This is a honeypot programmed in Micropython for the ESP8266

The honeypot is set up to act as a telnet server owned by a fake bank.
Port forwarding is needed to be configured in order for the microcontroller to be accessed from a public IP.  The public IP will be your routers IP, port 23 (12.345.678.910:23).  Make sure your router is secured since scanning the IP address of your router will also reveal your router's login console and/or other open ports.  Do this at your own risk!!  I am not liable if you get hacked. Comments on the code are still in progress

Original inspiration for this came from the arduino-powered honeypot, found [here.](https://www.reddit.com/r/arduino/comments/5ngt87/this_is_my_arduinopowered_honeypot_if_you_want_to/)

The esp8266 handles all of the socket functions and the terminal prompt.  The access point is disabled in the custom `boot.py` file.  The `boot.py` file must have the WiFi SSID, Wifi password, static IP, subnet mask, router IP, and DNS server address changed as needed.  The ampy config file (whichever one applies to your system) must be edited to point ampy to the right port (COMx for Windows, /dev/ttyUSB* for Linux, /dev/tty.* for Mac)

# What is a honeypot #

A honeypot is a device designed to lure/attract hackers into exploring your device as if it was a legitamte piece of infrastructure or private property that is unprotected.  Many open source honeypots, such as the ones found [here](https://github.com/paralax/awesome-honeypots) are designed to report attacks and gather information about hackers' activity on your network

# The SCRIPT KIDDIE HOLE OF DOOM #

The ESP8266 in all of its glory: :ok_hand:
![The_hole_of_doom](/images/honeypot_desk.jpg)
On the otherhand, this honeypot started as a funny thing to do and see how many people attacked our network.  This honeypot can not be as advanced as the ones linked above, since it is being run on a microcontroller.  This is why it emulates Telnet.  Telnet is a simple protocol that is easy to emulate on microcontroller, due to their being no encryption to worry about.

## The hardware and software ##
   - An ESP8266 microcontroller ([Adafruit Feather](https://www.adafruit.com/product/2821) version pictured above)
   - A Windows, Linux, or MacOS computer :computer:
   - If you have the bare ESP8266 module, you will also need a USB to Serial converter board, and the additional drivers to go with it
   - If you have a board with the USB to Serial chip already on it, you still need the appropriate drivers and a micro USB cable :electric_plug:

## :ok_hand: Features :ok_hand: ##

   - Console interface has **all-uppercase text** :thumbsup:
   - **Fake** database contents :thumbsup:
   - **Fake** system information :thumbsup:
   - **Fake** FDIC "get off my lawn" warnings :thumbsup:

## The attack sequence and mentality of the script kiddie ##

![script_kiddie](/images/script_kiddies.jpg)

 1.  Your ESP8266 honeypot found either with Shodan, Google Dorks, on accident, etc.
 2.  The hacker scans your router, and finds port 23 open.  An experienced hacker will know it is a              honeypot (routers do not just have port 23 open randomly!!)
 3.  The script kiddie will keep trying to guess the password for the router :confused:, until they decide to try the telnet port, and they get excited that no password is required to login to the server!! :grinning:
 4.  They start entering commands, but after awhile, something doesn't seem right.... **UNTIL THEY TRY          TO EXIT AND REALIZE THAT THEY WERE BEING WATCHED THE WHOLE TIME!!! MWHAHAHAHA** :smiling_imp: :smiling_imp: :astonished: (not really, their IP wasn't logged, the message is just to scare them)

## Deploying the script: ##
 1. Create file `main.py` in the project directory
 2. Copy and paste the contents of `esp8266_honeypot.py` into `main.py` with `cp esp8266_honeypot.py /path/to/main.py`
 3. Run the `ampy_config.bat` or `ampy_config.sh` (depending on your operating system)
 4. Run `ampy put sys_messages.py` and `ampy put status_update.py`
 5. Run `ampy put main.py`
 6. Reset your board for the program to run 
 7. Wait for those l33t h4x0rs!! :ok_hand:

## Monitoring (optional) ##

   ![Wireshark](/images/wireshark_medium.jpg)
 - set up [Wireshark](https://www.wireshark.org/) on a free computer to run all the time and capture packets
 - set a filter for Telnet ports
 - you will be able to see the plain ASCII text, since Telnet is not encrypted!!

## Coming soon: ##

 - more comments on code
 - more commands available to hackers
 - logging of how many times accessed
 - sending of [dweets](http://dweet.io/) to send status updates (Every time the MCU boots up)
 - implement try/except statement in the main code to avoid connection timeout (probably by resetting the     socket or rebooting the MCU)
 - better readme (screenshots, and memes possibly)

*please star this repo if you found it useful*

DM @frogthemonkey25#6628 on Discord if you have any questions or found a typo
