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
	ori_w , ori_h = im.size
	if ori_w + ori_h <= 1024:
		if ori_w < ori_h:
			new = 512/float(ori_h)
			new_w = int(new*ori_w+0.5)
			new_h = int(new*ori_h+0.5)
			im.resize((new_w,new_h)).save(png)
		else:
			new = 512/float(ori_w)
			new_w = int(new*ori_w+0.5)
			new_h = int(new*ori_h+0.5)
			im.resize((new_w,new_h)).save(png)
	else:
		if ori_w > ori_h:
			new = ori_w/float(512)
			new_w = int(ori_w/new+0.5)
			new_h = int(ori_h/new+0.5)
			im.resize((new_w,new_h)).save(png)
		else:
			new = ori_h/float(512)
			new_w = int(ori_w/new+0.5)
			new_h = int(ori_h/new+0.5)
			im.resize((new_w,new_h)).save(png)
			print png

for png in pnglist:
	if 	os.path.getsize(png) > 350000:
		im = Image.open(png)
		print 'too big'
