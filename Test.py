#!/usr/bin/env python3

import re
import operator
import csv

## Thing[1] = Message Type
## Thing[2] = Message Contents
## Thing[3] = Log Number
## Thing[4] = Username
## Dict1 = ERROR report
## Dict2 = User list
## Example 1: May 27 11:45:40 ubuntu.local ticky: INFO:  Created ticket [#1234] (username)
## Example 2: Jun  1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)
syslog = ["Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)", "Jan 31 00:09:39 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)", "Jan 31 00:09:39 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)", "Jan 31 00:09:39 ubuntu.local ticky: INFO Commented on ticket [#6518] (rr.robinson)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mcintosh)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mdouglas)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Timeout while retrieving information (oren)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Ticket doesn't exist (blossom)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR The ticket was modified while updating (bpacheco)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mcintosh)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mdouglas)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (oren)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (oren)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (sri)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (noel)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (breee)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (ahmed.miller)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (nonummy)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (noel)", "Jan 31 00:09:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (blossom)"]
## Total logs: 27. 4 INFO, 23 ERROR. 
## 5 ERROR types.
## 14 Users.

#get syslog


dict1 = {}
dict2 = {}
for line in syslog:#.split():
    thing = re.search(r"ticky: ([A-Z]*):? ([\w' ]*)(\[#[0-9]*\])? \(([\w.-_ ]*)\)", line)
    print("Thing 1 is: {}".format(thing[1]))
    print("Thing 2 is: {}".format(thing[2]))
    print("Thing 3 is: {}".format(thing[3]))
    print("Thing 4 is: {}".format(thing[4]))
    print("---BREAK---")
    if thing[1] == "INFO":
        if thing[4] not in dict2:
            dict2.setdefault(thing[4], [])
        #for thing[4] in dict2.items():
        dict2.setdefault(thing[4], []).append("INFO")
            #dict2[thing[4]] += "INFO, "

    if thing[1] == "ERROR":
        #username = thing[4]
        #message = thing[2]
        if thing[2] not in dict1:
            dict1[thing[2]] = 0
        #for message in dict1:
        dict1.setdefault(thing[2], 0)
        dict1[thing[2]] += 1
        if thing[4] not in dict2:
            dict2.setdefault(thing[4], [])
        #for username in dict2.items():
        dict2.setdefault(thing[4], []).append("ERROR")
            #dict2[thing[4]] += "ERROR, "

print(dict1)
print(dict2)

print("------------------------------------------------BREAK------------------------------------------------")

#dict3 = {}


print(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True))


dict3 = {}

for user, types in dict2.items():
    counter1 = 0
    counter2 = 0
    for message_type in types:
        if message_type == "INFO":
            counter1 +=1
            #dict3.setdefault(user, []).append(counter1)
        if message_type == "ERROR":
            counter2 += 1
            #dict3.setdefault(user, []).append(counter2)
    dict3.setdefault(user, []).append(counter1)
    dict3.setdefault(user, []).append(counter2)    
        #dict3.setdefault(user, []).extend(counter1, counter2)


#for user in dict2.items():
#    count1 = user.count("ERROR")
#    count2 = user.count("INFO")
#    dict3.setdefault(key, []).append(count1, count2)
print(sorted(dict3.items(), key=operator.itemgetter(0)))

dict1 = [{'Error Message':key, 'Count':value} for key, value in sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)]
with open('csvfile1.csv', mode='w') as csv_file:
    fieldnames = ['Error Message', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict1)

#dict3 = [{'username':key, 'info':value, 'error':value} for key, value in sorted(dict3.items(), key=operator.itemgetter(0))]
#with open('csvfile2.csv', mode='w') as csv_file:
#    fieldnames = ['username', 'info', 'error']
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#    writer.writeheader()
#    writer.writerows(dict3)
csvData = ['Username, Info, Error']

for col1, (col2, col3) in sorted(dict3.items(), key=operator.itemgetter(0)):
    csvData.append("%s, %s, %s" % (col1, col2, col3))
with open('csvfile2.csv', mode='w') as csv_file:
#    fieldnames = ['username', 'info', 'error']
#    writer = csv.writer(csv_file, fieldnames=fieldnames)
#    writer.writeheader()
#    writer.writerows(csvData)
    csv_file.write("\n".join(csvData))
#with open('csvfile2.csv', 'w') as f:
#    for key in sorted(dict3.items(), key=operator.itemgetter(0)):
#        f.write("%s,%s\n"%(key,dict3[key]))
print("---------------------")
print(' ')
print("---------------------")
print(dict2.items())

## Tried to add information to closed ticket = 16
## Ticket doesn't exist = 2
## The ticket was modified while updating = 2
## Timeout while retrieving information = 2
## Permission denied while closing ticket = 1

## mdouglas: INFO, ERROR, ERROR
## noel: INFO ERROR, ERROR
## breee: ERROR, ERROR
## ac: ERROR
## blossom: INFO, ERROR, ERROR
## rr.robinson: INFO
## mcintosh: ERROR, ERROR
## jackowens: ERROR, ERROR, ERROR
## oren: ERROR, ERROR, ERROR
## xlg: ERROR
## ahmed.miller: ERROR, ERROR
## bpacheco: ERROR
## sci: ERROR
## nonummy: ERROR

        
