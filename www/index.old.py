#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 简单模板 gettext encode decode integrate 可以抽象起来, 遗留


def gettext(file_name, encoding='utf-8'):
	if file_name == '': return ''
	try:
		res = ''
		pfile = open(file_name, 'r', encoding=encoding)
		res = pfile.read()
		pfile.close()
	except Exception as e:
		res = str(e)
	except:
		res = 'Error'
	finally:
		return res

# template中的变量%(var)s占位符 要写成 _<100percent>+(var)s
# 处理符号%
def encode(res):
	res = res.replace(r'%', r'<`!`<>-^&>')
	res = res.replace(r'_<100percent>+', r'%')
	return res
def decode(res):
	res = res.replace(r'<`!`<>-^&>', r'%')
	return res

def integrate():
	res = gettext('./resource/template/index/d-l.top.index.old.htm')
	js = gettext('./resource/js/dev_log.js')
	res = encode(res)
	js = encode(js)
	body = res % {'dev_log_js': js}
	body = decode(body)
	return body

def application(arg_io, query_string, ex_parm = None):
	assert isinstance(arg_io, dict) and isinstance(query_string, dict)
	arg_io['doc'] = integrate()
	arg_io['ctype'] = 'text/html'
