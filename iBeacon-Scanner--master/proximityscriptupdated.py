# test BLE Scanning software
# jcs 6/8/2014

#iBeacon Imports
import blescan
import sys

import bluetooth._bluetooth as bluez

#E-mail Imports
import smtplib
from email.message import EmailMessage

#Other imports
import time

#Setting stuff
dev_id = 0

estimote_udid = "b9407f30f5f8466eaff925556b57fe6d"

beacon1_mac = "ec:45:18:5f:22:c7"	#Purple
beacon2_mac = "dc:96:50:47:28:19"	#Yellow

sender = emicb55@gail.com			#sender email address
reciever = emicb55@gmail.com		#reciever email address

#Notification stuff
def sendMail():
	with open(textfile) as fp:
		msg = EmailMessage()
		msg.set_content(fp.read())
		
	msg['Subject'] = 'The contents of %s' % textfile
	msg['From'] = sender
	msg['To'] = reciever
	
	s = smtplib.SMTP('loacalhost')
	s.send_message(msg)
	s.quit()
	
	time.sleep(300)			#delays for 5 minutes (sleep is in seconds)

#iBeacon stuff
try:
	sock = bluez.hci_open_dev(dev_id)
	print ("ble thread started")

except:
	print ("error accessing bluetooth device...")
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print ("----------")
	for beacon in returnedList:
		beacon_split = beacon.split(",")
		beacon_udid = beacon_split[1]
		beacon_mac = beacon_split[0]		
		beacon_rssi = beacon_split[5]		#higher number = further
		if beacon_udid == estimote_udid:
			if beacon_mac == beacon1_mac:
				print ("Purple iBeacon: " + beacon_rssi)
				if beacon_rssi <= 50:
					print ("Purple iBeacon is close")
					sendMail()
			if beacon_mac == beacon2_mac:
				print ("Yellow iBeacon: " + beacon_rssi)
				if beacon_rssi <= 50:
					print ("Yellow iBeacon is close")	
					sendMail()

