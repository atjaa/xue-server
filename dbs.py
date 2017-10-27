# -*- coding: UTF-8 -*-
import MySQLdb as mdb
class dbmanager():
    """docstring for """
    def __init__(self):
        self.conn = mdb.connect('192.168.0.2','root','pl!112233','xue')
        self.conn.autocommit(1)
        self.cursor = self.conn.cursor(cursorclass=mdb.cursors.DictCursor)
    def close(self):
        self.cursor.close()
        self.conn.close()
    def rollback(self):
        self.conn.rollback()
    def insert(self,sql,values,ifcloseconn=True):
        try:
            self.cursor.execute(sql,values)
            #self.conn.commit()
        except Exception,e:
            print str(e)
            self.conn.rollback()
        finally:
            if(ifcloseconn):
                self.cursor.close()
                self.conn.close()
    def update(self,sql,values,ifcloseconn=True):
        try:
            self.cursor.execute(sql,values)
            #self.conn.commit()
        except Exception,e:
            print str(e)
            self.conn.rollback()
        finally:
            if(ifcloseconn):
                self.cursor.close()
                self.conn.close()
    def select(self,sql,values,num,ifcloseconn=True):
        try:
            count = self.cursor.execute(sql,values)
            results = self.cursor.fetchmanyDict(num)
            return results
        except Exception as e:
            print str(e)
        finally:
            if(ifcloseconn):
                self.cursor.close()
                self.conn.close()
    def closeconn(self):
        self.cursor.close()
        self.conn.close()
if __name__=='__main__':
    '''sql='insert into user(name,passwd,nickname) values(%s,%s,%s)'
    values=['黑牛','123','小黑']
    db = dbmanager()
    db.insert(sql,values)'''
    sql='select * from user where name=%s'
    values=['黑牛']
    db = dbmanager()
    results = db.select(sql,values,1)
    print results
