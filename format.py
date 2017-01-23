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
	ori_w , ori_h = im.size
	if ori_w + ori_h <= 1024:
		if ori_w < ori_h:
			new = 512/float(ori_h)
			new_w = new*ori_w
			new_h = new*ori_h
			im.resize((new_w,new_h)).save(png)
		else:
			new = 512/float(ori_w)
			new_w = new*ori_w
			new_h = new*ori_h
			im.resize((new_w,new_h)).save(png)
	else:
		if ori_w > ori_h:
			new = ori_w/float(512)
			new_w = ori_w/new
			new_h = ori_h/new
			im.resize((new_w,new_h)).save(png)
		else:
			new = ori_h/float(512)
			new_w = ori_w/new
			new_h = ori_h/new
			im.resize((new_w,new_h)).save(png)
			#png = splitext(jpg)[0]+".png"
			print png
	if 	os.path.getsize(png) > 350000:
		im = Image.open(png)
		im.thumbnail( (512,512) )
		im.save(jpg, quality=80)
		im = Image.open(jpg)
		im.save(png)
		print 'big except'
