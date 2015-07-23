#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys
import re

# init
_foxconndir = 'libs/foxconn/'
_curfullpath = os.path.dirname(os.path.realpath(__file__))
_foxconnfullpath = os.path.join(_curfullpath, _foxconndir)
_foxconnfullpath = os.path.normpath(_foxconnfullpath)
if not _foxconnfullpath in sys.path:
	#sys.path.insert(1, _foxconnfullpath)
	sys.path.append(_foxconnfullpath)

# 获取解析结果
# Returns: res; ctype: 'text/plain' or 'text/xml'; return_code 
def get_res(url, cdata = True):
	ctype = 'text/plain'
	try:
		from foxconn import Foxconn
		fxc = Foxconn(url)
		buff = fxc.parse_url()
		if buff is False:
			return 'Err: [Failed] Video not found.', ctype, False
		# ensure that the url is legal
		#if buff 中有通用的node:
		if exist_common_node(buff):
			ctype = 'text/xml'
			# special site:
			if (re.match(r'^.{0,17}\.youku\.com', url, re.M|re.I)):
				# youku.com
				from youku import Youku
				fxc.factory(Youku())
			elif (re.match(r'^.{0,17}\.youtube\.com', url, re.M|re.I)):
				# youtube.com
				from youtube import Youtube
				fxc.factory(Youtube())
			elif (re.match(r'^.{0,17}\.bilibili\.com', url, re.M|re.I)):
				#bilibili.com
				from bilibili import Bilibili
				fxc.factory(Bilibili())
			elif (re.match(r'^.{0,17}\.zhanqi\.tv', url, re.M|re.I)):
				from zhanqi_tv import Zhanqi_tv
				fxc.factory(Zhanqi_tv())
			#....

			# normal site:
			# 判断一下output 的return_code
			res, return_code = fxc.output(cdata)
			if return_code is False:
				ctype = 'text/plain'
			return res, ctype, return_code
		else:	
			# default:	
			# can get the correct results, but could not turn into xml
			body = ''
			for v in buff:
				body = body + v[0]
			ctype = 'text/plain'
			return body, ctype, True
	except Exception as e:
		ctype = 'text/plain'
		return 'Err: API server error.\n' + str(e), ctype, False


# 检查是否有通用的node
# [sS]ite [tT]itle [sS]ize Real\sURLs:
def exist_common_node(buff):
	import copy
	res_buff = copy.copy(buff)
	assert res_buff
	assert isinstance(res_buff, list)

	# 特征字符串
	feature_str = [r"[sS]ite", r"[tT]itle", r"[sS]ize", r"Real\sURLs?"]
	index = 0 
	feature_str_length = len(feature_str)

	# 如果v[0] 依次出现 [sS]ite [tT]itle [sS]ize Real\sURLs: 
	# 即返回 True; 否则返回 False
	for v in res_buff:
		if re.search(feature_str[index], v[0]):
			index = index + 1
		if index >= feature_str_length:
			return True
	return False
