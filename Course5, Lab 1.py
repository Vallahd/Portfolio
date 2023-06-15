#! /usr/bin/env python3

from PIL import Image
import os
import re

# .jpeg format, 128x128, rotated 90 degrees from a batch.

directory = '/home/student-01-bfbb550013fd/images'


for filename in os.listdir(directory):
	if filename.startswith("ic"):
		f = os.path.join(directory, filename)
		if os.path.isfile(f):
			im = Image.open(f, "r", None)
			rgb_im = im.convert('RGB')
			rgb_im.rotate(90).resize((128,128)).save("/opt/icons/" + filename, 'JPEG')



