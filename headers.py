#!/usr/bin/python
# -*- coding: utf-8 -*-

#Logos de PyPhone
import random


header1 = """

██▓███ ▓██   ██▓ ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████ 
▓██░  ██▒▒██  ██▒▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ 
▓██░ ██▓▒ ▒██ ██░▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███   
▒██▄█▓▒ ▒ ░ ▐██▓░▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ 
▒██▒ ░  ░ ░ ██▒▓░▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒
▒▓▒░ ░  ░  ██▒▒▒ ▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░
░▒ ░     ▓██ ░▒░ ░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░
░░       ▒ ▒ ░░  ░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░   
         ░ ░               ░  ░  ░    ░ ░           ░    ░  ░
         ░ ░                                                 """

header2 = """

██████╗ ██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  
██╔═══╝   ╚██╔╝  ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  
██║        ██║   ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗
╚═╝        ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝"""

header3 = """

▄▄▄· ▄· ▄▌ ▄▄▄· ▄ .▄       ▐ ▄ ▄▄▄ .
▐█ ▄█▐█▪██▌▐█ ▄███▪▐█▪     •█▌▐█▀▄.▀·
 ██▀·▐█▌▐█▪ ██▀·██▀▐█ ▄█▀▄ ▐█▐▐▌▐▀▀▪▄
▐█▪·• ▐█▀·.▐█▪·•██▌▐▀▐█▌.▐▌██▐█▌▐█▄▄▌
.▀     ▀ • .▀   ▀▀▀ · ▀█▄▀▪▀▀ █▪ ▀▀▀ """

header4 = """

  ▄███████▄ ▄██   ▄      ▄███████▄    ▄█    █▄     ▄██████▄  ███▄▄▄▄      ▄████████ 
  ███    ███ ███   ██▄   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███ 
  ███    ███ ███▄▄▄███   ███    ███   ███    ███   ███    ███ ███   ███   ███    █▀  
  ███    ███ ▀▀▀▀▀▀███   ███    ███  ▄███▄▄▄▄███▄▄ ███    ███ ███   ███  ▄███▄▄▄     
▀█████████▀  ▄██   ███ ▀█████████▀  ▀▀███▀▀▀▀███▀  ███    ███ ███   ███ ▀▀███▀▀▀     
  ███        ███   ███   ███          ███    ███   ███    ███ ███   ███   ███    █▄  
  ███        ███   ███   ███          ███    ███   ███    ███ ███   ███   ███    ███ 
 ▄████▀       ▀█████▀   ▄████▀        ███    █▀     ▀██████▀   ▀█   █▀    ██████████ 
                                                                                     """


def rand_header():
	headers = [header1, header2, header3, header4]
	return random.choice(headers)