from bs4 import BeautifulSoup  # для парсинга старниц
import requests                # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import time
import random
import pandas #для панд

def parsing():
    posts = []#лист куда записываются данные после парсинга
    count = 1 #счётчик
    while count <= 1:#Цикл для парсинга новостей
            url = 'https://zabgu.ru/php/news.php?category=1&page=' + str(count)#чтобы парсить заданное кол-во страниц
            print(url)
            response = get(url)#ответ сайта забирает
            html_soup = BeautifulSoup(response.text, 'html.parser')#парсит страницу

            posts_data = html_soup.find_all('div', class_="preview_new")
            if posts_data != []:#Проверка что данные есть
                posts.extend(posts_data)#запись в лист
                value = random.random() #рандом для задержки
                scaled_value = 1 + (value * (9 - 5))
                print(scaled_value)#принтит секунды задержки
                time.sleep(scaled_value)#таймер на всякий случай чтобы не страдать самому и сайту
            else:
                print('empty')#если страницы нет то программа завершится
                break
            posts_data2 = html_soup.find_all('div', class_="preview_new_end")#на сайте третья новость имеет другой класс
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
    return posts

def output(posts,newsDM,file_name): #Вывод данных в exel
    """Вывод данных в exel через pandas DataFrame 
    
    Args:
        posts (list): list с новостями
        newsDM (dataframe): таблица с данными
        file_name (text): назвать файл с данными
    """

    count = 0 #счётчик
    n = int(len(posts)) - 1 #узнаём сколько новостей всего записали
    while count <= n:  # count <= n
            info = posts[int(count)]#берём из листа 1 новость
            day = info.find('p',{"class":"day"}).text #записываем в переменные
            title = info.find('div',{"class":"headline"}).text
            year = info.find('p',{"class":"yearInTileNewsOnPageWithAllNews"}).text
            tagsRaw = posts[count].find('div', {'class': 'markersContainer'}).find_all('a', {'class': 'marker_news'})
            tags = [tagsRaw[k].text for k in range(0, len(tagsRaw))]
            date = day + ' ' + year #совмещаем день месяц и год
            # print(title, ' ', day,' ', tags ) использовалось для проверки
            newsDM = newsDM.append({'header':title, 'Date': date ,'tegs': tags}, True)
            count += 1
  

    newsDM.to_csv(file_name,sep='\t', encoding='UTF=16')