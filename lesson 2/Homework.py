# Bai tap 1: giai phuong trinh ax^2 + bx + c = 0
"""a, b, c = float(input("Nhập a = ")), float(input("Nhập b =")), float(input("Nhập c ="))
if a == 0 and b == 0 and c == 0:
    print("Phuong trinh vo so nghiem")
if a == 0 and b != 0 and c != 0:
    x=-c/b
    print("Nghiem cua phuong trinh la x = {}". format(round(x, 2)))
elif a != 0:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x= -b/(2*a)
        print("Phuong trinh co mot nghiem kep x ={}". format(round(x, 2)))
    else:
        x1= (-b+sqrt(delta)/(2*a))
        x2= (-b-sqrt(delta)/(2*a))
        print("Phuong trinh co hai nghiem x1 = {} va x2 = {}". format(round(x1, 2), round(x2, 2)))
"""
# Bai tap 2:
# S_1= 1 + x+x^2+x^3+...+x^n
"""n = int(input("Nhap so nguyen duong n ="))
while not n>0:
    n=int(input("Nhap lai so nguyen duong n="))
x = float(input("Nhap so thuc x="))
Sum_S1 = 1
for i in range(n+1):
    Sum_S1 += x**i
print ("S_1= 1 + x+x^2+x^3+...+x^n={}".format(Sum_S1))
"""

# S_2= 1-x+x^2-x^3+...+(-1)^n.x^n
"n = int(input("Nhap so nguyen duong n ="))
while not n>0:
    n=int(input("Nhap lai so nguyen duong n="))
x = float(input("Nhap so thuc x="))
Sum_S2 = 1
for i in range(n+1):
    Sum_S2 += (-x)**i
print ("S_2= 1-x+x^2-x^3+...+(-1)^n.x^n={}".format(Sum_S2))
"""

# Bai tap 3
n = int(input("Nhap so nguyen duong n ="))
while not 0<n<1000:
    n=int(input("Nhap lai so nguyen duong n="))
tong = 0
so_tach_ra = n % 10
tong += so_tach_ra
so_nguyen = n // 10
while so_nguyen ==0:
 print("Tong cac chu so cua n= {}".format(tong))