@echo off
REM this batch file sets up ampy to connect to the microcontroller in your current directory
REM specify COM port as needed
REM delay is required in order for files to be sent correctly
set AMPY_PORT=COM3
set AMPY_BAUD=115200
set AMPY_DELAY=0.5