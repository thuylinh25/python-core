# B�i 01: Vi?t ch??ng tr�nh ?? ??c n d�ng ??u trong 1 file text, v?i n ???c nh?p t? ng??i d�ng
#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
f=open("bill.txt",'r',encoding='utf-8')
str=f.read()
print ('Noi dung file cua ban la:\n', str)
# n=int(input())
# print(f_read.readline(n))