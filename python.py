import os, sys, platform, subprocess, socket
from scapy import*
from time import sleep
from fastapi import File


#############################################################
#							    #				#.
#	Pyphone is a free remote penetration    #
#	testing tool powered by nmap. 		    #
#   		     			                    #
#   							    #
#    							    #
#   You can use the software and		    #								#/.°*
#	modify it as you wish.					#					#/.°
#							    #		#
#											#
#	How to use it :							#			#/°*
#		pyphone [-b bind_address] [-sc]	            #					#/.*°
#				[-wpa (handshake)]		    #
#				[-conf (reconf)]            #
#				[-sn (ipaddr)][-r record]   #
#							    #				#
#############################################################

main_msg = """\n\033[0;35m
		       ____$$$$$$$$$$
		      ___$_________ $$
		     ____$_$$$$$$$_ $$
		    _____$_$     $_ $$
		    _____$_Python$_ $$			
		    _____$_Termux|_ $$			‖	PyPhone Script : execute scripts remotely or execute scripts- ‖
		    _____$_$     $_ $$           		‖           directly on your phone ! -Developped by Nathan Raymond    ‖
		    _____$_$$$$$$$_ $$ 
		    _____$_________ $$
		     _____$$$$$$$$$$
		     ____$_________$$
		    ____$_1__2__3_$$$
		   ____$_4__5__6_$$$
		   ___$_7__8__9_$$$
		  ___$_*__0__#_$$$
		  __$_________$$$
		   __$$$$$$$$$$$
		    __$$$$$$$$$
		\033[0;35m\n"""


#configure all of the messages
bye_msg = "\033[1;31mShutting down... Goodbye ! ( ^_^)/ \033[1;31m"
root_msg = "\033[1;31mPyPhone should be ran as root !\033[1;31m"
err_msg = "\033[1;31mError ! Something went wrong !\033[1;31m"
ssid_banner = """\033[1;31m|==============================================================|
			   
			   	           ⢠⡾⠃⠀⠀⠀⠀⠀⠀⠰⣶⡀⠀
			 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢠⡿⠁⣴⠇⠀⠀⠀⠀⠸⣦⠈⢿⡄⠀  SSID : {ssid}
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣾⡇⢸⡏⢰⡇⠀⠀⢸⡆⢸⡆⢸⡇⠀  Security : {Security}
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠘⣧⡈⠃⢰⡆⠘⢁⣼⠁⣸⡇⠀    ------------------
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠘⠃⠀⢸⡇⠀⠘⠁⣰⡟⠀⠀  Bandwidth : {Bandwidth}
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⢸⡇⠀⠀⠘⠋⠀⠀⠀  ip_addr : {ipaddr}
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀  
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃
			   |==============================================================|

			\033[1;31m"""
audio_msg = "\n033[1;31m[Playing ━━━━⬤─────── Playing...]033[1;31m\n
"
if not os.geteuid()==0:
	sys.exit(root_msg)

def home():
	try:
		def config(): #configure parameters for options()
			try:
				#assuming user is connected to internet. If not, any function except search_network will return err_msg
				global prvaddr
				global user
				global macaddr
				global hostname
				global prvaddrsrc
				prvaddr = os.popen("ifconfig | grep broadcast | awk '{print $2}'").read()
				prvaddr = prvaddr[:-1]
				user = os.getlogin()
				macaddr = os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read()
				hostname = os.popen("hostname -I").read()
				prvaddrsrc = os.popen("ip route show | tail -n1 | awk '{print $1}' | cut -f1 -d'/'").read()
			
			
		def bind_ssh(ipaddr):
			try:
				sleep(1)
				os.system("ssh root@{ipaddr}")
				device_name = os.popen("platform.system()")
				print("Connected to device {ipaddr} on {device_name} !")
			except ValueError:
				sys.exit(err_msg)
			
		if platform.system() == "Linux" or "Windows" or "Darwin":
			print("Connect phone with ssh ?\n")
			choice = raw_input(">>> ")
			if choice =="y" or "Y":
				ipaddr = input("Please input the phone's ip to connect with ssh : ")
				bind_ssh(ipaddr)
			elif choice =="n" or "N":
				options()
			else:
				sys.exit(err_msg)
		def options():
			print("""	 1) Scan nearby networks
					 2) Port scanner
					 3) Sniff data
					 4) WPA2 handshake cracking 
					 5) Start background-audio recording (phone ==> computer)
					 6) Exit""")
			choice = raw_input(">>> ")
			def scan():
				try:
					global network_list
					networks = subprocess.network("wlan", "network", "netsh", "")
					networks.decode("ascii")
					networks_list = []
					networks.append(networks_list)
					for elems in networks_list:
						for j in elems:
							SSID = elems[0]
							Security = elems [1]
							Bandwidth = elems[2]
							ip_addr = elems[3]
						print(ssid_banner)
					#doesn't work #soon + no hidden network scanning yet
				except InternalError:
					sys.exit(err_msg)
			def port_scan():
				#using nmap to scan networks && Open ports. 
				try:
					scan = os.system("nmap -A {prvaddrsrc}-255 ")
				except InternalError:
					sys.exit(err_msg)
					
			def sniff():
				pass #use socket to listen to data
			def wpa2_hs():
				pass # detect security type from network list, then use function for appropriate security type (ex : wep = wordlist,
				     # wpa2 = handshake cracking)
				def wep():
					pass
				def wpa2():
					pass
				def wpa3():
					pass
				def eap_pwd():
					pass
			def bg_record(playing = False):
				#first configure voip server, then
				while not bg_record == True:
					pass #toggles audio recording on bounded phone.
				     	     #in order to listen to real time audio, we need to configure voip /cloud server to send audio to the computer.
			if choice == 1:
				scan()
			elif choice == 2:
				port_scan()
			elif choice == 3:
				sniff()
			elif choice== 4:
				wpa2_hs()
		 	elif choice == 5:
				bg_record()
			elif choice == 6:
				sleep(1)
				sys.exit(bye_msg)
	except KeyboardInterrupt:
		sleep(1)
		sys.exit(bye_msg)

if __name__ == '__main__':
	home()

