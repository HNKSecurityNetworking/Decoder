#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#Libraries
import os 
import sys
import base64
import argparse
from sys import path
path.append("src/")
from Morse import morse 
from base import base
from time import sleep

class Colors: #function for colors
	Red   = "\033[0;31m"
	Green = "\033[0;32m"
	White = "\033[1;37m"
	End   = "\033[0m"

banner =Colors.Red+"""
	
			██╗  ██╗███╗   ██╗██╗  ██╗
   			██║  ██║████╗  ██║██║ ██╔╝
   			███████║██╔██╗ ██║█████╔╝ 
   			██╔══██║██║╚██╗██║██╔═██╗ 
   			██║  ██║██║ ╚████║██║  ██╗
   			╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
   			   HNK Security Networking."""+Colors.End

def Banner(ban):
	for b in ban + '\n':
		sys.stdout.write(b)
		sys.stdout.flush()
		sleep(7./500)

def System(): #function to get system information
	if sys.platform in ['linux', 'linux2']:
		os.system("clear")
	else:
		os.system("cls")
		Colors.Red   = ""
		Colors.Green = ""
		Colors.End   = ""

def Arguments(): #function to get the arguments
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument("--all", action="store_true", dest="all", required=False, help="Select all options.")
	parser.add_argument("--e", action="store", dest="e", required=False, help="Encode all options.")
	parser.add_argument("--d", action="store", dest="d", required=False, help="Decode all options.")
	parser.add_argument("--m", action="store_true", dest="m", required=False, help="Select option morse.")
	parser.add_argument("--b", action="store_true", dest="b", required=False, help="Select option for all base's.")
	args = parser.parse_args()
	if args.m and args.e:
		encode = morse.encode(args.e)
		print(Colors.Green+"String: "+Colors.White+args.e)
		print(Colors.White+"Encoded:"+Colors.Green,encode)
	elif args.m and args.d:
		decode = morse.decode(args.d)
		print(Colors.Green+"Encode: "+Colors.White,args.d)
		print(Colors.White+"Decode: "+Colors.Green,decode)
	elif args.b and args.e:
		print(Colors.White+"\nString for encode: "+str(args.e)+"\n")
		dec = base.encodebase(args.e)
		for i in dec:
			print(Colors.Red,i+": "+Colors.White,dec[i])
	elif args.b and args.d:
		print(Colors.White+"\nString for decode: "+str(args.d)+"\n")
		dec = base.decodebase(args.d)
		for i in dec:
			print(Colors.Red,i+": "+Colors.White,dec[i])

def Main(): #Function main
	System()
	Banner(banner)
	Arguments()

Main()
