#!/usr/bin/env python3

# Beep boop I am Pr00t

# Imports
# --------
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import reportlab

def generate(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (0,0), -1, colors.black),
                ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'LEFT')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])


# Create a pdf named processed.pdf using generate_report
# Module for data, need to be modular