from glob import glob
import os
from os.path import splitext, getsize
from PIL import Image
os.system('cd stickers@2x && rm *_key@2x.png *.meta tab*')
#jpglist = glob( "stickers@2x/*.[jJ][pP][gG]" )
pnglist = glob( "stickers@2x/*.[pP][nN][gG]" )

for png in pnglist:
	im = Image.open(png)
	png = splitext(png)[0]+".png"
	ori_w , ori_h = im.size
	if ori_w + ori_h <= 1024:
		if ori_w < ori_h:
			new = 512/float(ori_h)
			new_w = int(new*ori_w+0.5)
			new_h = int(new*ori_h+0.5)
			im.resize((new_w,new_h)).save(png)
			print png
		else:
			new = 512/float(ori_w)
			new_w = int(new*ori_w+0.5)
			new_h = int(new*ori_h+0.5)
			im.resize((new_w,new_h)).save(png)
			print png
	else:
		if ori_w > ori_h:
			new = ori_w/float(512)
			new_w = int(ori_w/new+0.5)
			new_h = int(ori_h/new+0.5)
			im.resize((new_w,new_h)).save(png)
			print png
		else:
			new = ori_h/float(512)
			new_w = int(ori_w/new+0.5)
			new_h = int(ori_h/new+0.5)
			im.resize((new_w,new_h)).save(png)
			#png = splitext(jpg)[0]+".png"
			print png
	if 	os.path.getsize(png) > 350000:
		im = Image.open(png)
		im.save(jpg, quality=80)
		im = Image.open(jpg)
		im.save(png)
		print 'big except'
