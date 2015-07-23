#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from jinja2 import Environment, FileSystemLoader
from jinja2 import TemplateSyntaxError, TemplateNotFound, UndefinedError, TemplateError
class TemplParse:
	# 解析模板
	#
	# 参数:
	#	template_root, 模板根目录
	#	template_file, 模板文件相对（根）路径 
	#	arg, karg （可变参数） 模板context
	# Returns:
	#	doc 解释后的文档或异常信息
	#	return_code 成功解释返回True, 否则返回False
	def get_doc(self, template_root, template_file, *args, **kwargs):
		try:
			return_code = False
			env = Environment(loader=FileSystemLoader(template_root))
			template = env.get_template(template_file)
			doc = template.render(*args, **kwargs)
			return_code = True
		except TemplateSyntaxError as e:
			doc = 'Err: Template Syntax Error, ' + str(e)
		except TemplateNotFound as e:
			doc = 'Err: Template Not Found, ' + str(e)
		except UndefinedError as e:
			doc = 'Err: Template Undefined Error, ' + str(e)
		except TemplateError as e:
			doc = 'Err: Template Error, ' + str(e)
		except Exception as e:
			doc = str(e)
		finally:
			return doc, return_code

	# 获取文件内容
	def get_text(self, file_name, encoding='utf-8'):
		return_code = False
		if file_name == '': return '', return_code
		try:
			res = ''
			pfile = open(file_name, 'r', encoding=encoding)
			res = pfile.read()
			pfile.close()
			return_code = True
		except Exception as e:
			res = str(e)
		except:
			res = 'Error, open/read file:' + file_name
		finally:
			return res, return_code


	# 不推荐的使用方式
	def __init__(self):
		self._temlroot = ''
		self._env = None
	def template_root(root):
		assert os.path.isdir(root)
		self._temlroot = root
		self._env = Environment(loader=FileSystemLoader(root))
	def load(template_file):
		assert os.path.isfile(os.path.join(self._temlroot, template_file))
		template = env.get_template(template_file)
	def render(*arg, **karg):
		return template.render(arg, karg)
'''
eg.
resource/template/jinja_test.htm:

<html>
<body>
{{ hello }} world! {{ var_i }} am Deel
</body>
</html>

from jinja_parse import TemplParse
root = 'resource/template'
templ_file = 'jinja_test.htm'
context = {'hello': 'Hello', 'vai_i': 'I'}
doc, return_code = TemplParse().get_doc(root, templ_file, context)
#doc, return_code = TemplParse().get_doc(root, templ_file, hello='Helloo', var_i='I')
print(doc, return_code)

'''

'''
or

from jinja2 import Environment, FileSystemLoader
from jinja2 import TemplateSyntaxError, TemplateNotFound, UndefinedError, TemplateError
try:
	return_code = False
	env = Environment(loader=FileSystemLoader('D:/www/openshift/simplevideo/www/resource/template'))
	template = env.get_template('jinja_test.htm')
	doc = template.render(hello='Hello', var_i='I')
	return_code = True
except TemplateSyntaxError as e:
	doc = 'Err: Template Syntax Error, ' + str(e)
except TemplateNotFound as e:
	doc = 'Err: Template Not Found, ' + str(e)
except UndefinedError as e:
	doc= 'Err: Template Undefined Error, ' + str(e)
except TemplateError as e:
	doc = 'Err: Template Error, ' + str(e)
except Exception as e:
	doc = str(e)
	
print(doc, return_code)

'''
