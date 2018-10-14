 # ESP8266 FAKE HONEYPOT
 # DESIGNED TO ACT AS A TELNET SERVER
# Features:
#   all uppercase text in the interface
#   fake system details
#   fake database
#   
#   made by the one and only Kramer Management Systems!! (not a real thing)
#   
#   Todo:
#   log how many times it has been accessed
#   send status updates through dweet.io
#

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import machine
import urequests

welcome = b'\r\n\nFDIC  FRONTIER SAVINGS BANK\r\nWARNING: UNAUTHORIZED USE IS PROHIBITED BY LAW\r\n'
commands = [b'SYS_STATUS', b'LIST', b'EXIT']
valid_commands = b'\r\n\nSYS_STATUS\r\nLIST\r\nEXIT\r\n\n'
prompt = 'FSB_MNGR:---> '
sys_info = b'\r\n\nKRAMER MANAGEMENT SYSTEMS\r\nENHANCED DATABASE SYSTEM V2\r\n\nOS: GM/OS\r\nVERSION: 3.04R3\r\nCPU USAGE: 12%\r\nRAM USAGE: 7%\r\n\n'
database = b'database here\r\n\n'

def showPrompt():
    for i in range(1):
        conn.sendall(prompt)

# currently not used, would be used for status updates
def sendCurrentIP():
    raw_ip = urequests.get('http://api.ipify.org')
    ip = raw_ip.text
    # if dweet is used, then change the thing name to something unique, do not keep this one
    send_ip = urequests.get('https://dweet.io/dweet/for/telnetespserver?ip=%s' % ip)

sk = socket(AF_INET, SOCK_STREAM)
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('192.168.0.200', 23))
sk.listen(5)
conn,addr = sk.accept()
conn.sendall(welcome)

while True:
    data = conn.recv(1024)
    if data == commands[0]:
        conn.sendall(sys_info)
    elif data == commands[1]:
        conn.sendall(database)
    elif data == commands[2]:
        conn.sendall(b'\r\nCLOSING CONNECTION...')
        conn.close()
        sk.close()
        del sk
        break
    elif data != commands and data == b'\r\n' and data != b'':
        showPrompt()
    elif data not in commands:
        conn.sendall(b'\r\n\nVALID COMMANDS\r\n\n')
        conn.sendall(valid_commands)
    if not data:
        conn.sendall(data)
