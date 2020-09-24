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
def is_pangram(str, alphabet):
  alphabet="abcdefghijklmnopqrstuvwxyz"
  for i in alphabet:
      if i not in str.lower():
          return False
      elif i in str.lower() and len(set(i))<=len(set(str.lower())):
          return True

print(is_pangram("quick brown fox jumps over the lazy dog","abcdefghijklmnopqrstuvwxyz"))

# str=("e quick brown fox jumps over the lazy dog")
# print(len(set(str)))