#Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
    #Sau đó, unpack các phần tử trong một tuple.
# tuple = (12, 'abc', 2.3, 1+3j)
# a,b,c,d = tuple
# print(a)
# print(b)
# print(c)
# print(d)

# Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
# tuple = (12, 'abc', 2.3, 1+3j)
# my_list=list(tuple)
# print(my_list)
# my_list=[12, 'abc', 2.3, 1+3j]
# my_tuple=tuple(my_list)
# print(my_tuple)

# # # Bài 02: Viết chương trình đảo ngược một tuple.
# my_tuple = ("ab", 2, 3, 4)
# my_tuple = tuple(reversed(my_tuple))
# print(my_tuple)

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
