#!/usr/bin/python
# -*- coding: utf-8 -*-

#Messages de Pyphone

def msgs(indice):
	below_msg = """\n033[1;31m[‖PyPhone : penetration testing tool that allows you to execute scripts directly on your phone ! @Nathan Raymond \n\033[1;31m["""
	bye_msg = "\n\033[1;31mShutting down... Goodbye ! ( ^_^)/ \n\033[1;31m"
	root_msg = "\n\033[1;31mPyPhone should be ran as root !\n\033[1;31m"
	err_msg = "\n\033[1;31mError ! Something went wrong !\n\033[1;31m"
	Messages = [below_msg, bye_msg, root_msg, err_msg]
	return Messages[indice]