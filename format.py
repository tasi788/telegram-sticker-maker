from glob import glob
import os
from os.path import splitext, getsize
from PIL import Image

#jpglist = glob( "stickers@2x/*.[jJ][pP][gG]" )
pnglist = glob( "*.[pP][nN][gG]" )

os.system('cd stickers@2x && rm *_key@2x.png *.meta tab*')
for png in pnglist:
	im = Image.open(png)
	png = splitext(png)[0]+".png"
	im.thumbnail( (512,512) )
	im.save(png)
	print png
	if 	os.path.getsize(png) > 350000:
		im = Image.open(png)
		im.thumbnail( (512,512) )
		im.save(jpg, quality=80)
		im = Image.open(jpg)
		im.save(png)
		print 'big except'
