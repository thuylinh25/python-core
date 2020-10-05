# coding=utf-8
# Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng

# def read_nline(fname,n):
#     with open (fname) as f:
#         for i in range (n):
#             line=f.readline()
#             print(line)
# read_nline("months.txt",3)

# Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file

# my_list=["summer","autumn","winter"]
# my_list=map(lambda x: x+'\n', my_list)
# f=open("my_file.txt", 'a',encoding='utf-8')
# f.writelines(my_list)

# Bài 03: Viết chương trình trộn 2 file thành file mới

# merged_file=file2=""
# with open("months.txt",'r',encoding='utf-8') as f1:
#     merged_file=f1.read()
# with open("seasons.txt",'r',encoding='utf-8') as f2:
#     file2=f2.read()
# merged_file +='\n'
# merged_file +=file2
# with open('new_file.txt','w',encoding='utf=8') as f3:
#     f3.write(merged_file)

# Bài 04: Viết hàm
#         def get_file_size(file)
#     để lấy và trả về dung lượng của file

# cách 1:
# import os
# def get_file_size(file):
#     with open(file) as f:
#         f.seek(0,os.SEEK_END)
#         print('Dung luong cua file la',f.tell(), 'bytes')
# get_file_size("new_file.txt")

# cách 2:
# def get_file_size(file):
#     with open(file) as f:
#         f.seek(0,2)
#         print('Dung luong cua file la',f.tell(), 'bytes')
# get_file_size("new_file.txt")

# Bài 05: Viết hàm
#         def extract_characters(*file)
#     trả lại tập các ký tự trong các file

# import glob
# def extract_characters(*file):
#     character_list=[]
#     file=glob.glob('*.txt')
#     for file_elements in file:
#         with open(file_elements,'r',encoding='utf-8') as f:
#             character_list.append(f.read())
#     print(character_list)
# extract_characters("months","seasons")


# Bài 06: Viết chương trình tạp ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt

# import string
# for letters in string.ascii_uppercase:
#     with open(letters +'.txt','w',encoding='utf-8') as f:
#         f.write(letters)

# Bài 07: Đoạn chương trình sau in ra gì?
# number = 5.0
# try:
#     r = 10/number
#     print(r)
# except:
#     print("Oops! Error occurred.")
#
# output: 2.0

# Bài 08: Đoạn chương trình sau thực viện việc gì?
# try:
#     # đoạn code có thể gây ra lỗi
#     except (TypeError, ZeroDivisionError):
#     print("Python Quiz")

# vd đoạn code lỗi
# try:
#     number= "a"
#     r = 10/number
#     print(r)
# except (TypeError, ZeroDivisionError):
#     print("Python Quiz")

# Nếu đoạn code mắc các lỗi TypeError (khi number không phải là số) hoặc ZeroDivisionError (khi number bằng 0) thì in ra "Python Quiz"

# Bài 09: Kết quả output của đoạn chương trình sau là gì?
# def hoan_function():
#     try:
#         print('Monday')
#     finally:
#         print('Sunday')
# hoan_function()

# Output:
# Monday
# Sunday

# Bài 10: Kết quả của đoạn chương trình sau là gì?
# try:
#     print("throw")
# except:
#     print("except")
# finally:
#     print("finally")

# output:
# throw
# finally
