#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def application(arg_io, query_string, ex_parm = None):
	assert isinstance(arg_io, dict) and isinstance(query_string, dict)
	TemplParse = ex_parm['TemplParse']
	templ_parse = TemplParse()

	import os
	root = './resource/template'
	templ_file = 'common/api_tool.htm'
	#if return_code:
	#	context = {'dev_log': dev_log}
	#else:
	#	context = {}
	
	#context = {}
	#doc, return_code = TemplParse().get_doc(root, templ_file, context)
	
	
	ymPrompt_js, return_code = templ_parse.get_text(os.path.join(root, '../js/common/ymPrompt.js'))
	assert return_code
	
	context = {'ymPrompt_js': ymPrompt_js}
	api_tool_doc, return_code = templ_parse.get_doc(root, templ_file, context)
	
	
	# header
	context = {'hello_message': '"Never stop believing in yourself."'}
	templ_file = 'common/header.htm'
	doc_header, return_code = templ_parse.get_doc(root, templ_file, context)
	assert return_code
	# footer
	doc_footer, return_code = templ_parse.get_text(os.path.join(root, 'common/footer.htm'))
	assert return_code
	# container
	context = {'container': api_tool_doc}
	templ_file = 'common/container.htm'
	doc_container, return_code = templ_parse.get_doc(root, templ_file, context)
	doc_container = '<div style="min-height:590px"><div style="height:20px"></div>'\
		+ '<section class="container"><h1><a href="/">D-L.top</a></h1>'\
		+ '<a href="javascript:history.go(-1);">返回前一页</a></section>'\
		+ doc_container + '<p></p></div>'
	#assert return_code
	
	doc = doc_header + doc_container + doc_footer
	
	arg_io['doc'] = doc
	arg_io['return_code'] = return_code
	if return_code:
		arg_io['ctype'] = 'text/html'
