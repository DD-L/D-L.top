#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#import pdb
#import types

import os, sys
_curfullpath = os.path.dirname(os.path.realpath(__file__))
_dbdir = '../libs/db/mysql/'
_dbfullpath = os.path.join(_curfullpath, _dbdir)
_dbfullpath = os.path.normpath(_dbfullpath)
if not _dbfullpath in sys.path:
	#sys.path.insert(1, _dbfullpath)
	sys.path.append(_dbfullpath)

from sv_db import *
'''
db_init 包含敏感信息，暂不对外开放
'''
def db_init(cover = False):
	pass


def add_token(token, extra, level = 1):
	db = SvDb()
	db.add_token(token, extra, level)
	db.commit()
