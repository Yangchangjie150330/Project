#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Yang chang jie
# @Time    : 2019/12/11 21:57

import tornado.web
import views.index
from config import settings


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ("/", views.index.IndexHander)
        ]
        super(Application, self).__init__(handlers, **settings,)
