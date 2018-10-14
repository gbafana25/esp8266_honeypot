# esp8266_honeypot
This is a honeypot programmed in Micropython for the ESP8266

The honeypot is set up to act as a telnet server owned by a fake bank.
Port forwarding is needed to be configured in order for the microcontroller to be accessed from a public IP.
Comments on the code are still in progress

Original inspiration for this came from the arduino-powered honeypot, found [here.](https://www.reddit.com/r/arduino/comments/5ngt87/this_is_my_arduinopowered_honeypot_if_you_want_to/)

The esp8266 handles all of the socket functions and the terminal prompt.  The access point is disabled in the custom `boot.py` file.  The `boot.py` file must have the WiFi SSID, Wifi password, static IP, subnet mask, router IP, and DNS server address changed as needed.  The ampy config file (whichever one applies to your system) must be edited to point ampy to the right port (COMx for Windows, /dev/ttyUSB* for Linux, /dev/tty.* for Mac)

Deploying the script:
 1. Create file `main.py` in the project directory
 2. Copy and paste the contents of `esp_8266_honeypot.py` into `main.py`
 3. Run the `ampy_config.bat` or `ampy_config.sh` (depending on your operating system)
 4. Run `ampy put main.py`
 5. Reset your board for the program to run 

Coming soon:

 - more comments on code
 - more commands available to hackers
 - logging of how many times accessed
 - sending of [dweets](http://dweet.io/) to send status updates
 - use of time.sleep() commands in order to emulate a old terminal with a slow baudrate
 - a bash script to setup ampy for Unix systems