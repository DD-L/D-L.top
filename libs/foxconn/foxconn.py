#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys
import re
import copy


# init
# you-get 的相对路径:
_relativePath = '../you-get/'
_srcdir = os.path.join(_relativePath, 'src')

_curfullpath = os.path.dirname(os.path.realpath(__file__))

_youfullpath = os.path.join(_curfullpath, _relativePath)
_srcfullpath = os.path.join(_curfullpath, _srcdir)

_youfullpath = os.path.normpath(_youfullpath)
_srcfullpath = os.path.normpath(_srcfullpath)

if not _srcfullpath in sys.path:
	#sys.path.insert(1, _srcfullpath)
	sys.path.append(_srcfullpath)
if not _youfullpath in sys.path:
	#sys.path.insert(1, _youfullpath)
	sys.path.append(_srcfullpath)

import you_get
from you_get.common import *


class TextArea(object):  
	def __init__(self): 
		self.buffer = []
		self.stdout = sys.stdout
	def write(self, *args, **kwargs): 
		self.buffer.append(args)
	def isatty(self):
		return self.stdout.isatty()
	def flush(self):
		return self.stdout.flush()

from factory import VideoFactory
from xml.dom import minidom
class Foxconn:
	def __init__(self, url):
		assert (sys.version_info[0] == 3)
		if isinstance(url, str): url = [url]
		self._url = url
		self._buff = ''
		self._videos = list()
		self.__fty = self # 只有 _video, attach 和 to_xml中使用

		self._video = dict() # VideoFactory 可改写
		# define self._video
		self._define_node()
		self.__doc = None
		
	def factory(self, videosite = None):
		assert (videosite._baseclass_ == VideoFactory.__name__)
		if videosite:
			self.__fty = videosite
			self._video = videosite._video
		else:
			self.__fty = self
	
	# 附加处理，兼容VideoFactory。比如youtube中的itag转质量的处理
	# VideoFactory 可改写 self._videos
	def attach(self, vidoes):
		#在取出node后，可对videos做出修改
		pass
	# 附加处理，兼容VideoFactory
	# 在to_xml()输出前 VideoFactory 可改写 self.__doc
	def modify_doc(self, doc):
		pass
	# 附加处理，兼容VideoFactory。比如bilibili中弹幕文件的处理
	# 在to_xml() 输出后 VideoFactory 可改写 self.__doc 输出的文本
	def post_proc(self, buff):
		return buff

	#Returns: 和to_xml()返回值一样
	def output(self, cdata = True):
		self.get_node()
		self.__fty.attach(self._videos)
		buff, return_code = self.to_xml(cdata)
		if return_code:
			buff = self.__fty.post_proc(buff)
		return buff, return_code
		
	def parse_url(self):
		#
		stream_id = None # a   # -F --format --stream --itag
		output_dir = '.'
		merge = True #False <---
		#merge = False# <---
		info_only = False
		playlist = False

		#cookies_txt = None
		#lang = None
		#proxy = None
		#extractor_proxy = None
		#traceback = False
		you_get.common.dry_run = True

		url = self._url
		
		# parse
		try:
			# 重定向stdout
			stdout = sys.stdout
			sys.stdout = TextArea()
			
			try:
				if stream_id:
					you_get.common.download_main(any_download, any_download_playlist, url, playlist, 
												stream_id=stream_id, output_dir=output_dir, 
												merge=merge, info_only=info_only)
				else:
					you_get.common.download_main(any_download, any_download_playlist, url, playlist, 
												output_dir=output_dir, merge=merge, info_only=info_only)
			except SystemExit as e:
				if str(e) != '0': 
					self._buff = False
					return False
			finally:
				# 恢复stdout
				text_area, sys.stdout = sys.stdout, stdout
			self._buff = text_area.buffer
			return self._buff
		except:
			#sys.exit(1)
			self._buff = False
			return self._buff


	# 定义node取出的方式, 可由VideoFactory改写
	# 定义self._video，类初始化时被调用
	def _define_node(self):

		# _video格式: dict()
		# key = str('node')
		# value = list() 
		#	1. 只能是下面两种情况:
		#		1. value = ['', r"node_regex"] # value[0] = ''(必须为''), value[1] = r"node_regex", 将要取出的文本用括号括起来，且只能有一个括号  
		#		2. value = ['other node', ''] # value[0]代表当前node 和 other node 值是一样的, 且value[1]必须为''
		#   2. 必须定义够7个键值对, site, title, vformat, size, furls, ftype, quality

		# 匹配是把结果分成单行来匹配的, 所以node_regex可以使用 (.+)$
		self._video = {'site': ['', r"^Video\sSite:\s+(.+)$"],
				'title': ['', r"^Title:\s+(.+)$"],
				'vformat': ['',  r"^Type:\s+(.+)$"],
				 'size': ['', r"^Size:\s+(.+)$"], 
				 #'furls': ['', r"^Real URLs:\s+(.+)$"],
				 'furls': ['', r"^Real URLs?:\s*(.+)$"],
				 'ftype': ['vformat', ''], # default value
				 'quality': ['vformat', '']} # default value

	# default
	def get_node(self):
		#_video
		assert isinstance(self.__fty._video, dict)
		assert self.__fty._video['vformat'][1] # vformat_regex
		assert self.__fty._video['furls'][1] # furls_regex
		
		# 将self._buff 转成 buff, 以便合并单行
		assert self._buff
		buff = list() # 每一个元素就是一整行文字
		linebuff = ''
		for v in self._buff:
			if v[0] != '\n':
				linebuff = linebuff + v[0]
			else: # 一行结束
				buff.append(linebuff)		
				linebuff = ''
		'''
		针对you-get的此次升级，（furls输出格式变化），做出相应调整.
		大致有：
		1. 正则表达式:
			由 'furls': ['', r"^Real URLs:\s+(.+)$"], 改为 'furls': ['', r"^Real URLs?:\s*(.+)$"],
		2. 在dig_node() 中修改匹配模式， 使'.'也能匹配'\n'
		3. 在dig_node()后取出的字符串，转list的时候，做了调整
		'''

		# 执行时要保证 self.__fty._video 值不变, 所以拿video做副本
		video = copy.copy(self.__fty._video) # 浅拷
		for line in buff:
			if line == '' or line == '\n': continue
			for node, value in video.items():
				if value[1] != '' and value[0] == '':
					#site = self.dig_node(site, site_regex, line)
					text = self.dig_node(value[0], value[1], line)
					video[node] = [text, value[1]]
					if text != '': break

			vformat = video['vformat'][0]
			furls = video['furls'][0]
			if furls: #一个video节点结束

				# 进一步处理 vformat 和 furls
				vformat = vformat.replace('\x1b[7m', "").replace('\x1b[0m', "")
				# furls str() -> list()
				#furls = furls.strip("[] ").replace(",", "").replace("'", "").split(" ") # old you-get version
				furls = furls.strip("[] ").split("\n")
				# 去除空元素
				if '' in furls:
					furls.remove('')
				# 去除[]
				i=0
				for furl in furls:
					furl = furl.strip("[] '")
					furls[i] = furl
					i = i + 1
				
				temp = video['vformat']
				assert temp[1] # node_regex
				video['vformat'] = [vformat, temp[1]]
				temp = video['furls']
				assert temp[1] # node_regex
				video['furls'] = [furls, temp[1]]


				for node, value in video.items():
					if value[0] != '' and value[1] == '':
						if video[value[0]][0] != '':
							#  video[value[0]] 已经被赋值
							video[node] = video[value[0]]
						else:
							# 保持原样
							pass
				# 制作self._videos
				self._videos.append(video)
				#videos.append({'site': site, 'title': title, 'vformat': vformat, 'size': size, 'furls': furls})	

				# 清空变量, 以便重新赋值
				#site, title, vformat, size, furls = '', '', '', '', list()
				# 重新赋值即为清空
				video = copy.copy(self.__fty._video) # 浅拷

	


	######################
	# 制作XML
	######################
	# default
	# Returns: res, return_code
	def to_xml(self, cdata = True):
		try:
			#放到output中去，以便控制流程
			#videos = self.get_node()
			videos = self._videos
			assert isinstance(videos, list)
			##################################################
			doc = minidom.Document()
			self.__doc = doc

			# root
			rootNode = doc.createElement("root")
			doc.appendChild(rootNode)

			for video in videos:
				assert isinstance(video, dict)
				#video: {'site': site, 'title': title, 'vformat': vformat, 'size': size, 'furls': furls}
				title   = video['title'][0]
				furls   = video['furls'][0]
				vformat = video['vformat'][0]
				size    = video['size'][0]
				site    = video['site'][0]
				ftype   = video['ftype'][0]
				quality = video['quality'][0]
				playurl = ''.join(self._url)

				# root - video
				videoNode = doc.createElement("video")
				#videoNode.setAttribute("id", "0") 
				rootNode.appendChild(videoNode)

				# root - video - title
				titleNode = doc.createElement("title")
				videoNode.appendChild(titleNode)
				self.textNode(titleNode, title)

				# root - video - files 
				filesNode = doc.createElement("files")
				videoNode.appendChild(filesNode)

				first = True
				for furl in furls:
					# root - video - files - file
					fileNode = doc.createElement("file")
					filesNode.appendChild(fileNode)

					# root - video - files - file - furl
					furlNode = doc.createElement("furl")
					fileNode.appendChild(furlNode)
					self.textNode(furlNode, furl)

					# root - video - files - file - ftype
					ftypeNode = doc.createElement("ftype")
					fileNode.appendChild(ftypeNode)
					self.textNode(ftypeNode, ftype, False)

					# root - video - files - file - size
					first and fileNode.appendChild(doc.createComment("Warning: Not supported yet. The size of a single video file (Byte)"))
					fsizeNode = doc.createElement("size")
					fileNode.appendChild(fsizeNode)
					self.textNode(fsizeNode, '0', False) # 遗留, 单个文件的大小(Byte)

					# root - video - files - file - seconds
					first and fileNode.appendChild(doc.createComment("Warning: Not supported yet. The duration of a single video file (seconds)"))
					secondsNode = doc.createElement("seconds")
					fileNode.appendChild(secondsNode)
					self.textNode(secondsNode, '0', False) # 遗留, 单个文件的时长(s)
					
					first = False
					# end: for furl in furls

				# root - video - size << new item >>
				videoNode.appendChild(doc.createComment("New - Added node 'size': the total size of video files"))
				sizeNode = doc.createElement("size")
				videoNode.appendChild(sizeNode)
				self.textNode(sizeNode, size)

				# root - video - site
				siteNode = doc.createElement("site")
				videoNode.appendChild(siteNode)
				self.textNode(siteNode, site)

				# 为了保持兼容，保留quality节点
				# root - video - quality
				qualityNode = doc.createElement("quality")
				videoNode.appendChild(qualityNode)
				self.textNode(qualityNode, quality)

				# root - video - playurl
				playurlNode = doc.createElement("playurl")
				videoNode.appendChild(playurlNode)
				self.textNode(playurlNode, playurl)

				# root - video - img 
				videoNode.appendChild(doc.createComment("Warning: Not supported yet. Preview of video"))
				imgNode = doc.createElement("img")
				videoNode.appendChild(imgNode)
				self.textNode(imgNode, '') # 遗留, 视频预览图, 参见优酷
				# end: for video in videos
			##################################################

			self.__fty.modify_doc(doc)
			return doc.toxml("UTF-8").decode(), True

		except Exception as e:
			return 'Err: [Failed] server error.', False

	
	# tools:
	def dig_node(self, n, regex, string):
		if isinstance(n, list): # 兼容节点furls(type:list)
			n = ''.join(n)
		if n == '': # 只有node变量n不等于''才能被赋新值
			n = ''.join(re.findall(regex, string, re.DOTALL))
		return n

	def textNode(self, node, text, cdata = True):
		assert isinstance(text, str)
		assert self.__doc
		doc = self.__doc
		if cdata:
			node.appendChild(doc.createCDATASection(' ' + text + ' '))
		else:
			node.appendChild(doc.createTextNode(text))


