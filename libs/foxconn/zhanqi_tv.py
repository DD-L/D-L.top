#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from factory import VideoFactory
class Zhanqi_tv(VideoFactory):
	def __init__(self):
		super(Zhanqi_tv, self).__init__()
		self.define_node()

	#def attach(self, videos):
	#	super(Youku, self)._attach(videos)
	#	pass

	def define_node(self):
		self._video = {'site':	['', r"^Video Site:\s+(.+)$"],
					'title':	['', r"^Title:\s+(.+)$"],
					'vformat':	['', r"^Type:\s+(.*)$"],
					'size':		['', r"^Size:\s+(.+)$"], 
					#'furls':	['', r"^Real URLs?:\s+(.+)$"],
					'furls': 	['', r"^Real URLs?:\s*(.+)$"],
					'ftype':	['vformat', ''],
					'quality':	['vformat', '']} 




'''
Video Site: zhanqi.tv
Title:      微笑：  今天是弟弟来直播视频2015-04-24-00-17
Type:       Flash video (video/x-flv)
Size:       inf MiB (inf Bytes)

Real URL:
['http://dlvod.cdn.zhanqi.tv//videonew/hls/special/18257_2ed64d/18257_2ed64d.m3u8']

'''
###############################
