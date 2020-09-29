# coding=utf-8
# Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
f=open("bill.txt",'r',encoding='utf-8')
print(f.read(11))
print(f.tell())
print(f"ten cua file la:{}")