#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from factory import VideoFactory

class Bilibili(VideoFactory):
	def __init__(self):
		super(Bilibili, self).__init__()
		self.define_node()
		self._videos = None

	def define_node(self):
		self._video = {'site': ['', r"^Video\sSite:\s+(.+)$"],
				'title': ['', r"^Title:\s+(.+)$"],
				'vformat': ['',  r"^Type:\s+(.+)$"],
				'size': ['', r"^Size:\s+(.+)$"], 
				#'furls': ['', r"^Real URLs:\s+(.+)$"],
				'furls': ['', r"^Real URLs?:\s*(.+)$"],
				'ftype': ['vformat', ''], # default value
				'quality': ['vformat', '']} # default value
	def attach(self, videos):
		import copy
		self._videos = copy.copy(videos)
#'''
#	# 修改doc
#	def modify_doc(self, doc):
#		def getpalyid(url):
#			import re
#			regex = r'.+bilibili\.com/video/av([\d]+)'
#			return ''.join(re.findall(regex, url))
#
#		# 获取弹幕链接
#		playurl = self._playurl
#		playid = getplayid(playurl)	
#		comment_url = "http://comment.bilibili.com/%s.xml" % playid
#		
#		# 获取弹幕文件名
#		videos = self._videos
#		for video in videos:  # B站的 video 只有一个
#			# 获取弹幕文件名
#			barrage_file = ''.join(video['title'][0] + '.cmt.xml')
#'''
	# 此时 to_xml 已经返回
	def post_proc(self, buff):
		import os
		for video in self._videos: # B站的 video 只有一个
			# 获取弹幕文件名
			barrage_file = ''.join(video['title'][0] + '.cmt.xml')
			#先在当前程序目录查找 barrage_file
			if os.path.isfile(barrage_file):
				#读取barrage_file 文本 to file_buff
				import sys
				if sys.platform[:5] != 'win32': # windows 平台有 bug, 尚未解决
					cmt_file = open(barrage_file, 'r')
				else:
					cmt_file = open(barrage_file, 'r', encoding="utf8")
					if cmt_file:
						file_buff = cmt_file.read()
						cmt_file.close()
						#file_buff 中去除 '<?xml version="1.0" encoding="UTF-8"?>'
						file_buff = file_buff.replace('<?xml version="1.0" encoding="UTF-8"?>', "")
						file_buff = "<barrage>" + file_buff + "</barrage></video></root>"

						#在 buff 中的最后， 即'</video></root>' 之前插入 file_buff
						buff = buff.replace('</video></root>', file_buff)
				try: os.remove(barrage_file)
				except: pass
				
			else:
				import sys
				if sys.platform[:5] == 'win32':
					os.system('delete *.cmt.xml')
				else:
					os.system('rm *.cmt.xml -f')
		return buff
