# esp8266_honeypot
This is a honeypot programmed in Micropython for the ESP8266

The honeypot is set up to act as a telnet server owned by a fake bank.
Port forwarding is needed to be configured in order for the microcontroller to be accessed from a public IP.
Comments on the code are still in progress

Original inspiration for this came from the arduino-powered honeypot https://www.reddit.com/r/arduino/comments/5ngt87/this_is_my_arduinopowered_honeypot_if_you_want_to/
The esp8266 handles all of the socket functions and the terminal prompt.
