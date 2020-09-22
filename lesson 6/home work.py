# # Bài 00: Viết chương trình tính tích value của các phần tử trong một dict
# my_dict = {1: 2, 2: 3, 3: 4}
# tich=1
# for i in my_dict:
#     tich=tich*my_dict[i]
# print(tich)

# Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
# my_dict = {"a": 26, 1: 3, 2: 4}
# max= my_dict["a"]
# min= my_dict ["a"]
# for i in my_dict.values():
#     if i> max:
#         max=i
#     if i <min:
#         min=i
# print(f"gia tri lon nhat la {max}, gia tri nho nhat la {min}")

# Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
# my_dict = {18: 2, 2: 3, 3: 4}
# new_dict = {}
# for (key, value) in my_dict.items():
#     for key in sorted(my_dict.keys()):
#         new_dict[key]= value
# print(new_dict)

# Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
# my_dict = {18: 2, 2: 3, 3: 4, 5:3}
# new_dict={}
# for (key,value) in my_dict.items():
#     if value not in new_dict.values():
#         new_dict[key]=value
# print(new_dict)

# Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
# my_dict = {18: 2, 2: 3, 3: 4, 5:3}
# new_dict={}
# for (key, value) in my_dict.items():
#     for key in sorted(my_dict.keys(), reverse=True):
#         new_dict[key]=value
#         if len(new_dict) == 3:
#             print(new_dict)

# Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
# my_dict={}
# my_dict[1]=[1,2,3,4,5]
# my_dict["a"]=[1,2,"b","c","d"]
# my_dict[("c","d")]=[0,9,8,7,6]
# print(my_dict)
# for i in my_dict:
#     print(my_dict[i][4])

# Bài 06:Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
# dict1 = {18: 2, 2: 3, 3: 4, 5:3}
# dict2 = {"a": 26, 1: 3, 2: 3}
# for (key, value) in dict1.items():
#     if (key, value) in dict2.items():
#         print((key, value))
# else:
#     print("khong co phan tu chung")

# Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
# Ví dụ:
#     dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
#     keys = ["name", "salary"]
#     Output: {'name': 'Kelly', 'salary': 8000}

# dict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
# new_dict={}
# for (key, value) in dict.items():
#     if key=="name" or key=="salary":
#         new_dict[key]=value
# print(new_dict)

# Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
# my_dict = {18: 2, 2: 4, 3: 10, 5:6}
# new_dict={}
# my_dict=sorted(my_dict.items(), reverse=True, key=lambda x:x[1])
# for i in my_dict:
#     new_dict[i[0]]=i[1]
#     if len(new_dict)==3:
#         print(new_dict)

# Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
# Ví dụ:
#     Input: ‘Stringings’
#     Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}

# string="Stringings"
# tuple={}
# for i in string:
#   tuple[i]=string.count(i)
# print(tuple)

# Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
# string = ' Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản '
# string2= string.split(" ")
# tuple={}
# for i in string2:
#   tuple[i]=string2.count(i)
# print(tuple)

# Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:

