#--coding:utf-8--
# B�i 00. Vi?t m?t ch??ng tr�nh ?? l?y ra t�n class c?a m?t object?
# class A:
#         pass
# ten = A()
# print(ten.__class__.__name__)

# B�i 01: Xem code ?� c� trong file btvn_01_dog.py.
#     Vi?t ?o?n ch??ng tr�nh v�o ti?p trong file ?� ?? gi?i quy?t y�u c?u sau:
#         - T?o ra 3 ??i t??ng Dog v?i c�c thu?c t�nh v? age kh�c nhau:
#             name        age
#             Fake         2
#             Mickey       7
#             Fuk          5
#         - Sau ?�, vi?t m?t h�m get_biggest_number(*args) nh?n v�o nhi?u tham s?, sau ?� tr? v? s? l?n nh?t.
#         - V� d?a tr�n h�m n�y, hay t�m v� in ra c� d?ng nh? sau:
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

# B�i 02. Xem code ?� c� trong file btvn_02_pet.py.
#     Vi?t ?o?n ch??ng tr�nh v�o ti?p trong file ?� ?? gi?i quy?t y�u c?u sau:
#         - H�y t?o ra class Pet ?? ch?a c�c ??i t??ng c?a class Dog, class Pet n�y ??c l?p v?i class Dog (hay Pet ko k? th?a t? Dog)
#         - Sau ?�, t?o 4 ??i t??ng ki?u Dog v� g�n th�nh thu?c t�nh c?a 1 ??i t??ng ki?u Pet
#             name        age
#             Tom          6
#             Jerry        9
#             Butt         3
#             Wine         1
#         - Code ?o?n ch??ng tr�nh ?? in ra ???c nh? sau:
#             I have 4 dogs.
#             Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
#             And they're all mammals, of course.