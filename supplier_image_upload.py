#!/usr/bin/env python3 

# Beep boop I am Pr00t

# Imports
# --------
import requests
import os
import re

directory = "/home/student-01-17eb3d4a3511/supplier-data/images/"
url = "http://34.27.74.150/upload/"
### COMPLETE URL AND DIRECTORY ###

for filename in os.listdir(directory):
	if filename.endswith(".jpeg"):
		f = os.path.join(directory, filename)
		if os.path.isfile(f):
			with open(f, 'rb') as opened:
				r = requests.post(url, files={'file': opened})

# Updated, works in lab