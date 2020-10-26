# -- coding: utf8 --
# Đề tài 2. Là một người dùng có nhu cầu mua lò sưởi trong những ngày Đông tới.
# Nhưng có quá nhiều trang thương mại điện tử mà mỗi đơn vị lại có một giá bán khác nhau.
# Hãy xây dựng công cụ thể thực hiện trích xuất dữ liệu từ tối thiểu 2 trang thương mại điện tử lớn để so sánh giá của các sản phẩm lò sưởi
# Chú ý:
#     + Nên xây dựng để mở rộng cho các sản phẩm khác nữa
#     + Thiết kế Cơ sở dữ liệu để lưu lại các dữ liệu đã trích xuất được
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

webdriver_path = 'C://Users//Linh Le//Downloads//chromedriver.exe'
Lazadar_url = 'https://www.lazada.vn'
search_item = 'lò sưởi điện'

browser = webdriver.Chrome(webdriver_path)
browser.get(Lazadar_url)

search_bar = browser.find_element_by_id('q')
search_bar.send_keys(search_item)
search_bar.send_keys(Keys.ENTER)

item_titles = browser.find_elements_by_class_name('c16H9d')
item_prices = browser.find_elements_by_class_name('c13VH6')

titles_list = []
prices_list = []
for title in item_titles:
    titles_list.append(title.text)
for price in item_prices:
    prices_list.append(price.text)

df = pd.DataFrame(zip(titles_list, prices_list), columns=["Tên sản phẩm", "Giá"])
print (df)
df.to_csv("Giá lò sưởi điện _lazada .csv")