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
	num += 1
	png = str(num) + '.png'

	if ori_w + ori_h <= 1024:
		if ori_w < ori_h:
			new = 512/float(ori_h)
			im.resize((ori_h*new,ori_w*new)).save(png)
		else:
			new = 512/float(ori_w)
			im.resize((ori_h*new,ori_w*new)).save(png)
	else:
		if ori_w > ori_h:
			new = ori_w/float(512)
			print str(new)+'new1'
			im.resize((ori_h*new,ori_w*new)).save(png)
		else:
			new = ori_h/float(512)
			print str(new)
			im.resize((ori_h/new,ori_w/new)).save(png)
			#png = splitext(jpg)[0]+".png"
			print png

for png in pnglist:
	if 	os.path.getsize(png) > 350000:
		im = Image.open(png)
