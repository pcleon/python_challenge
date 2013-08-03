#!/usr/bin/env python
#coding=utf-8
#学习urllib和pickle
import pickle
import urllib
file = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
txt = pickle.load(file)
print txt
for line in txt:
    line_char=''
    for k,v in line:
        line_char += k*v
    print line_char
