# coding=utf-8
# Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
# def read_nline(fname,n):
#     f=open("bill.txt",'r',encoding='utf-8')
#     for i in range (n):
#         line=f.readline()
#         print(line)
# read_nline("bill.txt",3)

# Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file
# my_list=["summer","autumn","winter"]
# my_list=map(lambda x: x+'\n', my_list)
# f=open("bill.txt", 'a',encoding='utf-8')
# f.writelines(my_list)

# Bài 03: Viết chương trình trộn 2 file thành file mới
# merged_file=file2=""
# with open("months.txt",'r',encoding='utf-8') as f1:
#     merged_file=f1.read()
# with open("seasons.txt",'r',encoding='utf-8') as f2:
#     file2=f2.read()
# merged_file +='\n'
# merged_file +=file2
# with open('new_file.txt','w',encoding='utf=8') as f3:
#     f3.write(merged_file)

# Bài 04: Viết hàm
#         def get_file_size(file)
#     để lấy và trả về dung lượng của file

def get_file_size(file):
    file.seek(0,os.SEEK_END)
    Print('Dung luong cua file la',file.tell(),'bytes')
get_file_size("new_file.txt")