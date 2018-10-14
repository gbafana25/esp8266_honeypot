# this file runs every time at boot
# please fill in wifi credentials and ifconfig lines for a static IP
# the values in the ifconfig function need to be changed to a static IP, your router IP, and you DNS server
#import esp
#esp.osdebug(None)
import gc
import network
#import webrepl
#webrep.start()
gc.collect()

# sets access point as false, since it is not needed
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('ssid', 'password')
station.ifconfig(('192.168.0.200','255.255.255.0','192.168.0.1','68.105.28.11'))
