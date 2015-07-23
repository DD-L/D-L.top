#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, sys, re
from .content_type import HTTP_CONTENT_TYPE
from .http_index import DOC_INDEX

# 返回格式化后的绝对路径
#	root: www的根路径(绝对路径); file_path 为文档的相对路径(相对根)
#   且file_path为root的子路径(root为file_path的子串)
def format_path(root, file_path):
	assert os.path.isabs(root)
	assert os.path.isdir(root)
	root = os.path.normpath(root)
	file_path = os.path.normpath(file_path)
	if sys.platform[:5] == 'win32':
		root = root.replace('\\', '/')
		file_path = file_path.replace('\\', '/')
	# file_path为绝对路径
	if os.path.isabs(file_path):
		#/ /uwr d:/sdf d:\\sdf \\ 
		#/ /usr d:/sdf d:/sdf  /
		# 对于/特殊处理
		if file_path == '/' or file_path == '\\':
			file_path = root
			return root, file_path
		if re.match(root, file_path):
			return root, file_path
	# file_path为相对路径
	#file_path = file_path.lstrip('/')
	file_path = os.path.join('./', './' + file_path)
	file_path = os.path.join(root, file_path)
	file_path = os.path.abspath(file_path)
	file_path = os.path.normpath(file_path)
	if sys.platform[:5] == 'win32':
		root = root.replace('\\', '/')
		file_path = file_path.replace('\\', '/')
	return root, file_path

# 验证file_path
#	file_path 为存在的文档或目录, 且不能越出 root目录
#	接受来自format_path()返回的路径
#	Returns: is_dir, file_path
def verify_path(root, file_path):
	try:
		if not re.match(root, file_path):
			# file_path 越出根目录 [越权]
			return False, False
		if os.path.isfile(file_path):
			is_dir = False
			# 返回格式化后的绝对路径
			return is_dir, file_path
		elif os.path.isdir(file_path):
			is_dir = True
			# 返回格式化后的绝对路径
			return is_dir, file_path
		else:
			return False, False
	except:
		return False, False

# 取出文档名的后缀
def get_suffix(file_path):
	file_name = os.path.basename(file_path)
	suffix = ''.join(re.findall(r'(\.[^.]*)$', file_name))
	if suffix == '':
		return file_name # 默认返回整个文件名
	else:
		return suffix

def get_index(file_path):
	assert os.path.isdir(file_path)
	assert DOC_INDEX
	for index in DOC_INDEX:
		index_path = os.path.join(file_path, index)
		if os.path.isfile(index_path):
			return index_path
	# 404
	return False


# 获取指定的文档 (当前只支持静态网页, 后续可添加对python的支持)
# 参数:
#	root 文档根
#	file_path 文档(相对根的路径)
#	query_s 查询字符串(参数)
#	ex_parm = {'environ': environ, 'start_response' = start_response}
# 返回值:
#  HTTP_CONTENT-TYPE, doc, is_binary, return_code
def get(root, file_path, query_s = '', ex_parm = None):
	# 得到格式化后的绝对路径
	root, file_path = format_path(root, file_path)
	
	# 获取文档后缀
	suffix = get_suffix(file_path)
	if '.do' in HTTP_CONTENT_TYPE and suffix == '.do':
		file_path = file_path[:-3] + '.py'

	# 验证path是否有效
	# test and verify path
	is_dir, file_path = verify_path(root, file_path)
	if file_path:
		if is_dir is False:
			# 获取文档后缀
			#suffix = get_suffix(file_path)
			if suffix in HTTP_CONTENT_TYPE:
				ctype = HTTP_CONTENT_TYPE[suffix]
				doc = ''
				is_binary = False
				return_code = False
				# 执行python 脚本
				if suffix == '.do':
					from .exec_script import py_exec
					arg_io = {'ctype': ctype, 'doc': doc, 'is_binary': is_binary, 'return_code': return_code}
					py_exec(root, file_path, arg_io, query_s, ex_parm)
					return arg_io['ctype'], arg_io['doc'], arg_io['is_binary'], arg_io['return_code']
				# 普通静态doc
				else:
					try:
						# 检查是否为text
						if re.match(r'text/', ctype):
							# 文本文件
								pfile = open(file_path, 'r', encoding='utf8')
								is_binary = False
						else:
							# 二进制文件
								pfile = open(file_path, 'rb')
								is_binary = True
						doc = pfile.read()
						pfile.close()
						return ctype, doc, is_binary, True 
					except Exception as e:
						# 读取文档出错
						return 'text/plain', 'An error occurred while reading the document', False, False

			else:
				# doc存在，但不支持这个后缀的doc
				#return 'text/plain', '403', False, False
				return get(root, '/', '', ex_parm) # 返回首页

		else: # is_dir is True
			# 目录
			index = get_index(file_path)
			if index is False:
				return get(root, './404.htm', '', ex_parm) # 去向404
			else:
				if index[-3:] == '.py':
					index = index[:-3] + '.do'
				return get(root, index, query_s, ex_parm) # 去向默认目录主页
	else:
		# 404 或 目录越级 403
		#return 'text/plain', '403 or 404', False, False
		return get(root, '/', '', ex_parm) # 返回首页	
			
