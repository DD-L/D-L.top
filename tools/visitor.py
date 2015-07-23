#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#import pdb
#import types

import os, sys
_curfullpath = os.path.dirname(os.path.realpath(__file__))
_dbdir = '../libs/db/mysql/'
_dbfullpath = os.path.join(_curfullpath, _dbdir)
_dbfullpath = os.path.normpath(_dbfullpath)
if not _dbfullpath in sys.path:
	#sys.path.insert(1, _dbfullpath)
	sys.path.append(_dbfullpath)

from sv_db import SvDb

class Visitor:
	db = ''
	def __init__(self):
		self.db = SvDb()
	def __del__(self):
		self.db.commit()

	def get_visitor_info(self, environ):
		#HTTP_USER_AGENT
		http_user_agent = ''
		#HTTP_X_CLIENT_IP
		client_ip = ''
		#HTTP_X_REQUEST_START
		request_start = ''
		
		#def default_http_user_agent():
		#	import random
		#	container = 'zyxwvutsrqponmlkjihgfedcbaABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		#	http_user_agent = ''.join(random.sample(container, 16))
		#	return http_user_agent
		def default_request_start():
			import time
			t = ''.join(str(time.time()).replace('.', ''))
			return 't=' + t

		#environ.get('HTTP_USER_AGENT', default_http_user_agent()),
		http_user_agent, client_ip, request_start, host =\
			environ.get('HTTP_USER_AGENT', 'Unknown Device'),\
			environ.get('HTTP_X_CLIENT_IP', '127.0.0.1'),\
			environ.get('HTTP_X_REQUEST_START', default_request_start()),\
			environ.get('HTTP_HOST', ''),

		request_start = request_start[2:12]
		return http_user_agent, client_ip, request_start, host

	def access(self, token, http_user_agent, client_ip, request_start, host):
		import base64
		user_agent_ip = http_user_agent + '@' + client_ip
		user_agent_ip = base64.b64encode(user_agent_ip.encode()).decode()
		return self.db.allow_access(token, user_agent_ip, request_start)

	def leave(self, http_user_agent, client_ip, request_start, host, path_info, request_url, is_cache, is_success, response_body, is_encrypt):
		return self.db.touch_table_visitor_info(http_user_agent, client_ip, request_start, host, path_info, request_url, is_cache, is_success, response_body, is_encrypt)

	# read cache
	# Returns: response_body, is_encrypt, return_code
	def cache(self, request_url):
		return self.db.visitor_cache(request_url)
