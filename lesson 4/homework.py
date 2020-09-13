# bai tap 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc
# import random
# old_list = [0, 1, 2, 3,4, "abc", 5, 6]
# new_list =[]
# for i in range(5):
#     new_list.append(random.choice(old_list))
# print("Chuoi moi la:",new_list)


#bai tap 1: Viết chương trình tính tổng, tích của các phần tử trong một list
# n=int(input("So phan tu cua chuoi la:"))
# list=[]
# for i in range (n):
#     list.append(input())
# a=0
# b=1
# try:
#     for v in list:
#         a += int(v)
#         b *= int(v)
# except:
#     a="chuỗi sai"
#     b="chuỗi sai"
# print("chuoi la:", list)
# print ("tong chuoi bang:" +str(a))
# print ("tich chuoi bang:" +str(b))

#bai tap 2: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list
# list=[]
# n=int(input("So phan tu trong chuoi la:"))
# for i in range(n):
#     gt=int(input("gia tri phan tu thu {} la:".format(i)))
#     list.append(gt)
# print("chuoi la:", list )
# if list:
#     max_list, min_list = list[0], list[0]
#     for v in list:
#         if max_list < v:
#             max_list = v
#         elif min_list > v:
#             min_list = v
#     print(f"so lon nhat la {max_list} va so nho nhat la {min_list}")

#bai tap 3: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
