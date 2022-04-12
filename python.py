import os, sys, platform, subprocess, socket
from time import sleep



#############################################################
#							    #				
#	Pyphone is a free remote penetration    	    #
#	testing tool powered by nmap. 		            #
#    							    #
#   	You can use the software and		   	    #								$*#/.°*
#	modify it as you wish.				    #					$#/.°*
#							    #				
#	How to use it :					    #			
#		pyphone [-b bind_address] [-sc]	            #					$*#/.*°
#				[-wpa (handshake)]          #
#				[-conf (reconf)]            #
#				[-sn (ipaddr)][-r record]   #
#							    #				
#############################################################

#devices supported to start VoIP server on your local machine/ Somehow figure how to connect server on localhost with phone (ngrok link maybe ?)
supported_devices = "Linux", "Windows", "Darwin"


#configure all of the messages
main_msg = """\n\033[0;35m
		       ____$$$$$$$$$$
		      ___$_________ $$
		     ____$_$$$$$$$_ $$
		    _____$_$     $_ $$
		    _____$_Python$_ $$			
		    _____$_Termux|_ $$			       
		    _____$_$     $_ $$           	  	
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

below_msg = """\n033[1;31m[‖PyPhone Script : execute scripts remotely or execute scripts-‖\n‖ directly on your phone ! -Developped by Nathan Raymond ‖\n033[1;31m["""
bye_msg = "\033[1;31mShutting down... Goodbye ! ( ^_^)/ \033[1;31m"
root_msg = "\033[1;31mPyPhone should be ran as root !\033[1;31m"
err_msg = "\033[1;31mError ! Something went wrong !\033[1;31m"

ssid_banner = f"""\033[1;31m|==============================================================|
			   
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

audio_msg = f"\n033[1;31m[Listening ━━━━⬤─────── {ipaddr}...]033[1;31m\n"
if not os.geteuid()==0:
	sys.exit(root_msg)

def home():
	try:
		print(main_msg)
		sleep(0.5)
		for chars in below_msg:
			sys.stdout.write(char)
			sys.stdout.flush()
			if char == "\n":
				sleep(1)
			else:
				sleep(0.1)
		def config(): 
			#configure the parameters for options()
			#assuming user is connected to internet. If not, any function except search_network will return an err_msg.
			global prvaddr
			global user
			global macaddr
			global hostname
			global prvaddrsrc
			prvaddr = os.popen("ifconfig | grep broadcast | awk '{print $2}'").read()
			prvaddr = prvaddr[:-1]
			user = os.getlogin()
			macaddr = os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read()
			macaddr = macaddr[:-1]
			hostname = os.popen("hostname").read()
			hostname = hostname[:-1]
			prvaddrsrc = os.popen("ip route show | tail -n1 | awk '{print $1}' | cut -f1 -d'/'").read()
			prvaddrsrc = prvaddrsrc[:-1]
			
		def bind_ssh(ipaddr):
			try:
				sleep(1)
				os.system("ssh root@{ipaddr}")
				print("Connected to device {ipaddr}")
			except ValueError:
				sys.exit(err_msg)
			
		if platform.system() == "Linux" or "Windows" or "Darwin":
			print("Connect phone with ssh ?\n")
			choice = raw_input(">>> ")
			if choice =="y" or "Y":
				ipaddr = input("Please input the phone's ip to connect with ssh : ")
				bind_ssh(ipaddr)
			elif choice =="n" or "N":
				config()
				options()
			else:
				sys.exit(err_msg)
		def options():
			print("""	 1) Scan nearby networks
					 2) Port scanner
					 3) Sniff data
					 4) Wifi cracker 
					 5) Start background-audio recording (phone ==> computer)
					 6) Exit\n""")
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
					sleep(0.2)
					print("""1) Aggressive scan
						 2) Stealth scan
						 3) Quick scan
						 4) Firewall evasion & MTU""")
					choice = raw_input(">>> ")
					if choice == 1:
						scan = os.system("nmap -A {prvaddrsrc}-255 -vv | grep -i 'Scan report for' 'Host is up'>> scan.txt ")
						path = os.path()
						print(f"Scan report will be sent to {path}.") 
					elif choice ==2:
						scan = os.system("nmap -Pn {prvaddrsrc}-255 -vv | grep -i 'Scan report for' 'Host is up'>> scan.txt ")
					elif choice ==3:
						scan = os.system("nmap -F {prvaddrsrc}-255 -vv | grep -i 'Scan report for' 'Host is up'>> scan.txt ")
					elif choice ==4:
						pass
						#implementation soon
				except InternalError:
					sys.exit(err_msg)
					
			def sniff():
				pass #use socket to sniff data
			def wifi_cracking():
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
				if platform.platform() not in supported_devices:
					sys.exit(err_msg)
					try:
						def voip_conf(audio):
							pass
							#then configure voip server (over ngrok ??) --listener / sender
							#return true or false according to connectivity of voip server
					except InternalError:
						sys.exit(err_msg)
					
					while not voip_conf() == False:
						path = os.path()
						#send mp3 file in /audio file
						#check if audio file exists
						#if not create one
						pass
					    #toggles microphone on bounded phone from (recording app). Send data live through the voip server, might need rooted phone to do this.
					    #display just the "audio_msg" variable , while only waiting for user interrupting with ctrl+c or error with phone
					    #when ctrl+c or connection ends, send the recorded audio as a file in the current path.

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

