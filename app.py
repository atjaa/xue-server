#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bottle import route,run,request,response,hook
import service
@hook('after_request')
def enable_cors():
    # 设置只允许www.xue37.cn 和180.76.239.61 跨域
    if('xue37.cn' in request.get('HTTP_HOST')):
        response.headers['Access-Control-Allow-Origin'] = 'http://www.xue37.cn'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
@route('/bot/user/:name')
def getUser(name):
    user = service.UserService()
    res = user.getUser(name)
    return res
@route('/bot/visitcount',method=['post','get'])
def gevisitcounttUser():
    user = service.UserService()
    res = user.visitCount()
    return res
@route('/bot/searchbook',method=['post','get'])
def searchbook():
    utype = request.forms.get('utype')
    uvalue = request.forms.get('uvalue')
    currentpage = request.forms.get('currentpage')
    if(not utype == None or not uvalue == None or not currentpage == None):
        book = service.Bookservice()
        res = book.searchbook(utype,uvalue,currentpage)
        return res
    else:
        return 'err'
@route('/bot/getbooklist',method=['post','get'])
def getbooklist():
    menuid = request.forms.get('menuid')
    currentpage = request.forms.get('currentpage')
    books = service.Bookservice()
    res = books.getBooklist(menuid,currentpage)
    return res
@route('/bot/addbook',method=['post','get'])
def addbook():
    param ={}
    param['menuid'] = request.forms.get('menuid')
    param['author'] = request.forms.get('author')
    param['bookname'] = request.forms.get('bookname')
    param['introduction'] = request.forms.get('introduction')
    param['pan'] = request.forms.get('pan')
    param['source'] = request.forms.get('source')
    books = service.Bookservice()
    user = service.UserService()
    res = user.iflogin(request)
    if res=='false':
        return '当前用户未登陆'
    username = res.get('username')
    usertype = user.getUser(username)
    if(not (usertype.get('type') == '1' or usertype.get('type') == '3')):
        return '当前用户没有权限'
    books = service.Bookservice()
    res = books.getBooklistByName(param.get('bookname'))
    if(res == 'err' or len(res.get('res'))>0):
        return "此图书已存在"
    else:
        br = books.addbook(param,username)
        if(br=="success"):
            return "success"
        else:
            return "添加失败"
@route('/bot/getbookcomment',method=['post','get'])
def getbookcomment():
    bookid = request.forms.get('bookid')
    books = service.Bookservice()
    res = books.getBookComments(bookid)
    return res
@route('/bot/addchan',method=['post','get'])
def addchan():
    bookid = request.forms.get('bookid')
    books = service.Bookservice()
    res = books.addchan(bookid)
    return res
@route('/bot/addbookcomment',method=['post','get'])
def addbookcomment():
    param ={}
    param['bookid'] = request.forms.get('bookid')
    param['comment'] = request.forms.get('comment')
    books = service.Bookservice()
    user = service.UserService()
    res = user.iflogin(request)
    if res=='false':
        return '当前用户未登陆'
    username = res.get('username')
    books = service.Bookservice()
    br = books.addbookcomment(param,username)
    if(br=="success"):
        return "success"
    else:
        return "添加失败"
@route('/bot/iflogin',method=['post','get'])
def iflogin():
    user = service.UserService()
    res = user.iflogin(request)
    return res
@route('/bot/login',method=['post','get'])
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if(not username == None or not password == None):
        user = service.UserService()
        return user.login(username,password,response)
    else:
        return 'param err'
@route('/bot/logout',method='post')
def logout():
    username = request.forms.get('username')
    user = service.UserService()
    user.logout(username,response)
    return 'success'
@route('/bot/regist',method='post')
def regist():
    username = request.forms.get('username')
    password = request.forms.get('password')
    nickname = request.forms.get('nickname')
    phone = request.forms.get('phone')
    if(not username == None or not password == None or not nickname == None or not phone == None):
        user = service.UserService()
        return user.regist(username,password,nickname,phone,response)
    else:
        return 'param err'

run(host='0.0.0.0',port=8080)
