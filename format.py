from glob import glob
import os
from os.path import splitext, getsize
from PIL import Image

os.system('cd stickers@2x && find . \! -name "*.png" -delete && rm *_key@2x.png tab*')
#jpglist = glob( "stickers@2x/*.[jJ][pP][gG]" )
pnglist = glob( "stickers@2x/*.[pP][nN][gG]" )
jpglist = glob( "stickers@2x/*.[jJ][pP][gG]" )
for png in pnglist:
	im = Image.open(png)
	png = splitext(png)[0]+".png"
	#resize((512,443),Image.ANTIALIAS).save('new.png')
	ori_w , ori_h = im.size
	if ori_w + ori_h <= 1024:
		if ori_w < ori_h:
			new = 512/float(ori_h)
			new_w = int(new*ori_w+0.5)
			new_h = int(new*ori_h+0.5)
			im.convert('RGBA').resize((new_w,new_h),Image.ANTIALIAS).save(png)
			print png
		else:
			new = 512/float(ori_w)
			new_w = int(new*ori_w+0.5)
			new_h = int(new*ori_h+0.5)
			im.convert('RGBA').resize((new_w,new_h),Image.ANTIALIAS).save(png)
			print png
	else:
		if ori_w > ori_h:
			new = ori_w/float(512)
			new_w = int(ori_w/new+0.5)
			new_h = int(ori_h/new+0.5)
			im.convert('RGBA').resize((new_w,new_h),Image.ANTIALIAS).save(png)
			print png
		else:
			new = ori_h/float(512)
			new_w = int(ori_w/new+0.5)
			new_h = int(ori_h/new+0.5)
			im.convert('RGBA').resize((new_w,new_h),Image.ANTIALIAS).save(png)
			#png = splitext(jpg)[0]+".png"
			print png
	if 	os.path.getsize(png) > 350000:
		qua = 90
		for x in range(8):
			jpg = splitext(png)[0]+".jpg"
			im = Image.open(png)
			im.save(jpg, quality=qua)
			im = Image.open(jpg)
			im.save(png)
			qua -= x*10
			print str(qua)
			if 	os.path.getsize(png) <= 350000:
				os.system('rm stickers@2x/*.jpg')
				print 'big except'
