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
my_dict = {18: 2, 9: 3, 3: 4}
new_list=sorted(my_dict, key=lambda x: my_dict.keys())
# for i in x:
#     print(i)
#     my_dict={}.setdefault(i[])
# print(my_dict)
# # for i in my_dict.keys():
print(new_list)