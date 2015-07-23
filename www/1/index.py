#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ex_parm = {'environ': environ, 'start_response': start_response}
def application(arg_io, query_string, ex_parm = None):
	assert isinstance(arg_io, dict) and isinstance(query_string, dict)
	#res = 'hello world'
	#if 'fname' in query_string and 'lname' in query_string :
	#	fname = query_string['fname']
	#	lname = query_string['lname']
	#	res = res + '\nfname = ' + fname + '\nlname = ' + lname
	import types
	res = '<h1>hello</h1><h2>path_info:\'' + ex_parm['environ']['PATH_INFO'] + '\'</h2>'
	arg_io['doc'] = res
	arg_io['ctype'] = 'text/html'
