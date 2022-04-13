#!/usr/bin/python
# -*- coding: utf-8 -*-

from banners import computer_conf, box_lenght, lines_box
from headers import rand_header
from messages import msgs
import os, sys, random, platforms, subprocess
from time import sleep

#supported devices bg function
supported_devices = "Linux", "Windows", "Darwin"

#check user privileges
if not os.geteuid() == 0:
	sys.exit(msgs(-1))

#main function
def main():
	try:
		def network__conf():
			#configure the network first, assuming user is connected to internet
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
		network__conf()

		def interface():
			#display the main interface
			print(rand_header())
			print("\n")
			print(msgs(0))
			print(lines_box(-1))
			print("\n")
			for chars in msgs(1):
				sys.stdout.write(chars)
				sys.stdout.flush()
				if chars !="\n":
					sleep(0.05)
				else:
					sleep(1)
			print(lines_box(-1))
			print(computer_conf)
			print(box_lenght(len(sys.stdout())))
		interface()

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
				sleep(0.2)
				print("""
					 1) Aggressive scan
					 2) Stealth scan
					 3) Quick scan
					 4) Firewall evasion & MTU""")
				choice = raw_input(">>> ")
				if choice == 1:
					scan = os.system(f"nmap -A {prvaddrsrc}-255 -vv | grep -i 'Scan report for' 'Host is up'>> scan.txt ")
					path = os.getcwd()
					os.system(f"{path}/scan")
					print(f"Scan report will be sent to {path}.") 
				elif choice ==2:
					scan = os.system(f"nmap -Pn {prvaddrsrc}-255 -vv | grep -i 'Scan report for' 'Host is up'>> scan.txt ")
				elif choice ==3:
					scan = os.system(f"nmap -F {prvaddrsrc}-255 -vv | grep -i 'Scan report for' 'Host is up'>> scan.txt ")
				elif choice ==4:
					pass
					#implementation soon

			def sniff():
				pass #use socket to sniff data
			def wifi_cracking(network_list):
				for networks in network_list:
					for security in network_list:
						if security == "WEP":
							pass
						elif security == "WPA2":
							pass
						elif security == "WPA3":
							pass
						else:
							sys.exit(msgs(-1))
						# detect security type from network list, then use function for appropriate security type
				def wep():
					pass
				def wpa2():
					pass
				def wpa3():
					pass
			def bg_record():
				if platform.system() not in supported_devices:
					sys.exit(err_msg)
					try:
						class voIP:
							def __init__(self, audio, running = False):
								pass
								#then configure voip server (over ngrok ??) --listener / sender
								#return true or false according to connectivity of voip server
							def voIP functions(self):
								pass #**

							def run(self):
								try:
									pass
								except KeyboardInterrupt:
									sys.exit(msgs(1))


							run()
					except InternalError:
						sys.exit(err_msg)
					
					while not voip_conf() == False:
						path = os.getcwd()
						#send mp3 file in /audio file
						#check if audio file exists
						#if not create one
						pass
					    #toggles microphone on bounded phone from (recording app). Send data live through the voip server, might need rooted phone to do this.
					    #display just the "audio_msg" variable , while only waiting for user interrupting with ctrl+c or error with phone
					    #when ctrl+c pressed or connection ends, send the recorded audio as a file in the current active path.

		def options():
			print("""	 
					 1) Scan nearby networks
					 2) Port scanner
					 3) Sniff data
					 4) Wifi cracker 
					 5) Start background-audio recording (phone ==> computer)
					 6) Exit\n""")

			choice = raw_input(">>> ")
			if choice == 1:
				scan()
			elif choice == 2:
				port_scan()
			elif choice == 3:
				sniff()
			elif choice== 4:
				wifi_cracking()
		 	elif choice == 5:
				bg_record()
			elif choice == 6:
				sleep(1)
				sys.exit(msgs[2])

	except KeyboardInterrupt:
		sleep(0.5)
		sys.exit(msgs[2])
if __name__ == "__main__":
	main()
