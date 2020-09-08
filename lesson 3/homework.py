# bai tap 1 Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
s = input("Nhap mot chuoi:")
if len(s) > 0:
    print(s.replace(s[0], "$"))


# bai tap 2 Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
s = input("Nhap mot chuoi:")
if len(s) == 0:
    s = input("Moi nhap lai chuoi: ")
m = int(input("xoa ky tu thu"))
if 0 <= m < len(s):
    s_new = s[:m] + s[m+1:]
    print ("chuoi moi la:",s_new)
else:
    print ("khong tim duoc vi tri xoa")

# bai tap 3 Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
s = input("Nhap mot chuoi:")
print(s[0::2])

#bai tap 4 Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào,nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
s = input ("Nhap mot chuoi:")
s_new = s[:2] + s[len(s)-2:len(s)]
if len(s_new) >= 2:
    print("chuoi moi la:", s_new)
else:
    print("Chuoi rong")

#bai tap 5 Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
s = input("Nhap mot chuoi:")
print("Ky tu lon nhat la:", max(s))
print("ky tu nho nhat la:", min(s))

#bai tap 6 Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
s = input("Nhap mot chuoi:")
s_new = ""
for i in range(len(s)):
    if "a" <= s[i] <= "z":
        s_new += s[i].upper()
    elif "A" <= s[i] <= "Z":
        s_new += s[i].lower()
    else:
        s_new += s[i]
print("Chuoi moi la:", s_new)

