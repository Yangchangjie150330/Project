#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Yang chang jie
# @Time    : 2019/12/11 21:46
import os

BASE_DIRS = os.path.dirname(__file__)

settings = {
    "port": 8000,
    "debug": True,
    "static_path": os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "template")
}
