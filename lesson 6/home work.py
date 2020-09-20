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
# new_list={}
# for (key, value) in my_dict.items():
#     for key in sorted(my_dict.keys(), reverse=True):
#         new_list[key]=value
#         if len(new_list) == 3:
#             print(new_list)

# Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
# dict={}
# n=int(input('So phan tu trong dict la:'))
list1=[]
list1.append(input())
if len(list1)>5:
    print(list1)
# for (key, value) in dict.items():
#     if n > 3 and len(list) > 5:
#         dict[key] = list
#         print(dict)

