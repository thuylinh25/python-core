#Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
    #Sau đó, unpack các phần tử trong một tuple.
tuple = (12, 'abc', 2.3, 1+3j)
a,b,c,d = tuple
print(a)
print(b)
print(c)
print(d)

# Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
# tuple = (12, 'abc', 2.3, 1+3j)
# my_list=list(tuple)
# print(my_list)
# my_list=[12, 'abc', 2.3, 1+3j]
# my_tuple=tuple(my_list)
# print(my_tuple)

# Bài 02: Viết chương trình đảo ngược một tuple.
# my_tuple = ("ab", 2, 3, 4)
# cách một:
# new_tuple = tuple(reversed(my_tuple))
# print(new_tuple)
# cách hai:
# print(my_tuple[::-1])

# Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
# list=["a", "b", (1, 2,"b"), -23]
# for x in range(len(list)):
#     if type(list[x]) == tuple:
#         print(len(list[:x]))
#         break
# else:
#     print(len(list))

# Bài 04: Cho 1 list chứa các tuple không rỗng.
#     Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
#     Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
# list=[(2, 5), (4, 1), (0,0)]
# print("final_list:",sorted(list, key= lambda x:x[-1]))

# Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
# list=[(2, 5), (4, 1,4), (0,5,0)]
# print(min(list,key = lambda x:x[1]))

# Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
# tuple=("a","b","c","d","e",(2, 5), (4, 1), (0, 0))
# print("phan tu thu tư la:",tuple[3])
# print("phan tu thu tu tư cuoi len:", tuple[-4])

# Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
# tuple1= ("a","b","c","d",(2,5))
# tuple2=("e",(2, 5), (4, 1), (0, 0))
# for i in tuple1:
#     if i in tuple2:
#         print("2 tuple co phan tu chung")
#         break
# else:
#     print("2 tuple khong co phan tu chung")

# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
# tuple= ("a","a",1,2)
# for i in tuple:
#     if tuple.count(i)==len(tuple):
#         print("giong")
#         break
#     else:
#         print("khong giong")
#         break

# Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
# tuple=(2,3,1.1,2.1,0)
# print(sum(tuple))
# x=0
# for i in tuple:
#     if type(i)==float and i>x:
#         max=i
# print(max)

# Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
# list=["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
# a,b,c,d=list
# print(a[-2:])
# print(b[-3:])
# print(c[-3:])
# print(d[-3:])

# Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
# list=["abc","edff","ggggg"]
# x=0
# for i in list:
#     if len(i)>0:
#         max=i
# print(max)
