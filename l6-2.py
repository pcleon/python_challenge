#!/usr/bin/env python
#学习python 压缩zip
import zipfile
dir = "files" + "/"
file = dir + "channel.zip"
zip_file = zipfile.ZipFile(file)
comment =''
file_name = '90052.txt'
zc =[]
while 1:
	f = open('files/%s' % file_name)
	next_num = f.read().split()[-1]
	f.close
	zc.append(zip_file.getinfo(file_name).comment)
	if next_num.isdigit():
		file_name = next_num + '.txt'
	else:
		break
print ''.join(zc)
