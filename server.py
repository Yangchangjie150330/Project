#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Yang chang jie
# @Time    : 2019/12/11 21:46


import tornado.web
import tornado.httpserver
import tornado.ioloop
from application import Application


if __name__ == '__main__':
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.current().start()
