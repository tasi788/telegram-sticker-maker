from glob import glob
import os
from os.path import splitext, getsize
from PIL import Image

jpglist = glob( "*.[jJ][pP][gG]" )
pnglist = glob( "*.[pP][nN][gG]" )
num = 0
for jpg in jpglist:
	im = Image.open(jpg)
	ori_w , ori_h = im.size
	print str(ori_w)+','+str(ori_h)
	if ori_w + ori_h <= 1024:
		if ori_w < ori_h:
			new_w = 512/ori_h
		else:
			new_h = 512/ori_w
	else:
		if ori_w > ori_h:
			new_w = ori_w/512
		else:
			new_h = ori_h/512
	num += 1
	png = str(num) + '.png'
	#png = splitext(jpg)[0]+".png"
	im.save(png)
	print png

for png in pnglist:
	if 	os.path.getsize(png) > 350000:
		im = Image.open(png)
