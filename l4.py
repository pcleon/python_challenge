#!/usr/bin/env python
#学习正则和urllib
import urllib2 , urllib
import re
url_args = 8022
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url= base_url + str(url_args)
while True:
    content=urllib.urlopen(url).read()
    final_world = re.search('\w+$',content)
    url_args = final_world.group()
    url= base_url + str(url_args)
    print(url)
    file = open("4.result",'a')
    file.write(url + "\n")
    file.close()
