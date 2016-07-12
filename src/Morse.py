#!/usr/bin/env python 
#_*_ coding:utf-8 _*_

Morse = {
   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..','E': '.', 'F': '..-.',   
   'G': '--.', 'H': '....', 'I': '..', 'J': '.---','K': '-.-', 'L': '.-..',
   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
   '0': '-----','=':'-...-', '.-.-':'~', '\'': '.----.', '$': '...-..-', '(':'-.--.',
   ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-', '/': '-..-.', ':': '---...',
   ';': '-.-.-.', '?': '..--..', '_': '..--.-',
   '@': '.--.-.', '!': '-.-.--'
    }
class morse():
	def decode(morse):
		global Morse
		decode = ""
		rep = morse.replace("/", "xz").split(" ")
		for i in rep:
			if i == "xz":
				decode += " "
			else:
				for key, value in Morse.items():
					if i == value:
						decode += key
		return decode

	def encode(morse):
		global Morse
		decode = ""
		rep = list(morse.replace(" ", "|").upper())
		for i in rep:
			if i == "|":
				decode += "/ "
			for key, value in Morse.items():
				if i == key:
					decode +=value+" "
		return decode
