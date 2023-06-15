#!/usr/bin/env python3

import re
import operator
import csv

dict1 = {}
dict2 = {}
dict3 = {}

# Modules imported and dictionaries initialized.

with open('syslog.log', 'r') as syslog:
	#Reading from syslog.log and iterating through each entry.
	for line in syslog:
	    thing = re.search(r"ticky: ([A-Z]*):? ([\w' ]*)(\[#[0-9]*\])? \(([\w.-_ ]*)\)", line)
	    # Regex line broken into 4 parts:
	    # Thing 1: Error type.
	    # Thing 2: Message Contents.
	    # Thing 3: Info Log Number.
	    # Thing 4: Username.
	    if thing.group(1) == "INFO":
	        if thing.group(4) not in dict2:
	            dict2.setdefault(thing.group(4), [])
	        dict2.setdefault(thing.group(4), []).append("INFO")
	    # INFO section, countes towards Dict2 and catalogues users who created an INFO message.

	    if thing.group(1) == "ERROR":
	        if thing.group(2) not in dict1:
	            dict1[thing.group(2)] = 0
	        dict1.setdefault(thing.group(2), 0)
 	        dict1[thing.group(2)] += 1
	        if thing.group(4) not in dict2:
	            dict2.setdefault(thing.group(4), [])
	        dict2.setdefault(thing.group(4), []).append("ERROR")
	    # ERROR section, counts towards Dict1 and Dict2. First part catalogues error messages and counts how many. 
	    # Second catalogues users who greated an ERROR message.

for user, types in dict2.items():
    counter1 = 0
    counter2 = 0
    for message_type in types:
        if message_type == "INFO":
            counter1 +=1
        if message_type == "ERROR":
            counter2 += 1
    dict3.setdefault(user, []).append(counter1)
    dict3.setdefault(user, []).append(counter2)  
    # This segment iterages through Dict2 and creates counts based on number of ERROR and 
    # INFO messages associated with their Username and saves them to Dict3.  

dict1 = [{'Error':key, 'Count':value} for key, value in sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)]
with open('error_message.csv', mode='w') as csv_file:
    fieldnames = ['Error', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict1)
    # This segment sorts Dict1 according to error count and writes it to a CSV file named error_message.csv.
csvData = ['Username, INFO, ERROR']

for col1, (col2, col3) in sorted(dict3.items(), key=operator.itemgetter(0)):
    csvData.append("%s, %s, %s" % (col1, col2, col3))
with open('user_statistics.csv', mode='w') as csv_file:
    csv_file.write("\n".join(csvData))
    # This segment sorts Dict3 according to Username alphabetical order and writes it to a CSV file named user_statistics.csv.