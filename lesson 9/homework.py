#--coding:utf-8--
# Bài 00. Vi?t m?t ch??ng trình ?? l?y ra tên class c?a m?t object?
# class A:
#         pass
# ten = A()
# print(ten.__class__.__name__)

# Bài 01: Xem code ?ã có trong file btvn_01_dog.py.
#     Vi?t ?o?n ch??ng trình vào ti?p trong file ?ó ?? gi?i quy?t yêu c?u sau:
#         - T?o ra 3 ??i t??ng Dog v?i các thu?c tính v? age khác nhau:
#             name        age
#             Fake         2
#             Mickey       7
#             Fuk          5
#         - Sau ?ó, vi?t m?t hàm get_biggest_number(*args) nh?n vào nhi?u tham s?, sau ?ó tr? v? s? l?n nh?t.
#         - Và d?a trên hàm này, hay tìm và in ra có d?ng nh? sau:
#             The oldest dog is 7 years old.

# class Dog:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Fake = Dog("Fake", 2)
# Mickey = Dog("Mickey", 7)
# Fuk = Dog("Fuk", 5)
#
# def get_biggest_number(*args):
#     return max(args)
# print("The oldest dog is {} years old".format(get_biggest_number(Fake.age,Mickey.age,Fuk.age)))

# Bài 02. Xem code ?ã có trong file btvn_02_pet.py.
#     Vi?t ?o?n ch??ng trình vào ti?p trong file ?ó ?? gi?i quy?t yêu c?u sau:
#         - Hãy t?o ra class Pet ?? ch?a các ??i t??ng c?a class Dog, class Pet này ??c l?p v?i class Dog (hay Pet ko k? th?a t? Dog)
#         - Sau ?ó, t?o 4 ??i t??ng ki?u Dog và gán thành thu?c tính c?a 1 ??i t??ng ki?u Pet
#             name        age
#             Tom          6
#             Jerry        9
#             Butt         3
#             Wine         1
#         - Code ?o?n ch??ng trình ?? in ra ???c nh? sau:
#             I have 4 dogs.
#             Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
#             And they're all mammals, of course.