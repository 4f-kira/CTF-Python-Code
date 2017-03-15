#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import itertools
import time


url = 'http://429aa454be8e476381f43c6a369b720bfe41191e1c254db8.ctf.game/'
hea = {"cookie":"token=hello1"}

def post():
	r = requests.get(url=url,headers=hea)
	print r.content

post()