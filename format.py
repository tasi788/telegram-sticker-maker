from glob import glob
import os
from os.path import splitext, getsize
from PIL import Image

jpglist = glob( "*.[jJ][pP][gG]" )
pnglist = glob( "*.[pP][nN][gG]" )
num = 0
for jpg in jpglist:
	im = Image.open(jpg)
	num += 1
	png = str(num) + '.png'
	im.thumbnail( (512,512) )
	im.save(png)
	print png

for png in pnglist:
	if 	os.path.getsize(png) > 350000:
		im = Image.open(png)
