#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 临时变动当前工作目录
import os, sys
class ExecPath:
	def __init__(self):
		self._old_path = os.getcwd()
		self._new_path = self._old_path
		self._already_exists_in_syspath = False
	def set(self, path):
		assert os.path.isdir(path)
		assert os.path.isabs(path)
		self._new_path = path
		# 设置当前工作路径
		os.chdir(self._new_path)
		# 将当前工作路径添加到sys.path中
		if not self._new_path in sys.path:
			#sys.path.insert(1, self._new_path)
			sys.path.append(self._new_path)
			self._already_exists_in_syspath = False
		else:
			self._already_exists_in_syspath = True
			
	def reset(self):
		# 恢复之前的工作路径
		os.chdir(self._old_path)
		# 清理sys.path
		if self._already_exists_in_syspath is False:
			sys.path.remove(self._new_path)