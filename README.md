To deauthenticate A WI-FI Target # All you need know is victim mac address 

commands to know victim MAC address 
    " ~# sudo airodump-ng  wlan0 "
    " ~# copy the target MAC address"


In case if you want to send a packet anonymously to a router don't change addr 1 or change it to a random mac or use macchanger 

uncomment  line number 3 or target1 and make changes in addr3 = target to target1 # to make a perticular target to deauthenticate from a network

each deauth packet removes the victim from network for 10 seconds 
 
Follow for new Updates https://github.com/TUDDUMDEBBA/Wifi_Deauthentication.git
