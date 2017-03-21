#! /usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import requests
import urllib
aa = ')\xa5\xa1\xec>)F\x119\xbc\xfcor\x11\xd9\xa4'
url = "http://218.2.197.235:23737/"
cookie = {"PHPSESSID":"qe6s9hjkpqrfcv07hf1ous71m7"}
iv = ["\x00"]*16
cipher = ['\x00', 236, 46, 92, 100, 49, 71, 211, 255, 106, 69, 3, 16, 13, 233, 54]
plain = "admin"
plain += 11*chr(11)
plain = list(plain)
# for i in xrange(16,17):
# 	for j in xrange(1,i):
# 		iv[16-i+j] = chr(cipher[16-i+j] ^ i)
# 	for x in xrange(218,256):
# 		iv[16-i] = chr(x)
# 		tmp_iv = "".join(iv)
# 		cookie['token'] = urllib.quote(base64.b64encode(tmp_iv))
# 		print cookie
# 		try:
# 			r = requests.get(url, cookies=cookie)
# 			print "%s"%x, r.content
# 		except:
# 			print cipher
# 			print x
# 			exit();
# 		if "ctfer!" in r.content:
# 			break
# 	else:
# 		print cipher
# 		exit();
# 	cipher[16-i] = x ^ i
# 	break
# print cipher
# for x in cipher:
# 	print hex(x)
plain = ['a', '\x88', 'C', '5', '\n', ':', 'L', '\xd8', '\xf4', 'a', 'N', '\x08', '\x1b', '\x06', '\xe2', '=']
for x in xrange(193,256):
	plain[0] = chr(x)
	tmp_p = "".join(plain)
	cookie['token'] = urllib.quote(base64.b64encode(tmp_p))
	print cookie
	r = requests.get(url, cookies=cookie)
	print x
	print r.content
	if "NJCTF" in r.content:
		break