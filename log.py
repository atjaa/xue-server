#!/usr/bin/python
# -*- conding:utf-8 -*-
import time
class LogUtile():
    fileName = 'xue.log'
    def info(self,msg,path='app'):
        f=open(self.fileName,'a')
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(now + ' ' + path + ' ' + msg+'\n')
        f.close()
if __name__ == '__main__':
    log = LogUtile()
    log.info('aaa')
