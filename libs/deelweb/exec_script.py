#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, sys
_curfullpath = os.path.dirname(os.path.realpath(__file__))
_common_path = '../common'
_commonfullpath = os.path.join(_curfullpath, _common_path)
_commonfullpath = os.path.abspath(_commonfullpath)
if not _commonfullpath in sys.path:
	#sys.path.insert(1, _commonfullpath)
	sys.path.append(_commonfullpath)

from .jinja_parse import TemplParse

def parse_query_string(query_s):
	query_string = dict()
	if query_s != '':
		res = query_s.lstrip('?')
		res = res.split('&')
		for arg in res:
			if arg == '': continue
			kv = arg.split('=')
			if len(kv) == 1:
				key, value = kv[0], ''
			else:
				key, value = kv[0], kv[1] # 多余的将被丢弃
			if key != '':
				query_string[key] = value
	return query_string

def py_exec(root, file_path, arg_io, query_s, ex_parm = None):
	try:
		assert isinstance(arg_io, dict)
		import exec_path
		exec_path = exec_path.ExecPath()
		exec_path.set(os.path.dirname(file_path))
		
		script_module = os.path.basename(file_path)
		script_module = script_module.rstrip('.py')
		if script_module == '':
			raise Exception("import err: module is ''")
		#import script_module
		script = __import__(script_module)
		query_string = parse_query_string(query_s)
		ex_parm['TemplParse'] = TemplParse
		script.application(arg_io, query_string, ex_parm)
	except Exception as e:
		arg_io['ctype'] = 'text/plain'
		arg_io['doc'] = str(e)
		arg_io['return_code'] = False
	except:
		arg_io['ctype'] = 'text/plain'
		arg_io['doc'] = ''
		arg_io['return_code'] = False
	finally:
		exec_path.reset()
		
#'''
#脚本样例:
#
#/test.py?url=index.htm
#
## *- <code> -*
#def application(arg_io, query_string, ex_parm = None):
#	#ex_parm = {'environ': environ, 'start_response' = start_response}
#	assert isinstance(arg_io, dict) and isinstance(query_string, dict)
#	res = 'hello world'
#	if 'url' in query_string:
#		url = query_string['url']
#		res = res + '\nurl = ' + url
#	arg_io['doc'] = res
## *- </code> -*
#
#output:
#
#hello world
#url = index.htm
#
#
#模板样例: (详见jinja_parse.py)
#
#def application(arg_io, query_string, ex_parm = None):
#	root = 'resource/template'
#	templ_file = 'jinja_test.htm'
#	context = {'hello': 'Hello', 'vai_i': 'I'}
#	TemplParse = ex_parm['TemplParse']
#	doc, return_code = TemplParse().get_doc(root, templ_file, context)
#	#doc, return_code = TemplParse().get_doc(root, templ_file, hello='Helloo', var_i='I')
#	#print(doc, return_code)
#	arg_io['doc'] = doc
#	arg_io['return_code'] = return_code
#'''
