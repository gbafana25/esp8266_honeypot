
# This is a module with all the fake system messages
# If you have any other messages to add, put them here, and then implement them in esp8266_honeypot.py

welcome = b'\r\n\nFDIC  FRONTIER SAVINGS BANK\r\nWARNING: UNAUTHORIZED USE IS PROHIBITED BY LAW\r\n'
commands = [b'SYS_STATUS', b'DB_LIST', b'ACCOUNT_MANAGER', b'DEVICE_MANAGER', b'EXIT']
valid_commands = b'\r\n\nSYS_STATUS - DISPLAY SYSTEM INFO\r\nDB_LIST - SHOW CURRENT DATABASE LISTING\r\nACCOUNT_MANAGER - OPENS ACCOUNT MANAGER\r\nDEVICE_MANAGER - SHOW CURRENTLY ATTACHED DEVICES\r\nEXIT - CLOSE CONNECTION\r\n\n'
prompt = 'FSB_MNGR:---> '
sys_info = b'\r\n\nKRAMER MANAGEMENT SYSTEMS\r\nENHANCED DATABASE SYSTEM V2\r\n\nOS: GM/OS\r\nVERSION: 3.04R3\r\nCPU USAGE: 12%\r\nRAM USAGE: 7%\r\n\n'
database = b'\r\nACCOUNT LIST:\r\n----------------------\r\nBUSINESS: 45,903\r\nHOME: 73,459\r\nCURRENT TRANSFERS: 7,824\r\n\n'
attached_devices = b'\r\n\nDEVICE LIST:\r\n--------------------\r\nFLOPPY DRIVE: DISK NOT INSERTED\r\nHARD DISK(1): 72MB/512MB USED\r\nNETWORK DRIVE(S): FSB NAS SYSTEM -- RUN NAS_STATUS FOR MORE INFO\r\n\n'