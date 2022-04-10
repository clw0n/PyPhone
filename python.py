import os, sys, threading
from time import sleep

main_msg = """\n\033[0;35m
 _________$$$$$$$$$$
_________$_________$$
_________$_$$$$$$$_$$
_________$_$     $_$$
_________$_Python$_$$			
_________$_Termux|_$$			‖	Python Termux Script : execute scripts remotely or execute script ‖
_________$_$     $_$$           ‖   directly on your phone ! -Developped by Nathan Raymond ‖
_________$_$$$$$$$_$$ 
_________$_________$$
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

def home():
	try:
		def config0(): #configure parameters for options
			try:
				prvaddr = os.popen("ifconfig | grep broadcast | awk '{print $2}'").read()
				user = os.getlogin()
				n_mac = os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read()
				hostname = os.popen("hostname -I").read()
				netmask = os.popen("ip route show | grep 'default via' | awk '{print $3}'").read()
				prvaddr = prvaddr[:-1]
			except: ##implémenter l'erreur (aucune connection internet)
				print("\033[1;31mYou need to be connected to internet to configure your network !\033[1;31m")

		def options():
			print("""1) Scan nearby networks
					 2) Port scanner
					 3) Sniff data
					 4) WPA2 handshake cracking 
					 5) Exit""")
			choice = raw_input(">>> ")
			def scan0():
				pass
			def port_scan():
				pass
			def sniff():
				pass
			def wpa2_hs():
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
				sleep(1)
				sys.exit(bye_msg)
	except KeyboardInterrupt:
		sleep(1)
		sys.exit(bye_msg)

if __name__ == '__main__':
	home()

