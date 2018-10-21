
# This is a module with all the fake system messages
# If you have any other messages to add, put them here, and then implement them in esp8266_honeypot.py

welcome = b'\r\n\nFDIC  FRONTIER SAVINGS BANK\r\nWARNING: UNAUTHORIZED USE IS PROHIBITED BY LAW\r\n'
# array_number     0            1              2                   3                4              5           6
commands = [b'SYS_STATUS', b'DB_LIST', b'ACCOUNT_MANAGER', b'DEVICE_MANAGER', b'NAS_STATUS', b'EXIT']

valid_commands = b'\r\n\nSYS_STATUS - DISPLAY SYSTEM INFO\r\nDB_LIST - SHOW CURRENT DATABASE LISTING\r\nACCOUNT_MANAGER - OPENS ACCOUNT MANAGER\r\nDEVICE_MANAGER - SHOW CURRENTLY ATTACHED DEVICES\r\nNAS_STATUS - SHOWS STATUS OF NETWORK DRIVES\r\nEXIT - CLOSE CONNECTION\r\n\n'

prompt = 'FSB_MNGR:---> '

sys_info = b'\r\n\nKRAMER MANAGEMENT SYSTEMS\r\nENHANCED DATABASE AND DOMAIN CONTROLLER SYSTEM V2\r\n\nOS: GM/OS\r\nVERSION: 3.04R3\r\nCPU USAGE: 12%\r\nRAM USAGE: 7%\r\n\n'

database = b'\r\nACCOUNT LIST:\r\n----------------------\r\nBUSINESS: 45,903\r\nHOME: 73,459\r\nCURRENT TRANSFERS: 7,824\r\n\n'

attached_devices = b'\r\n\nDEVICE LIST:\r\n--------------------\r\nFLOPPY DRIVE: DISK NOT INSERTED\r\nHARD DISK(1): 1.2MB/64MB USED\r\nNETWORK DRIVE(S): FSB NAS SYSTEM -- RUN NAS_STATUS FOR MORE INFO\r\n\n'

nas_status = b'\r\n\nNETWORK DRIVE DIAGNOSTIC TOOL\r\n---------------------------\r\n\n\r\nNETBOOT DISK:  39.9M/40M  OK  FAT\r\nRAID SETUP:\r\nRAID DISK 1: 119.7M/120M  OK  FAT\r\nRAID DISK 2: 119.7M/200M  OK  FAT\r\nRAID DISK 3: 119.7M/200M  OK  FAT\r\nRAID DISK 4: 119.7M/200M  OK  FAT'