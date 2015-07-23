#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from factory import VideoFactory
class Youku(VideoFactory):
	def __init__(self):
		super(Youku, self).__init__()
		self.define_node()

	#def attach(self, videos):
	#	super(Youku, self)._attach(videos)
	#	pass

	def define_node(self):
		self._video = {'site':	['', r"^site:\s+(.+)$"],
					'title':	['', r"^title:\s+(.+)$"],
					'vformat':	['',  r"^\s+-\sformat:\s+(.*)$"],
					'size':		['', r"^\s+size:\s+(.+)$"], 
					#'furls':	['', r"^Real URLs:\s+(.+)$"],
					'furls': ['', r"^Real URLs?:\s*(.+)$"],
					'ftype':	['', r"^\s+container:\s+(.+)$"],
					'quality':	['', r"^\s+video-profile:\s+(.+)$"]} 




'''
新版:
[
	('site:                优酷 (Youku)',), ('\n',), 
	('title:               宇宙大爆炸',), ('\n',), 
	('stream:',), ('\n',), 
	('    - format:        mp4',), ('\n',), 
	('      container:     mp4',), ('\n',), 
	('      video-profile: 高清',), ('\n',), 
	('      size:          232.6 MiB (243858848 bytes)',), ('\n',), 
	('    # download-with: you-get --format=mp4 [URL]',), ('\n',), ('\n',), 
	('audio-languages:',), ('\n',), 
	('    - lang:          英语',), ('\n',), 
	('      download-url:  http://v.youku.com/v_show/id_XMzgzNTUyNTI0\n',), ('\n',), 
	('Real URLs:\nhttp://101.36.96.21:8082/117.177.248.48/65724ED07B830821C9DB283906/030008090050CCCF41EC4206685340A25F2AAA-A979-6F99-40B4-C366E82386D5.mp4\nhttp://101.36.96.21:8082/117.177.248.77/6572E28448437826D2280B3A93/030008090150CCCF41EC4206685340A25F2AAA-A979-6F99-40B4-C366E82386D5.mp4\nhttp://101.36.96.21:8082/117.177.248.47/6975C508CB833823F1F94B2BB6/030008090250CCCF41EC4206685340A25F2AAA-A979-6F99-40B4-C366E82386D5.mp4\nhttp://101.36.96.21:8082/117.177.248.25/697658BC9574182E0281462BCF/030008090350CCCF41EC4206685340A25F2AAA-A979-6F99-40B4-C366E82386D5.mp4\nhttp://101.36.96.21:8082/117.177.248.141/6775C50891639828424A7D6AC4/030008090450CCCF41EC4206685340A25F2AAA-A979-6F99-40B4-C366E82386D5.mp4\nhttp://101.36.96.21:8082/117.177.248.54/6575315451E368261A190F5240/030008090550CCCF41EC4206685340A25F2AAA-A979-6F99-40B4-C366E82386D5.mp4\nhttp://101.36.96.21:8082/117.177.248.141/697813D8D0730821C9EC3B5FBC/030008090650CCCF41EC4206685340A25F2AAA-A979-6F99-40B4-C366E82386D5.mp4',), ('\n',)
]


[
	('Video Site:',), (' ',), 
	('Tudou.com',), ('\n',), 
	('Title:     ',), (' ',), ('【发现最热视频】秀恩爱死得快！千万别在单身狗前秀恩爱',), ('\n',), 
	('Type:      ',), (' ',), 
	('Flash video (video/x-flv)',), ('\n',), 
	('Size:      ',), (' ',), ('34.91',), (' ',), ('MiB (36600715 Bytes)',), ('\n',), ('\n',), 
	('Real URLs:\nhttp://180.153.94.167/f4v/18/225430818.h264_4.040005010054FFEA74B7FFE995826F44021BE3-5AF0-227C-3EAF-000292113610.f4v?key=084e24cf32d1267470c43c555c099300112a08b9e3&playtype=5&tk=155012700720739147710903082&brt=5&bc=0&xid=040005010054FFEA74B7FFE995826F44021BE3-5AF0-227C-3EAF-000292113610&nt=0&nw=0&bs=0&ispid=42&rc=200&inf=12&si=un&npc=3364&pp=0&ul=0&mt=0&sid=0&pc=0&cip=118.122.88.216&id=tudou&hf=0&hd=0&sta=0&ssid=0&cvid=&itemid=292113610&fi=0&sz=36600715',), ('\n',)
]

旧版：

[
	('site:                优酷 (Youku)',), ('\n',), 
	('title:               技术牛人用硬盘和软盘做音乐：涅盘--少年心气',), ('\n',), 
	('stream:',), ('\n',), 
	('    - format:        \x1b[7mhd2\x1b[0m',), ('\n',), 
	('      container:     flv',), ('\n',), 
	('      video-profile: 超清',), ('\n',), 
	('      size:          38.3 MiB (40198118 bytes)',), ('\n',), 
	('    # download-with: \x1b[4myou-get --format=hd2 [URL]\x1b[0m',), ('\n',), ('\n',), 
	("Real URLs:\n['http://101.36.96.22:8082/113.6.237.202/6974BBF06AB3E73181DAA57E1/0300010200552A911326761581DC5716057C50-BD66-883F-9766-BDA05BE0A88B.flv', 'http://101.36.96.22:8082/221.204.199.112/677424729FE338292DC8E72E2B/0300010201552A911326761581DC5716057C50-BD66-883F-9766-BDA05BE0A88B.flv']\n",), ('\n',)
]



site:                优酷 (Youku)
title:               技术牛人用硬盘和软盘做音乐：涅盘--少年心气
stream:
    - format:        hd2
      container:     flv
      video-profile: 超清
      size:          38.3 MiB (40198118 bytes)
    # download-with: you-get --format=hd2 [URL]

Real URLs:
['http://101.36.96.21:8082/113.6.237.202/67738CF47DA3772BD37A45775/0300010200552A911326761581DC5716057C50-BD66-883F-9766-BDA05BE0A88B.flv', 'http://101.36.96.21:8082/221.204.199.112/6975536E7F13582AD374C85053/0300010201552A911326761581DC5716057C50-BD66-883F-9766-BDA05BE0A88B.flv']
'''
###############################
