#!/usr/bin/env python3

# Beep boop I am Pr00t

# Imports
# --------
import os
import requests
import re

test_directory = "/media/General/Programming/test_directory/"
directory = "/home/student-01-17eb3d4a3511/supplier-data/descriptions/"
url = "http://34.27.74.150/fruits"
### COMPLETE DIRECTORY AND URL ###

for filename in os.listdir(test_directory):
	if filename.endswith(".txt"):
		file = os.path.join(test_directory, filename)
		print("Processing file: ".format(filename))
		name = filename.removesuffix(".txt")
		if os.path.isfile(file):
			entry = {
			"Name": "",
			"Weight": "",
			"Description": "",
			"Image Name": "",
			}
			with open(file) as f:
				lines = [line.rstrip() for line in f]
				weight = int(lines[1].removesuffix(" lbs"))
				entry["Name"] = lines[0]
				entry["Weight"] = weight
				entry["Description"] = lines[2]
				entry["Image Name"] = name + ".jpeg"
			r = requests.post(url, data=entry)
			print("Return code: ".format(r))



# Supplier data directory: ~/supplier-data
# Subdirectories: descriptions and images
# Description fields: Name, Weight, Description, Image Name
# url = "<iP-Address>/fruits"
# Files are: 001.txt, 002.txt, etc.
# Weight needs converted from string to int, drop the lbs