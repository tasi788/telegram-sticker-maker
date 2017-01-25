#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import sys
import time
import random
import datetime
import telepot
import uniout
import pprint
import urlparse
import urllib
import zipfile
from glob import glob
from pytg import Telegram
from pytg.sender import Sender
from pytg.receiver import Receiver
from pyquery import PyQuery as pq
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read('apitoken.txt')
receiver = Receiver(host="localhost", port=4458)
sender = Sender(host="localhost", port=4458)

#定義telegram各項參數
def handle(msg):
	#pprint.pprint(msg)
	content_type, chat_type, chat_id = telepot.glance(msg)
	chat_id = msg['chat']['id']
	message_id = msg['message_id']
	try:
		username = msg['from']['first_name'] +' '+ msg['from']['last_name']
	except:
		username = msg['from']['first_name']
	user_id = msg['from']['id']
	url = 'http://dl.stickershop.line.naver.jp/products/0/0/1/replace/iphone/stickers@2x.zip'

#https://line.me/S/sticker/7834
#zh-Hant
	#接收文字訊息回應
	if content_type == 'text':
		command = msg['text'].lower()
		content = str(username.encode('utf-8'))+'('+str(user_id)+')'+'說：'+str(command.encode('utf-8'))
		if 'https://line.me' in command:
			try:
				sticker_id = str(command.split('\n')[1].split('/')[-1])
			except:
				sticker_id = str(command.split('/')[-1])
			urllib.urlretrieve (url.replace('replace',sticker_id),sticker_id+'.zip')
			bot.sendMessage(chat_id, '下載完畢')
			url = 'https://store.line.me/stickershop/product/id/zh-Hant'
			q = pq(url=url.replace('id',sticker_id))
			packname = q('h3').filter('.mdCMN08Ttl').text()
			bot.sendMessage(chat_id,packname.encode('utf-8'))
			zip_ref = zipfile.ZipFile(sticker_id+'.zip', 'r')
			zip_ref.extractall('stickers@2x.zip')
			zip_ref.close()
			os.system('rm *.zip')
			os.system('python format.py')
			pnglist = glob( 'stickers@2x/*.[pP][nN][gG]' )
			sender.send_msg('Stickers', u'/newpack')
			sender.send_msg('Stickers', packname)
			pnglist = glob( "stickers@2x/*.[pP][nN][gG]" )
			for png in pnglist:
				print png
				sender.send_document('Stickers', png)
				sender.send_msg('Stickers', u'🔗')

		else:
			bot.sendMessage(chat_id,'QQ')
	#接收圖片顯示圖片id
	elif content_type == 'photo':
			#取出原始尺寸圖片file_id
			a = msg['photo']
			max=0
			for i in range(1,len(a)):
			   if a[i]['width']>a[max]['width']:
				  max=i
			max_file_id=a[max]['file_id']
			content = str(username.encode('utf-8'))+'('+str(user_id)+')傳送圖片 \n'+str(max_file_id)
	#接收貼圖
	elif content_type == 'sticker':
		content = str(username.encode('utf-8'))+'('+str(user_id)+')傳送貼圖 \n'+str(msg['sticker']['file_id'])
	#接收檔案
	elif content_type == 'document':
		content = str(username.encode('utf-8'))+'('+str(user_id)+')傳送檔案 \n'+str(msg['document']['file_name'])+'\n'+str(msg['document']['file_id'])
	#接收位置
	elif content_type == 'location':
		content = str(username.encode('utf-8'))+'('+str(user_id)+')傳送位置 \n'+str(msg['location']['latitude'])+','+str(msg['location']['longitude'])

	elif content_type == 'voice':
		content = str(username.encode('utf-8'))+'('+str(user_id)+')傳送聲音 \n'+str(msg['voice']['file_id'])

	#log定義
	log = '['+str(time.strftime("%Y-%m-%d %I:%M:%S"))+'] '+content+'\n'
	#寫入txt
	f = open('log.txt', 'a')
	f.write(log)
	print log
	f.close()

#登入資訊
bot_apitoken = parser.get('apitoken', 'token')
bot = telepot.Bot(bot_apitoken)
bot.message_loop(handle)
print '監聽中 ...'

while 1:
	time.sleep(10)
