# Bài 01: Viết hàm
#         def max_min(*numbers)
#     trả lại cả giá trị max, min của nhiều số được truyền vào

# def max_min(*numbers):
#     print(max(numbers))
#     print(min(numbers))
#     return max(numbers),min(numbers)
# max_min(2,4,9)

# Bài 02: Viết hàm
#         def reverse_string(str)
#     trả lại chuỗi đảo ngược của chuỗi str

# def reverse_string(str):
#     reversed_str=''.join(reversed(str))
#     print(reversed_str)
#     return reversed_str
# reverse_string("what a beautiful day")

# Bài 03: Viết hàm
#         def is_perfect(n)
#     để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
#     Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi

# def is_perfect(n):
#     for p in range(n):
#         if n==(2**p-1) * 2**(p-1):
#             print(f"{n} la so hoan hao")
#             break
#     else:
#         print(f"{n} khong la so hoan hao")
# is_perfect(495)

# Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False

# def is_prime(n):
#     for m in range(2,n):
#         if n%m!=0:
#             return True
#             break
#         else:
#             return False
# print(is_prime(4))

# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str

# def count_upper_lower(chuoi):
#     i= sum(map(str.islower, chuoi))
#     print(f"tong chu cai viet hoa la {i}")
#     j= sum(map(str.isupper, chuoi))
#     print(f"tong chu cai viet thuong la {j}")
#     return i,j
# count_upper_lower("HellO")

# Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần


# Bài 07: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j

#cach 1:
# def create_matrix(n,m):
#     matrix=[]
#     for i in range (n):
#         matrix.append([])
#         for j in range (m):
#             matrix[i].append(i*j)
#     return matrix
# print(create_matrix(4,5))

#cach 2:
# def create_matrix(n,m):
#     return[[i*j for i in range(n)]for j in range(m)]
# print(create_matrix(4,5))

# Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h

# def body_mass_index(m,h):
#     bmi=m/(h**2)
#     return bmi
# print(body_mass_index(49,1.5))
#
# def bmi_information(m, h):
#     bmi = m / (h ** 2)
#     if bmi < 18.8:
#         print("gay")
#     elif bmi >= 25:
#         print("beo")
#     else:
#         print("binh thuong")
#
# bmi_information(49,1.5)

# Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str

# def change_upper_lower(str):
#     s_new=""
#     for i in str:
#         if "a"<=i<="z":
#             s_new+=i.upper()
#         elif "A"<=i<="Z":
#             s_new+=i.lower()
#     return s_new
# print(change_upper_lower("HeLLo"))

# Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
# def odd_count(n):
#    last_digit = n % 10
#    first_digit= n // 10
#    if n<10 and last_digit % 2 == 0:
#        return 0
#    if last_digit % 2 != 0:
#        return 1 + odd_count(first_digit)
#    else:
#        return 0 + odd_count(first_digit)
#
# print(odd_count(19922610))

# Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy
# def recursive_tribo(n):
#     if n == 1 or n==2:
#         return 1
#     elif n==3:
#         return 2
#     else:
#         return recursive_tribo(n-1)+recursive_tribo(n-2)+recursive_tribo(n-3)
#
# print(recursive_tribo(6))

def tribo(n):
    for i in 


