#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
class CookieManager():
    def setCookie(self,response,key,text):
        response.set_cookie(key,text,secret='xue-secret-key',path='/',domain="xue37.cn",httponly=True)
    def getCookie(self,request,key):
        return request.get_cookie(key,secret='xue-secret-key')
    def delCookie(self,response,key):
        response.delete_cookie(key,path='/',domain="xue37.cn")
