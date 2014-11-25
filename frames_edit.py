# crop, grayscale, enhance and resize video frames in a given folder
# replaces original files

import os
import ImageEnhance
from PIL import Image
from PIL import ImageFilter

rootdir = '/home/cdathuraliya/usjp_project/tests/data_ready'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # print "Converting file " + os.path.join(subdir, file)
        im = Image.open(os.path.join(subdir, file))
        outfile = os.path.join(subdir, file)

        im = im.crop((130, 50, 510, 430))
        im = im.convert('LA')
        bright = ImageEnhance.Brightness(im)
        im = bright.enhance(1.7)
        contr = ImageEnhance.Contrast(im)
        im = contr.enhance(1.1)

        width = 128
        height = 128
        im = im.resize((width, height), Image.ANTIALIAS)
        
        im.save(outfile, "PNG")
