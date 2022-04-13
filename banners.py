#!/usr/bin/python
# -*- coding: utf-8 -*-

#Bannières de PyPhone
import random

def lines_box(indice):
	line_separator = """°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸"""
	line_variable = f"""▬▬ι═══════ﺤ{variable}-═══════ι▬▬"""
	lines = [line_variable, line_separator]
	return lines[indice]

def computer_conf():
	global hostname
	global cpu
	global operating_system
	global version
	hostname = platform.node()
	cpu = platform.processor()
	operating_system = platform.system()
	version = platform.version()
	variable = "Your computer's configuration : "
	print(lines_box(1))
	print(f"Hostname : {hostname}\nCPU : {cpu}\n Operating System : {operating_system}\nVersion : {version}\n")

def box_lenght(lenght):
	box_config =f"▬"
	return box_config*len(lenght)
