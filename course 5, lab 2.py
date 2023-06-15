#! /usr/bin/env python3

import os
import requests
import re

directory = "/media/General/Programming/test_directory/"




for filename in os.listdir(directory):
	if filename.endswith('.txt'):
		f = os.path.join(directory, filename)
		if os.path.isfile(f):
			with open(f, 'r') as file:
				
				a = 0
				b = 0
				c = 0
				d = 1

				dict1 = {
					'title': '',
					'name': '',
					'date':	'',
					'feedback': '',
				}	

				for line in file:
					line.split('\n')
					if a == 0:
						dict1['title'] = line.replace('\n', '')
						a += 1
					elif b == 0:
						dict1['name'] = line.replace('\n', '')
						b += 1
					elif c == 0:
						dict1['date'] = line.replace('\n', '')
						c += 1
						d = 0
					elif d == 0:
						dict1['feedback'] += line.strip()
				#print(dict1)

				requests.post("http://69.231.84.249/feedback", dict1)
				response.raise_for_status()