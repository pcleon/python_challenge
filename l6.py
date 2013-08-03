#!/usr/bin/env python
#使用到split,isdigit
dir = "files" + "/"
file = dir + "90052.txt"
while 1:
	file = open(file)
	letter = file.read()
	file.close()
	get_last=''.join(letter.split(" ")[-1:])
	if get_last.isdigit():
		file = dir + get_last + '.txt'
		print file
	else:
		print letter
		break
