import os, sys, threading, platform
from time import sleep

main_msg = """\n\033[0;35m
 _________$$$$$$$$$$
_________$_________ $$
_________$_$$$$$$$_ $$
_________$_$     $_ $$
_________$_Python$_ $$			
_________$_Termux|_ $$			‖	Python Termux Script : execute scripts remotely or execute script ‖
_________$_$     $_ $$           ‖   directly on your phone ! -Developped by Nathan Raymond ‖
_________$_$$$$$$$_ $$ 
_________$_________ $$
__________$$$$$$$$$$
_________$_________$$
________$_1__2__3_$$$
_______$_4__5__6_$$$
______$_7__8__9_$$$
_____$_*__0__#_$$$
____$_________$$$
_____$$$$$$$$$$$
______$$$$$$$$$
\033[0;35m\n"""



bye_msg = "\033[1;Shutting down... \033[1;31m"

if not os.geteuid()==0:
	sys.exit("\033[1;31m\nScript should be ran as root ! ( •̀_•́ ) \n\033[1;31m")
else:
	sleep(1)
	print(main_msg)
	print("="*len(main_msg))

def home():
	try:
		def config(): #configure parameters for options
			try:
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
			except: ##implémenter l'erreur (aucune connection internet)~~~
				print("\033[1;31mYou need to be connected to internet in order to configure your network !\033[1;31m")
		def bind_ssh(ipaddr):
			try:
				os.system("ssh root@{ipaddr}")
				print("Connected to {}")
			except ##finish later
			
			if platform.system() == "Linux" or "Windows" or "Darwin":
				print("Computer detected ! Connect phone with ssh ?")
				choice = raw_input(">>> ")
				if choice =="y" or "Y":
					ipaddr = input("Please input the phone's ip to connect with ssh. ")
					bind_ssh(ipaddr)
				elif choice =="n" or "N":
					options()
				else:
					print("033[1;31mPlease input a correct value !033[1;31m")
				
		def options():
			print("""1) Scan nearby networks
					 2) Port scanner
					 3) Sniff data
					 4) WPA2 handshake cracking 
					 5) Start background-audio recording (phone ==> computer)
					 6) Exit""")
			choice = raw_input(">>> ")
			def scan0():
				pass
			def port_scan():
				pass
			def sniff():
				pass
			def wpa2_hs():
				pass
			def bg_record():
				pass
			if choice == 1:
				scan0()
			elif choice == 2:
				port_scan()
			elif choice == 3:
				sniff()
			elif choice== 4:
				wpa2_hs()
		 	elif choice ==5:
				bg_record()
			elif choice ==6:
				sleep(1)
				sys.exit(bye_msg)
	except KeyboardInterrupt:
		sleep(1)
		sys.exit(bye_msg)

if __name__ == '__main__':
	home()

