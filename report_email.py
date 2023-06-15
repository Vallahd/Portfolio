#!/usr/bin/env python3

# Beep boop I am Pr00t

# Imports
# --------
import os
from datetime import date
import datetime
import reports
import emails

#def data_conversion(data_report):
#	print(data_report)
#	data_report[2] = " "
#	return data_table
# Use created report.py module to generate pdf
# Get data from: supplier-data/descriptions
# Format: Name, weight, space (replace description with " ".?)
# Generate PDF to: '/tmp/processed.pdf'
# reports.generate_report(attachment, title, paragraph)
# Paragraph is text description processed from the text files
# Email address: <username>@example.com

def main():
	directory = "~/supplier-data/descriptions"
	report_list = []
	for filename in os.listdir(directory):
		temp = []
		if filename.endswith(".txt"):
			file = os.path.join(directory, filename)
			if os.path.isfile(file):
				with open(file) as f:
					lines = [line.rstrip() for line in f]
					lines[2] = " "
					temp.append("Name: " + lines[0])
					temp.append("Weight: " + lines[1])
					temp.append(lines[2])
					for item in temp:
						items = []
						items.append(item)
						report_list.append(items)

	today = date.today()
	time = today.strftime("%B %d, %Y")
	title = ("Processed Update on {}".format(time))
	print(title)
	data_table = report_list
	attachment = (directory + "TestPDF.pdf")
	reports.generate(attachment, title, "", data_table)

	sender = "me"
	recipient = "you"
	subject = "Report"
	body = "Y u do dis"
	attachment_path = attachment
	emails.generate(sender, recipient, subject, body, attachment_path)

if __name__== "__main__":
	main()
# Main definition, call generate_report and generate_email here 