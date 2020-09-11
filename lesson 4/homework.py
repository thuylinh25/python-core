# bai tap 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc
# import random
# old_list = [0, 1, 2, 3,4, "abc", 5, 6]
# new_list =[]
# while len(new_list) >= 0:
#     new_list.append(random.choice(old_list))
#     if len(new_list) ==5:
#         print("Chuoi moi la:",new_list)
#         print("Bai 1 DONE!")

#bai tap 1: Viết chương trình tính tổng, tích của các phần tử trong một list
my_list = input("Nhap chuoi:")
tong = 0
if my_list.isnumeric() == True:
    print("Nhap dung")
else:
    print("Nhap sai")


