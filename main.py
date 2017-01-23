#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import time
import random
import datetime
import telepot
import uniout
import pprint
import urlparse
import urllib
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read('apitoken.txt')
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
