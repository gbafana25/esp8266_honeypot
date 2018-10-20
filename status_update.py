
# This is currently not used, but it would be implemented in the future to provide status updates through dweet.io,
# a free IoT messaging service.  If you would like to use a paid lock and a alert system, that can be added here as well
# Fore more information visit dweet.io

def sendStatus():
    # gets IP address in raw form
    raw_ip = urequests.get('http://api.ipify.org')
    # converts to string format
    ip = raw_ip.text
    # if dweet is used, then change the thing name to something unique, do not keep this one
    send_ip = urequests.get('https://dweet.io/dweet/for/telnetespserver?ip=%s' % ip)