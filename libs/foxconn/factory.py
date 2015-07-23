#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 抽象类
class VideoFactory:
	def __init__(self):
		self._baseclass_ = 'VideoFactory'
		self._video = dict()
		#define self._video
		self._define_node()

	# 留作子类重写(修改videos)
	def attach(self, videos):
		pass
	# 留作子类重写
	def _define_node(self):
		pass
	# 留作子类重写(修改doc)
	def modify_doc(self, doc):
		pass
	# 留作子类重写(修改doc 输出的文本)
	def post_proc(self, buff):
		return buff
'''
# eg.

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
					'furls':	['', r"^Real URLs:\s+(.+)$"],
					'ftype':	['', r"^\s+container:\s+(.+)$"],
					'quality':	['', r"^\s+video-profile:\s+(.+)$"]} 
'''
