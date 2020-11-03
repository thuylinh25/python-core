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
import numpy as np
from time import sleep
from random import randint

Item_list = np.array(['lò sưởi','máy giặt'])
for item in Item_list:
    webdriver_path = 'C://Users//Linh Le//Downloads//chromedriver.exe'
    browser = webdriver.Chrome(webdriver_path)
    browser.get('https://www.lazada.vn')

    search_bar = browser.find_element_by_id('q')
    search_bar.send_keys(item)
    search_bar.send_keys(Keys.ENTER)
    sleep(randint(2, 10))

    item_titles = browser.find_elements_by_class_name('c16H9d')
    item_prices = browser.find_elements_by_class_name('c13VH6')

    titles_list = []
    prices_list = []
    for title in item_titles:
        titles_list.append(title.text)
    for price in item_prices:
        prices_list.append(price.text)

    df = pd.DataFrame(zip(titles_list, prices_list,"Trang"), columns=["Tên sản phẩm","Giá","Lazada"])
    df["Giá"] = df["Giá"].str.replace("₫","")
    df["Giá"] = df["Giá"].str.replace(",","").astype(int)
    df = df[df["Tên sản phẩm"].str.contains("x2") == False]
    # df["Trang"] = "Lazada"
    print(df)
    df.to_csv("Khảo_sát_giá_lazada .csv")


# webdriver_path = 'C://Users//Linh Le//Downloads//chromedriver.exe'
# Tiki_url = 'https://tiki.vn/'
# search_item = 'máy giặt'
#
# browser = webdriver.Chrome(webdriver_path)
# browser.get(Tiki_url)
#
#
# search_bar = browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/div[3]/div/div[1]/div[2]/div/input')
# search_bar.send_keys(search_item)
# search_bar.send_keys(Keys.ENTER)
#
# item_titles = browser.find_elements_by_class_name('title')
# item_prices = browser.find_elements_by_class_name('product-price_current-price')
#
# titles_list = []
# prices_list = []
# for title in item_titles:
#     titles_list.append(title.text)
# for price in item_prices:
#     prices_list.append(price.text)
#
# df = pd.DataFrame(zip(titles_list, prices_list), columns=["Tên sản phẩm","Giá"])
# df["Giá"] = df["Giá"].str.replace("₫","")
# df["Giá"] = df["Giá"].str.replace(",","").astype(int)
# df = df[df["Tên sản phẩm"].str.contains("x2") == False]
# df["Trang"] = "Tiki"
# print(df)
# df.to_csv("Giá lò sưởi_Tiki .csv")

#
# sns.set()
# _ = sns.boxplot(x="Trang", y="Giá", data=df)
# _ = plt.title("So sánh giá lò sưởi giữa các trang thương mại điện tử")
# _ = plt.ylabel("Giá(vnd)")
# _ = plt.xlabel("các trang thương mại điện tử")
# plt.show()
