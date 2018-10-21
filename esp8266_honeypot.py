 # ESP8266 FAKE HONEYPOT
 # DESIGNED TO ACT AS A TELNET SERVER
# Features:
#   all uppercase text in the interface
#   fake system details
#   fake database
#   fake deterring FDIC warnings
#  ------------------------------------------------------------------------------------    
# 
#   made by the one and only Kramer Management Systems!! (not a real thing)
#   
#   Todo:
#   log how many times it has been accessed (probably logging it to a file on the board's internal filesystem)
#   send status updates through dweet.io
#   

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import machine
import time
import urequests
import sys_messages
import status_update


# shows terminal prompt
def showPrompt():
    for i in range(1):
        conn.sendall(sys_messages.prompt)

sk = socket(AF_INET, SOCK_STREAM)
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.settimeout(None)
sk.bind(('192.168.0.200', 23))
sk.listen(5)
conn,addr = sk.accept()
conn.sendall(sys_messages.welcome)
status_update.sendStatus()

# loops forever while client is connected, checks input with commands list
while True:
    data = conn.recv(1024)
    try:
        if data == sys_messages.commands[0]:
            time.sleep(1)
            conn.sendall(sys_messages.sys_info)   
        elif data == sys_messages.commands[1]:
            time.sleep(1)
            conn.sendall(sys_messages.database)
        elif data == sys_messages.commands[2]:
            time.sleep(1)
            conn.sendall(b'\r\nERROR: PROCESS IN USE\r\n\n')
        elif data == sys_messages.commands[3]:
            time.sleep(1)
            conn.sendall(sys_messages.attached_devices)
        elif data == sys_messages.commands[4]:
            time.sleep(1)
            conn.sendall(sys_messages.nas_status)
        elif data == sys_messages.commands[5]:
            conn.sendall(b'\r\nCLOSING CONNECTION...   AND LOGGING YOUR IP')
            time.sleep(1)
            conn.close()
            sk.close()
            del sk
            machine.reset()
        elif data != sys_messages.commands and data == b'\r\n' and data != b'':
            showPrompt()
        elif data not in sys_messages.commands:
            conn.sendall(b'\r\n\nVALID COMMANDS\r\n\n')
            conn.sendall(sys_messages.valid_commands)
        if not data:
            conn.sendall(data)
    except OSError:
        conn.close()
        sk.close()
        del sk
        machine.reset()
