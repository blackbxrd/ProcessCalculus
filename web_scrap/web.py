from bs4 import BeautifulSoup  # для парсинга старниц
import requests                # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import time
import random
import func

url = 'https://zabgu.ru/php/news.php?category=1&page='
posts = []
count = 1
# while count <= 1:
#     url = 'https://zabgu.ru/php/news.php?category=1&page=' + str(count)
#     print(url)
#     response = get(url)
#     html_soup = BeautifulSoup(response.text, 'html.parser')

#     posts_data = html_soup.find_all('div', class_="preview_new")
#     if posts_data != []:
#         posts.extend(posts_data)
#         value = random.random()
#         scaled_value = 1 + (value * (9 - 5))
#         print(scaled_value)
#         time.sleep(scaled_value)
#     else:
#         print('empty')
#         break
#     posts_data2 = html_soup.find_all('div', class_="preview_new_end")
#     if posts_data2 != []:
#         posts.extend(posts_data2)
#         value = random.random()
#         scaled_value = 1 + (value * (9 - 5))
#         print(scaled_value)
#         time.sleep(scaled_value)
#     else:
#         print('empty')
#         break
func.parsing(count,posts)
    

n = int(len(posts)) - 1 #узнаём сколько новостей всего записали
count = 0
# while count <= n:  # count <= n
#     info = posts[int(count)]
#     day = info.find('p',{"class":"day"}).text
#     title = info.find('div',{"class":"headline"}).text
#     year = info.find('p',{"class":"yearInTileNewsOnPageWithAllNews"}).text
#     tegs = info.find('div',{"class":'markersContainer'}).text
#     print(title, ' ', day,' ',year, tegs )
#     count += 1
func.output(posts,count,n)