# -- coding: utf8 --
# Đề tài 1. Một team dự án marketing tại công ty PhongVu cần phát triển một công cụ để hỗ trợ cho việc gửi email:
#     - Gửi đơn: Gửi mail cho 1 người
#     - Gửi đa: Gửi mail cho nhiều người
# Bạn hãy tìm hiểu về cách gửi email trên Python và tiến hành xây dựng công cụ đáp ứng yêu cầu trên.
# Chú ý:
#     + Xây dựng công cụ dạng GUI là một điểm cộng
#     + Trong dạng gửi đa, danh sách email người nhận sẽ được nhập vào qua file excel
#     + Trong dạng gửi đa, hãy nghĩ đến việc mỗi người nhận, sẽ nhận được nội dung email khác nhau,
#     mang tính cá nhân của chính người nhận.

# Gửi đơn
import smtplib, ssl
port = 465
sender_email = "shauqia53@gmail.com"
receiver_email= "shauqia53+person1@gmail.com"
message ="""Subject: Greetings

Hi Linh, hope you are well"""
password = input("Type your pasword and press enter: ")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.encode("utf-8"))

# Gửi đa
import openpyxl
from pathlib import Path
import pandas as pd
import smtplib, ssl
port = 465
sender_email = "shauqia53@gmail.com"
message ="""Subject: Greetings

Hi {name}, hope you are well"""

password = input("Type your pasword and press enter: ")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login(sender_email, password)

    data = pd.ExcelFile("contact_list.xlsx")
    df = data.parse("Sheet1")
    ps = openpyxl.load_workbook('contact_list.xlsx')
    sheet = ps['Sheet1']

    for row in range(2, sheet.max_row + 1):
        name= sheet['A' + str(row)].value
        email = sheet['B'+ str(row)].value
        server.sendmail(sender_email, email, message.format(name=name).encode("utf-8"))
