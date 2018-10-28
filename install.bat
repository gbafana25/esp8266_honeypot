@echo off
REM this batch file now sets up ampy and copies all the files to the board
REM specify COM port as needed
REM delay is required in order for files to be sent correctly
REM run this in the project directory and reset your board to start the code
set AMPY_PORT=COM3
set AMPY_BAUD=115200
set AMPY_DELAY=0.5
type esp8266_honeypot.py > main.py
ampy put boot.py
ampy put sys_messages.py
ampy put main.py 
