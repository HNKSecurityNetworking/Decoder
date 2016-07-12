#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import base64

class base():
	def encodebase(encoder): #Function for encoder for all base's
		encoder =encoder.encode("utf-8")
		Encoders = {}
		Encoders["Base64"]    = str(base64.b64encode(encoder), "utf-8")
		Encoders["Base32"]    = str(base64.b32encode(encoder), "utf-8")
		Encoders["a85encode"] = str(base64.a85encode(encoder), "utf-8")
		Encoders["b16encode"] = str(base64.b16encode(encoder), "utf-8")
		return Encoders
	def decodebase(encoder): #Functions for decode for all base's
		decode = {} 
		try: 
			decode["Base64"] = str(base64.b64decode(encoder), "utf-8")
		except:
			decode["Base64"] = "Not is Base64"
		try:
			decode["Base32"] = str(base64.b32decode(encoder), "utf-8")
		except:
			decode["Base31"] = "Not is Base32"
		try:
			decode["Base16"] = str(base64.b16decode(encoder), "utf-8")
		except:
			decode["Base16"] = "Not is Base16"
		try:
			decode["a85"] = str(base64.a85decode(encoder), "utf-8")
		except:
			decode["a85"] = "Not is a85"
		return decode