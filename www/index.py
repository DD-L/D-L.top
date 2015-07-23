#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def application(arg_io, query_string, ex_parm = None):
	assert isinstance(arg_io, dict) and isinstance(query_string, dict)
	TemplParse = ex_parm['TemplParse']

	#dev_log, return_code = TemplParse().get_text('./resource/js/dev_log.js')
	root = './resource/template'
	templ_file = 'index/d-l.top.index.htm'
	#if return_code:
	#	context = {'dev_log': dev_log}
	#else:
	#	context = {}
	context = {}
	doc, return_code = TemplParse().get_doc(root, templ_file, context)
	
	arg_io['doc'] = doc
	arg_io['return_code'] = return_code
	if return_code:
		arg_io['ctype'] = 'text/html'
