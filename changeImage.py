#!/usr/bin/env python3

# Beep boop I am Pr00t

# Imports
# --------
from PIL import Image
import os
import re

directory = "/home/student-01-17eb3d4a3511/supplier-data/images/"
### COMPLETE DIRECTORY ###

for filename in os.listdir(directory):
        if filename.endswith(".tiff"):
                f = os.path.join(directory, filename)
                if os.path.isfile(f):
                        #name = filename.removesuffix(".TIFF")

                        outfile = f.split(".")[0] + ".jpeg"
                        im = Image.open(f)
                        out = im.convert("RGB")
                        out.resize((600,400)).save(outfile, "JPEG", quality=100)


# Supplier data directory: ~/supplier-data/images
# Final image conversion: 600x400 pixels, .JPEG type, RGB format
# Save to: ~/supplier-data/images

# Updated, works in lab