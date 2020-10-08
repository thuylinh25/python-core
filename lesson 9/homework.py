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

# class Dog:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#             return f'{self.name} is {self.age} years old'
#
#     def speak(self, sound):
#             return f'{self.name} says {sound}'
#
# class RussellTerrier(Dog):
#     def run(self, speed):
#         return f'{self.name} runs {speed}'
#
# class Bulldog(Dog):
#     def run(self, speed):
#         return f'{self.name} runs {speed}'
# class Pet:
#     my_dogs=[]
#     def __init__(self,dogs):
#         self.dogs = dogs
#
# my_dogs=[Dog("Tom",6), Dog("Jerry",9), Dog("Butt",3), Dog("Wine",1)]
# my_pet=Pet(my_dogs)
# print("I have {} dogs.".format(len(my_pet.dogs)))
# for dog in my_pet.dogs:
#     print("{} is {}.".format(dog.name, dog.age))
# print("And they're all {}s, of course.".format(dog.species))

# B�i 03. S? d?ng ti?p file btvn_02_pet.py sau khi ?� code xong B�i 02.
#     Gi?i quy?t y�u c?u sau:
#         - Th�m thu?c t�nh is_hungry = True cho class Dog
#         - Th�m m?t method eat() ?? thay ??i gi� tr? cho is_hungry th�nh False khi n� ???c g?i ??n
#         - Ki?m tra v� in ra
#             My dogs are not hungry.
#         n?u nh? t?t c? c�c Dog trong Pet ??u c� is_hungry = False, ng??c l?i th� in ra
#             My dogs are hungry.
#         - Cu?i c�ng c� th? in ra ???c ki?u nh? sau:
#             I have 4 dogs.
#             Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
#             And they're all mammals, of course.
#             My dogs are not hungry.

# class Dog:
#     species = 'mammal'
#     is_hungry = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         self.is_hungry = False
#
#     def description(self):
#             return f'{self.name} is {self.age} years old'
#
#     def speak(self, sound):
#             return f'{self.name} says {sound}'
#
# class RussellTerrier(Dog):
#     def run(self, speed):
#         return f'{self.name} runs {speed}'
#
# class Bulldog(Dog):
#     def run(self, speed):
#         return f'{self.name} runs {speed}'
# class Pet:
#     my_dogs=[]
#     def __init__(self,dogs):
#         self.dogs = dogs
#
# my_dogs=[Dog("Tom",6), Dog("Jerry",9), Dog("Butt",3), Dog("Wine",1)]
# my_pet=Pet(my_dogs)
# print("I have {} dogs.".format(len(my_pet.dogs)))
# for dog in my_pet.dogs:
#     print("{} is {}.".format(dog.name, dog.age))
# print("And they're all {}s, of course.".format(dog.species))
#
# are_my_dogs_hungry = False
# for dog in my_pet.dogs:
#     if dog.is_hungry:
#         are_my_dogs_hungry = True
# if are_my_dogs_hungry:
#     print("My dogs are hungry")
# else:
#     print("My dogs are not hungry")

# B�i 04. Xem code ?� c� trong file btvn_04_dog_walking.py.
#     Gi?i quy?t y�u c?u sau:
#         - Th�m method walk() v�o class Pet v� Dog. Khi g?i ??n h�m walk() trong Pet th� v?i m?i ??i t??ng c?a Dog trong Pet
#         s? g?i ??n h�m walk() t??ng ?ng.
#         - Vi?t ?o?n ch??ng tr�nh ?? in ra nh? sau:
#             Tom is walking!
#             Jerry is walking!
#             Butt is walking!

#
# class Dog:
#     species = 'mammal'
#     is_hungry = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f"{self.name} is walking"
#
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
#
#     def eat(self):
#         self.is_hungry = False
#
#
# class RussellTerrier(Dog):
#     def run(self, speed):
#         return f'{self.name} runs {speed}'
#
#
# class Bulldog(Dog):
#     def run(self, speed):
#         return f'{self.name} runs {speed}'
#
# class Pet:
#
#     dogs = []
#
#     def __init__(self, dogs):
#         self.dogs = dogs
#
#     def walk(self):
#         for dog in self.dogs:
#             print(dog.walk())
#
# my_dogs=[Dog("Tom",6), Dog("Jerry",9), Dog("Butt",3)]
# my_pet=Pet(my_dogs)
# my_pet.walk()

# B�i 05. Vi?t m?t class NewString trong ?� c� 2 ph??ng th?c: get_string() v� print_string()
#     - get_string - nh?n m?t string do ng??i d�ng nh?p v�o
#     - print_string - in string nh?p v�o ? d?ng to�n ch? in hoa

# class NewString:
#     def __init__(self):
#         self.str = ''
#     def get_string(self):
#         self.str = input()
#     def print_string(self):
#         print(self.str.upper())
# str = NewString()
# str.get_string()
# str.print_string()

# B�i 06. X�y d?ng class User ?? l?u tr? th�ng tin ng??i d�ng h? th?ng
#     - Thu?c t�nh: first_name, last_name, birthday, email, address, username, password
#     - H�nh vi (ph??ng th?c): login(), logout(), update_info()
class User:
    def __init__(self,first_name,las_name,birthday,email, address, username, password):
        self.first_name = first_name
        self.las_name = las_name
        self.birthday = birthday
        self.email = email
        self.address = address
        self.username = username
        self.password = password

    def login(self):

