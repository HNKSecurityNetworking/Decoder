#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#Libraries
import os 
import sys
import base64
import argparse


def Main(): #Function main
	System()
	Banner()
	Arguments()

class Colors: #function for colors
	Red   = "\033[0;31m"
	Green = "\033[0;32m"
	White = "\033[1;37m"
	End   = "\033[0m"

def System(): #function to get system information
	if sys.platform in ['linux', 'linux2']:
		os.system("clear")
	else:
		os.system("cls")
		Colors.Red   = ""
		Colors.Green = ""
		Colors.End   = ""

def Banner():
	print(Colors.Red+"""
			██╗  ██╗███╗   ██╗██╗  ██╗
   			██║  ██║████╗  ██║██║ ██╔╝
   			███████║██╔██╗ ██║█████╔╝ 
   			██╔══██║██║╚██╗██║██╔═██╗ 
   			██║  ██║██║ ╚████║██║  ██╗
   			╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝"""+Colors.End)
	print(Colors.Green+"\t\t\t  HNK Security Network"+Colors.End)

def Arguments(): #function to get the arguments
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument("--all", action="store_true", dest="all", required=False, help="Select all options.")
	parser.add_argument("--e", action="store", dest="e", required=False, help="Encode all options.")
	parser.add_argument("--d", action="store", dest="d", required=False, help="Decode all options.")
	args = parser.parse_args()
	if args.e and args.all:
		EncodeBaseAll(bytes(args.e, "utf-8"))
	else:
		print("Use algum argumento xD")

def EncodeBaseAll(encoder): #Function for encoder for base64
	Encoders = {}
	Encoders["Base64"]    = str(base64.b64encode(encoder), "utf-8")
	Encoders["Base32"]    = str(base64.b32encode(encoder), "utf-8")
	Encoders["a85encode"] = str(base64.a85encode(encoder), "utf-8")
	Encoders["b16encode"] = str(base64.b16encode(encoder), "utf-8")
	for i in Encoders:
		print(Colors.White+i+" Encode: "+Colors.Green+Encoders[i]+Colors.End)
Main()
