from bs4 import BeautifulSoup  # для парсинга старниц
import requests                # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import time
import random

def parsing(count,posts):
    while count <= 1:#Цикл для парсинга новостей
        url = 'https://zabgu.ru/php/news.php?category=1&page=' + str(count)#чтобы парсить заданное кол-во страниц
        print(url)
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')

        posts_data = html_soup.find_all('div', class_="preview_new")
        if posts_data != []:#Проверка что данные есть
            posts.extend(posts_data)#запись в лист
            value = random.random() 
            scaled_value = 1 + (value * (9 - 5))
            print(scaled_value)
            time.sleep(scaled_value)#таймер на всякий случай
        else:
            print('empty')#если страницы нет то программа завершится
            break
        posts_data2 = html_soup.find_all('div', class_="preview_new_end")#на сайте треться новость имеет другой класс
        if posts_data2 != []:
            posts.extend(posts_data2)
            value = random.random()
            scaled_value = 1 + (value * (9 - 5))
            print(scaled_value)
            time.sleep(scaled_value)
        else:
            print('empty')
            break#если страницы нет то программа завершится
        count += 1

def output(posts,count,n):
    while count <= n:  # count <= n
        info = posts[int(count)]#берём из листа 1 новость
        day = info.find('p',{"class":"day"}).text
        title = info.find('div',{"class":"headline"}).text
        year = info.find('p',{"class":"yearInTileNewsOnPageWithAllNews"}).text
        tegs = info.find('div',{"class":'markersContainer'}).text
        print(title, ' ', day,' ',year, tegs )
        count += 1