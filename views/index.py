#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Yang chang jie
# @Time    : 2019/12/11 22:01

from tornado.web import RequestHandler


class IndexHander(RequestHandler):
    def get(self, *args, **kwargs):
        return self.write("hello worldxxxx")
