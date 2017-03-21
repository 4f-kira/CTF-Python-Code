#coding:utf-8
import base64
import urllib
import requests

iv = base64.b64decode("IawOWe0ggWo=")
cipher = base64.b64decode("kPJY6KEX1oo=")
plain = "guest" + "\x03\x03\x03"      #\x03 是padding  
dest_plain = "admin" + "\x03\x03\x03"
 
def sxor(s1,s2):    #异或好函数
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def send_payload(x):
    url = "http://wargame.kr:8080/dun_worry_about_the_vase/main.php"
    hea = {"Cookie":"L0g1n={}".format(urllib.quote(x))}
    res = requests.get(url=url,headers=hea).content
    if "padding error" in res:
        return 0
    else:
        print res
        return 1

def padding(l,test):
    if l > 1:
        tmp = chr(test) + sxor(imtermediary,chr(l)*(l-1))
    else:
        tmp = chr(test)
    return "{:\x00>8}".format(tmp)


def make_ses(x):
    return base64.b64encode(x)+base64.b64encode(cipher)

imtermediary = ""
ptxt = ""

for i in range(1,9):
    for j in range(255):
        tmp = padding(i,j)
        #print "[+] checking:{}".format(hex(j))
        if send_payload(make_ses(tmp)):
            imtermediary = chr(j ^ i) + imtermediary 
            ptxt = sxor(imtermediary[::-1],iv[::-1])[::-1]
            print "[!] find:{}\t{}\t{}\t{}".format(imtermediary,imtermediary.encode('hex'),ptxt,ptxt.encode('hex'))
            #raw_input()
            break

print base64.b64encode(sxor(sxor(ptxt,iv),dest_plain))


