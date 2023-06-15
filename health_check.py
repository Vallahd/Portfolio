#!/usr/bin/env python3

# Beep boop I am Pr00t

# Imports
# -------
import psutil
import socket
import emails

# Things it should do:
# (DONE) Report error if CPU usage is over 80%: psutil.cpu_percent(interval=None, percpu=True)
# (DONE) Report error if available disk space is below 20%: usage = psutil.disk_usage(path)
# (DONE) Report error if available memory is less than 500MB: mem = psutil.virtual_memory(), look at available, Threshold 500 * 1024 * 1024
# (DONE) Report error if hostname "localhost" cannot be resolved to "127.0.0.1": Socket


def error1(sender, recipient):
	subject = "Error-CPU usage is over 80%"
	body = "Please check your system and resolve the issue as soon as possible."
	attachment_path = ""
	emails.generate(sender, recipient, subject, body, attachment_path)


def error2(sender, recipient):
	subject = "Error-Available disk space is less than 20%"
	body = "Please check your system and resolve the issue as soon as possible."
	attachment_path = ""
	emails.generate(sender, recipient, subject, body, attachment_path)


def error3(sender, recipient):
	subject = "Error-Available memory is less than 500MB"
	body = "Please check your system and resolve the issue as soon as possible."
	attachment_path = ""
	emails.generate(sender, recipient, subject, body, attachment_path)


def error4(sender, recipient):
	subject = "Error-localhost cannot be resolved to 127.0.0.1"
	body = "Please check your system and resolve the issue as soon as possible."
	attachment_path = ""
	emails.generate(sender, recipient, subject, body, attachment_path)


def main():
	sender = "automation@example.com"
	recipient = "username@example.com"
	# Check error 1
	p = psutil.cpu_percent(interval=1, percpu=True)
	for item in p:
		if item >= 80:
			error1(sender, recipient)

	# Check error 2
	disks = psutil.disk_partitions()
	for line in disks:
		disk = line.mountpoint	
		d = psutil.disk_usage(disk)
		if d.percent >= 80:
			error2(sender, recipient)

	# Check error 3
	mem = psutil.virtual_memory()
	Threshold = 500 * 1024 * 1024
	if mem.available <= Threshold:
		error3(sender, recipient)

	# Check error 4
	hostname=socket.gethostname()
	IPAddr=socket.gethostbyname(hostname)
	if hostname == "localhost":
		if IPAddr != "127.0.0.1":
			error4(sender, recipient)

if __name__ == "__main__":
	main()
# Libraries like shutil and psutil should be used
# In event of an error, send a custom email to user
# Runs every 60 seconds via cron job!