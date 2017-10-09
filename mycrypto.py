# -*- coding: UTF-8 -*-
import md5
class mycrypto():
    def encrypt(self, text):
        md=md5.new()
        md.update(text)
        return md.hexdigest()
if __name__ == '__main__':
    pc = mycrypto()      #初始化密钥
    e = pc.encrypt("123")
    print e
    s = pc.encrypt("00000000000000000000000000")
    print s
