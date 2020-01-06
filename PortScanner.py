#!/bin/python

import sys
import socket
from datetime import datetime

#Define our Target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Changing a hostname into ipv4
else:
	print("Invalid number of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Adding some fortmatting banners
print("-" * 50)
print("Scanning target " + target)
print("Time started : " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #will return an error indicator, if open result 0 else result 1 if there is an error
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldnt connect to server.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
