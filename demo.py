#!/usr/bin/python
#-*-coding:utf-8-*- 

import time
import urllib,urllib2,cookielib,re

'''
url = 'http://test.com/s?wd=哈哈'
url = url.decode('gbk', 'replace')
print urllib.quote(url.encode('utf-8', 'replace'))



try:
    print "Waiting 10 seconds"
    time.sleep(10)

except KeyboardInterrupt:
    print "Caught KeyboardInterrupt, terminating workers"


class A:
    member = "this is a test."
    def __init__(self):
        pass
 
    @classmethod
    def Print1(cls):
       
        print "print 1: ", cls.member
         
    def Print2(self):
        print "print 2: ", self.member
            
         
    @classmethod    
    def Print3(paraTest):
        print "print 3: ", paraTest.member
 
a = A()
A.Print1()  
a.Print2()   
A.Print3()   

#中文哈哈'''