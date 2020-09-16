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
list=[]
n=int(input("So phan tu trong chuoi la:"))
for i in range(n):
    gt=int(input("gia tri phan tu thu {} la:".format(i)))
    list.append(gt)
print("chuoi la:", list )
# if list:
#     max_list, min_list = list[0], list[0]
#     for v in list:
#         if max_list < v:
#             max_list = v
#         elif min_list > v:
#             min_list = v
#     print(f"so lon nhat la {max_list} va so nho nhat la {min_list}")

#bai tap 3: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
# list = [0, 1, 2, 3,4, "abc"]
# s=str(input("Nhap chuoi"))
# list.extend(s)
# print("Chuoi moi la:", list)

#Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
# list = [0, 1, 2, 3,4, "abc"]
# len1 = int(input("Do dai phan dau la:"))
# print("Chuoi dau la:", list[0:len1])
# print("Chuoi sau la:", list[len1:])
#Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
        # Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
# n=int(input("So phan tu cua chuoi la:"))
# list=[]
# for i in range (n):
#     list.append(input())
# print("chuoi la:",list)
# max = 0
# giatri = ""
# if list:
#     for i in list:
#         if max<list.count(i):
#             max=list.count(i)
#             giatri=i
# print("Phần tử {} co so lan lap lai nhieu nhat la {}". format(i,max))

#Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        # + Độ dài từ 2 trở lên
        # + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
# list = []
# n=int(input("so chuoi trong list:"))
# for i in range(n):
#     gt=input("chuoi thu {} la:". format(i))
#     list.append(gt)
# print("List la:", list)
# x = 0
# for j in range(len(list)):
#     if len(list[j]) >= 2 and list[j][0] == list[j][-1]:
#         x+=1
#         print("So chuoi thoa man dieu kien la:", x)
#         break
# else:
#     print("Khong co chuoi nao thoa man dieu kien")
#Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
# n=int(input("So phan tu cua chuoi thu nhat la:"))
# m=int(input("So phan tu cua chuoi thu hai la:"))
# list1=[]
# list2=[]
# for i in range (n):
#     list1.append(input())
# print("chuoi thu nhat la:",list1)
# for j in range(m):
#     list2.append(input())
# print("chuoi thu hai la:", list2)
# for x in list1:
#     if x in list2:
#         print("Hai list co phan tu chung")
#         break
# else:
#     print("Hai list khong co phan tu chung")

#Bài 08: Cho list các số nguyên dương A.
        #Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
# A=[]
# n=int(input("So phan tu trong chuoi la:"))
# for x in range(n):
#     gt=int(input())
#     if gt < 0:
#         print("Moi nhap lai chuoi")
#     else:
#         A.append(gt)
# print("Chuoi la:", A)
# count = 0
# for i in range (len(A)):
#     for j in range (len(A)):
#         if A[i] > A[j] and i < j:
#             count +=1
# print("So luong tap thoa man dieu kien la:", count)