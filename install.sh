#!/bin/bash
# this script configures ampy and copies the files to the board
# after you run this reset the board to start the honeypot
# will need to be set to executable before running
export AMPY_PORT=/dev/ttyUSB0 # change this to wherever your ESP8266 shows up on
export AMPY_BAUD=115200
export AMPY_DELAY=0.5
touch main.py
cat esp8266_honeypot.py >> main.py
ampy put boot.py
ampy put sys_messages.py
ampy put main.py