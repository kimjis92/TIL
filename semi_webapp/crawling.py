from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import numpy as np
import time

def crawling_result(keyword):
    driver = webdriver.Chrome(executable_path='(driver) chromedriver.exe')
    url= 'https://map.kakao.com/'
    driver.get(url)

    loc_name = keyword[0]
    food_name = keyword[1]

    driver.find_element_by_name('q').send_keys(loc_name+food_name)
    driver.find_element_by_xpath("//button[@id='search.keyword.submit']").send_keys(Keys.ENTER)
    time.sleep(1)

    # 1) 가게 이름
    store_name = driver.find_elements_by_class_name('link_name')
    store_list = []
    for i in store_name:
        store_list.append(i.text)
    # 2) 평점
    score = driver.find_elements_by_class_name('num')
    score_list = []
    for i in score:
        score_list.append(i.text)
    # 3) 리뷰
    review = driver.find_elements_by_class_name('review')
    review_list=[]
    for i in review:
        review_list.append(i.text)

    driver.close()
    driver.quit()

    score_list=[e for e in score_list if e !='' ]
    df_accuracy = pd.DataFrame({'Store':store_list, 'Score':score_list, 'Review':review_list})

    result_list=[]
    for i in range(15):
        result_list.append([store_list[i], score_list[i], review_list[i]])

    return result_list
