from bs4 import BeautifulSoup  # для парсинга старниц
import requests                # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import time
import random
import func
import pandas as pd

url = 'https://zabgu.ru/php/news.php?category=1&page='

newsDM = pd.DataFrame()
posts=func.parsing()
func.output(posts,newsDM,file_name='date.csv')


# func.parsing(count,posts)
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

    

#                                func.output(posts,count,n) вывод в консоль
# while count <= n:  # count <= n
#     info = posts[int(count)]
#     day = info.find('p',{"class":"day"}).text
#     title = info.find('div',{"class":"headline"}).text
#     year = info.find('p',{"class":"yearInTileNewsOnPageWithAllNews"}).text
#     tegs = info.find('div',{"class":'markersContainer'}).text
#     print(title, ' ', day,' ',year, tegs )
#     count += 1

#                                func.output(posts,count,n,newsDM) вывод в ексель
# while count <= n:  # count <= n
#         info = posts[int(count)]#берём из листа 1 новость
#         day = info.find('p',{"class":"day"}).text
#         title = info.find('div',{"class":"headline"}).text
#         year = info.find('p',{"class":"yearInTileNewsOnPageWithAllNews"}).text
#         tagsRaw = posts[count].find('div', {'class': 'markersContainer'}).find_all('a', {'class': 'marker_news'})
#         tags = [tagsRaw[k].text for k in range(0, len(tagsRaw))]
#         date = day + ' ' + year
#         print(title, ' ', day,' ', tags )
#         newsDM = newsDM.append({'header':title, 'Date': date ,'tegs': tags}, True)
#         count += 1

# file_name = '.\data.csv'

# newsDM.to_csv(file_name,sep='\t', encoding='UTF=16')
