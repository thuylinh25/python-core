# Bài 01: Vi?t ch??ng trình ?? ??c n dòng ??u trong 1 file text, v?i n ???c nh?p t? ng??i dùng
#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
f=open("bill.txt",'r',encoding='utf-8')
str=f.read()
print ('Noi dung file cua ban la:\n', str)
# n=int(input())
# print(f_read.readline(n))