from bs4 import BeautifulSoup  # для парсинга старниц
import requests                # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import time
import random
import pandas as pd

symbols_en = "abcdefghijklmnopqrstuvwxyz1234567890"
user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
url = 'http://176.124.215.22:60023/'
headers = {
    'user-agent':user_agent_val
}
datas = {
    'login':'login',
    'password':'password'
}

login='login'

password='password'



url2=f'http://176.124.215.22:60023/?login={login}&password={password}'
lg=requests.get(url2)
f=open('res.txt', '+w')
f.write(lg.text)
f.close


# posts = []#лист куда записываются данные после парсинга
# print(url)
# response = get(url)#ответ сайта забирает
# html_soup = BeautifulSoup(response.text, 'html.parser')#парсит страницу

# posts_data = html_soup.find_all('div', class_="preview_new")
# if posts_data != []:#Проверка что данные есть
#     posts.extend(posts_data)#запись в лист
#     value = random.random() #рандом для задержки
#     scaled_value = 1 + (value * (9 - 5))
#     print(scaled_value)#принтит секунды задержки
#     time.sleep(scaled_value)#таймер на всякий случай чтобы не страдать самому и сайту
# else:
#     print('empty')#если страницы нет то программа завершится

# post_request = session.post(url, {
#      'backUrl': 'https://moscow.hh.ru/',
#      'username': 'yourlogin',
#      'password': 'yourpassword',
#      '_xsrf':_xsrf,
#      'remember':'yes',
# })
    