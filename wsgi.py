#!/usr/bin/env python
import os, sys
import re

_curfullpath = os.path.dirname(os.path.realpath(__file__))
# 在sys.path中去除./libs 干扰, 为避免模块名冲突
__libs_fullpath = os.path.normpath(os.path.join(_curfullpath, './libs'))
if __libs_fullpath in sys.path:
	sys.path.remove(__libs_fullpath)
if not _curfullpath in sys.path:
	#sys.path.insert(1, _curfullpath)
	sys.path.append(_curfullpath)
import tools.visitor as vstr
import tools.function as func
import libs.deelweb.doc_get as httpdoc

import libs.common.exec_path as epath
exec_path = epath.ExecPath()

def application(environ, start_response):
	ctype = 'text/plain'
	if environ['PATH_INFO'] == '/health':
		response_body = "1"
	#elif environ['PATH_INFO'] == '/test/env':
	#	response_body = ['%s: %s' % (key, value)
	#				for key, value in sorted(environ.items())]
	#	response_body = '\n'.join(response_body)
	elif environ['PATH_INFO'] == '/you':
		response_body = 'path_info: /you'
		#sys_platform = sys.platform
		#import yg_api
		#playurl, title, site, ftype, quality, vformat, size, furls = yg_api.get_node('http://v.youku.com/v_show/id_XOTEwNDExMzc2_ev_5.html', True)

		#response_body = ''.join(vformat)
		#response_body = ''.join(sys_platform) + '<--\n\n' + response_body


		#from yg_api import toxml
		#ctype = 'text/xml'
		#cdata = False # default: True
		#response_body = toxml('http://v.youku.com/v_show/id_XOTM0MDg5NTcy.html', cdata = True)

		#response_body = response_body.encode("UTF-8")

		#status = '200 OK'
		#response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
		##
		#start_response(status, response_headers)
		#return [response_body]
	
	#elif environ['PATH_INFO'] == '/fuck/db_init/token/deelorder/do':
	#	try:
	#		import db_tools
	#		db_tools.db_init()
	#		response_body = 'database initialization'
	#	except Exception as e:
	#		response_body = str(e) 
	#elif environ['PATH_INFO'] == '/fuck/db_forced_init/token/deelorder/do':
	#	try:
	#		import db_tools
	#		db_tools.db_init(True)
	#		response_body = 'database Forced initialization'
	#	except Exception as e:
	#		response_body = str(e) 
        
	###############################
	#api
	#'''API 格式: (PHP版)'''
	#	http://simplevideo-deel.rhcloud.com/svapi/token/$token/url/$base64url
	#	http://simplevideo-deel.rhcloud.com/svencryptapi/token/$token/url/$base64url
	#	http://D-L.top/svapi/token/$token/url/$base64url
	#	http://D-L.top/svencryptapi/token/$token/url/$base64url

	#Notes:
	#	1. /svapi/... 返回普通xml数据
	#	2. /svencryptapi/... 返回对xml可逆加密后的数据
	#	3. $token 请向管理员申请
	#	4. $base64url = strtr(base64_encode(str_replace('://', ':##', $url)), '+/', '-_'); // $url 为原站视频播放页url
	#	5. 注意token和url的顺序不能颠倒'''
	###############################
	elif re.match(r"^/sv(encrypt)?api/token/[^/]+/url/[^/]+", environ['PATH_INFO']):
		path_info = environ['PATH_INFO']
		#
		try:
			# 设置工作目录及sys.path
			exec_path.set(_curfullpath)

			visitor = vstr.Visitor()
			http_user_agent, client_ip, request_start, host = visitor.get_visitor_info(environ)
			is_cache = False
			url = ''
			ctype = 'text/plain'
			# added debug host localhost:8051
			if host == 'api.d-l.top' or host == 'simplevideo-deel.rhcloud.com' or 'localhost:8051':
				try:
					# parse url
					is_encrypt, token, base64url, return_code = func.parse_url(path_info)
					if return_code:
						# decode base64url
						url, return_code = func.decode_base64url(base64url)
						if return_code:
							# test and verify
							if (visitor.access(token, http_user_agent, client_ip, request_start, host)):
								# get api
								import simplevideo_api
								is_success = False
								cdata = True
								response_body, ctype, return_code = simplevideo_api.get_res(url, cdata)
								if return_code:
									is_success = True
								if is_encrypt:
									response_body = func.api_respone_encrypt(response_body)
								if len(response_body) > 16777215: # mysql: TEXT 0~65535; MEDIUMTEXT: 0~16,777,215
									is_cache = True # 数据库里的数据可能会不完整，必须使以后的查询不再使用该数据
								visitor.leave(http_user_agent, client_ip, request_start, host, path_info, url, is_cache, is_success, response_body, is_encrypt)
							else:
								response_body = 'Err: Not permitted to enter. token error, or requests are too frequent, please try again later.' 
								visitor.leave(http_user_agent, client_ip, request_start, host, path_info, url, is_cache, False, response_body, is_encrypt)
						else:
							response_body = 'Err: Bad url.'
							visitor.leave(http_user_agent, client_ip, request_start, host, path_info, url, is_cache, False, response_body, is_encrypt)
					else:
						response_body = 'Err: An error occurred when parsing url.'
						visitor.leave(http_user_agent, client_ip, request_start, host, path_info, '', is_cache, False, response_body, is_encrypt)
				except BaseException: # all Exception. Contain: BaseException, SystemExit, Exception
					try:
						# read cache 
						# 去数据库中查找，最新的（同比id最大的） is_success == True and is_cache == False and requset_url == url 的那条记录
						db_response_body, db_is_encrypt, return_code = visitor.cache(url);
						if return_code:
							ctype = 'text/xml'
							response_body = db_response_body
							if (is_encrypt == True) and (db_is_encrypt == False):
								ctype = 'text/plain'
								response_body = api_respone_encrypt(response_body)
							visitor.leave(http_user_agent, client_ip, request_start, host, path_info, url, True, return_code, response_body, is_encrypt)
						else:
							# the specified record was not found
							raise Exception('Err: API Server Error. even the cache(\'' + url + '\') was not found')
					except Exception as e:
						#response_body = 'Err: API Server Error.'
						response_body = str(e)
						visitor.leave(http_user_agent, client_ip, request_start, host, path_info, url, False, False, response_body, False)
			else:
				response_body = 'Err: To access the API, please use the host "api.D-L.top" or "simplevideo-deel.rhcloud.com"'
				visitor.leave(http_user_agent, client_ip, request_start, host, path_info, url, is_cache, False, response_body, False)

		except Exception as e:
			response_body = 'Err: Database Error.'
		finally:
			exec_path.reset()	
	# default
	else: # 参数在这里面: environ['QUERY_STRING'] 
		try:
			# 设置工作目录及sys.path
			exec_path.set(_curfullpath)
			# 获取查询字符串
			if environ['REQUEST_METHOD'] == 'GET':
				query_string = environ['QUERY_STRING']
			elif environ['REQUEST_METHOD'] == 'POST':
				try:
					request_body_size = int(environ.get('CONTENT_LENGTH', 0))
				except (ValueError):
					request_body_size = 0
				query_string = environ['wsgi.input'].read(request_body_size).decode('utf8')
			else:
				query_string = ''

			file_path = environ['PATH_INFO']
			doc_root = os.path.join(_curfullpath, './www/')
			ctype = 'text/plain'
			ex_parm = {'environ': environ, 'start_response': start_response}
			ctype, doc, is_binary, return_code = httpdoc.get(doc_root, file_path, query_string, ex_parm)
			response_body = doc
			if return_code:
				if is_binary:
					status = '200 OK'
					response_headers = [('Content-Type', ctype), 
							('Content-Length', str(len(response_body)))]
					start_response(status, response_headers)
					return [response_body]
			else:
				# 404 or 403
				pass
		except Exception as e:
			response_body = 'Welcome to D-L.top'
		finally:
			exec_path.reset()
	# end if
	response_body = response_body.encode("UTF-8")
	status = '200 OK'
	response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
	#
	start_response(status, response_headers)
	#return [response_body.encode('utf-8') ]
	return [response_body]

#
# Below for testing only
#
if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	#httpd = make_server('localhost', 8051, application)
	httpd = make_server('0.0.0.0', 8051, application)
	# Wait for a single request, serve it and quit.
	httpd.handle_request()
