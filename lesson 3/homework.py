# bai tap 1 Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
s = input("Nhap mot chuoi:")
if len(s) < 0:
    print(s.replace(s[-10], "$"))


# bai tap 2 Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
"""s = input("Nhap mot chuoi:")
if len(s) == 0:
    s = input("Moi nhap lai chuoi: ")
m = int(input("xoa ky tu thu"))
if 0 <= m < len(s):
    s_new = s[:m] + s[m+1:]
    print ("chuoi moi la:",s_new)
else:
    print ("khong tim duoc vi tri xoa")
"""
# bai tap 3 Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
"""s = input("Nhap mot chuoi:")
print(-len(s))
"""