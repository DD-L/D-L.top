#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def application(arg_io, query_string, ex_parm = None):
	assert isinstance(arg_io, dict) and isinstance(query_string, dict)
	TemplParse = ex_parm['TemplParse']
	templ_parse = TemplParse()
	
	import os
	root = './resource/template'
	# header
	context = {'hello_message': '"Never stop believing in yourself."'}
	templ_file = 'common/header.htm'
	doc_header, return_code = templ_parse.get_doc(root, templ_file, context)
	assert return_code

	# footer
	doc_footer, return_code = templ_parse.get_text(os.path.join(root, 'common/footer.htm'))
	assert return_code

	# body_div
	doc_body_div, return_code = templ_parse.get_text(os.path.join(root, 'dev_log.htm'))
	assert return_code

	# container
	context = {'container': doc_body_div}
	templ_file = 'common/container.htm'
	doc_container, return_code = templ_parse.get_doc(root, templ_file, context)
	assert return_code

	doc = doc_header + doc_container + doc_footer
	
	arg_io['doc'] = doc
	arg_io['return_code'] = return_code
	if return_code:
		arg_io['ctype'] = 'text/html'
