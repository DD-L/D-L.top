#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def application(arg_io, query_string, ex_parm = None):
	assert isinstance(arg_io, dict) and isinstance(query_string, dict)
	#res = 'hello world'
	#if 'fname' in query_string and 'lname' in query_string :
	#	fname = query_string['fname']
	#	lname = query_string['lname']
	#	res = res + '\nfname = ' + fname + '\nlname = ' + lname
	res = '<h1>hello</h1>'
	arg_io['doc'] = res
	arg_io['ctype'] = 'text/html'