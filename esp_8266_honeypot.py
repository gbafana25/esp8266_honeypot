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

welcome = b'\r\n\nFDIC  FRONTIER SAVINGS BANK\r\nWARNING: UNAUTHORIZED USE IS PROHIBITED BY LAW\r\n'
commands = [b'SYS_STATUS', b'DB_LIST', b'ACCOUNT_MANAGER', b'DEVICE_MANAGER', b'EXIT']
valid_commands = b'\r\n\nSYS_STATUS - DISPLAY SYSTEM INFO\r\nDB_LIST - SHOW CURRENT DATABASE LISTING\r\nACCOUNT_MANAGER - OPENS ACCOUNT MANAGER\r\nDEVICE_MANAGER - SHOW CURRENTLY ATTACHED DEVICES\r\nEXIT - CLOSE CONNECTION\r\n\n'
prompt = 'FSB_MNGR:---> '
sys_info = b'\r\n\nKRAMER MANAGEMENT SYSTEMS\r\nENHANCED DATABASE SYSTEM V2\r\n\nOS: GM/OS\r\nVERSION: 3.04R3\r\nCPU USAGE: 12%\r\nRAM USAGE: 7%\r\n\n'
database = b'\r\nACCOUNT LIST:\r\n----------------------\r\nBUSINESS: 45,903\r\nHOME: 73,459\r\nCURRENT TRANSFERS: 7,824\r\n\n'
attached_devices = b'\r\n\nDEVICE LIST:\r\n--------------------\r\nFLOPPY DRIVE: DISK NOT INSERTED\r\nHARD DISK(1): 72MB/512MB USED\r\nNETWORK DRIVE(S): FSB NAS SYSTEM -- RUN NAS_STATUS FOR MORE INFO\r\n\n'

# shows terminal prompt
def showPrompt():
    for i in range(1):
        conn.sendall(prompt)

# currently not used, would be used for status updates
def sendStatus():
    # gets IP address in raw form
    raw_ip = urequests.get('http://api.ipify.org')
    # converts to string format
    ip = raw_ip.text
    # if dweet is used, then change the thing name to something unique, do not keep this one
    send_ip = urequests.get('https://dweet.io/dweet/for/telnetespserver?ip=%s' % ip)

sk = socket(AF_INET, SOCK_STREAM)
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('192.168.0.200', 23))
sk.listen(5)
conn,addr = sk.accept()
conn.sendall(welcome)

# loops forever while client is connected, checks input with commands list
while True:
    data = conn.recv(1024)
    # displays fake system information
    if data == commands[0]:
        time.sleep(1)
        conn.sendall(sys_info)
    # shows fake database
    elif data == commands[1]:
        time.sleep(1)
        conn.sendall(database)
    # attempts to open fake account management application
    elif data == commands[2]:
        time.sleep(1)
        conn.sendall(b'\r\nERROR: PROCESS IN USE\r\n\n')
    elif data == commands[3]:
        time.sleep(1)
        conn.sendall(attached_devices)
    # closes connection
    elif data == commands[4]:
        conn.sendall(b'\r\nCLOSING CONNECTION...   AND LOGGING YOUR IP')
        time.sleep(1)
        conn.close()
        sk.close()
        del sk
        break
        machine.reset()
    elif data != commands and data == b'\r\n' and data != b'':
        showPrompt()
    elif data not in commands:
        conn.sendall(b'\r\n\nVALID COMMANDS\r\n\n')
        conn.sendall(valid_commands)
    if not data:
        conn.sendall(data)