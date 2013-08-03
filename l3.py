#!/usr/bin/env python
#简单的文件打开关和列表定位
right_num=0
file = open("files/txt","r")
for line in file.readlines():
    for index in range(3,len(line)):
        if ( line[index].islower() ):
            left_char = line[index-3:index]
            if ( line[index-4].islower() and line[index-3].isupper() and  line[index-2].isupper() and line[index-1].isupper() ):
                if ( line[index+1].isupper() and line[index+2].isupper() and line[index+3].isupper() and line[index+4].islower() ):
                    print line[index] 
