

#   Постановка задачи:
#   Страница: http://socr.ucla.edu/docs/resources/SOCR_Data/SOCR_Data_Dinov_020108_HeightsWeights.html
#   Страница содержит информацию о росте и весе 25000 людей. Требуется посчитать средний ИМТ(индекс массы тела)
#   Для людей, чей рост от 170 до 180 см

import Functional
import requests
from bs4 import BeautifulSoup

URL = "http://socr.ucla.edu/docs/resources/SOCR_Data/SOCR_Data_Dinov_020108_HeightsWeights.html"


extendedList = Functional.ExtendCollectionClass(list)

response = requests.get(URL)

soup = BeautifulSoup(response.text, features="lxml")

#Достает данные из таблицы
def parse_table(rows):
    rows = soup.find_all('tr')

    def get_values_from_tag(columns):
        columns = columns.find_all('td')
        try:
            return Functional.Map(columns, lambda x: float(x.text)).collect()
        except:
            return None


    return Functional.Map(rows,get_values_from_tag).filter(lambda x : x != None)

def get_IMT(h, m):
    return m / (h/100)**2


#Данные из таблицы
mapped_obj = parse_table(soup)

#Перевод из имперской системы мер в европейскую, отброс первого столбца
mapped_obj = mapped_obj.map(lambda x: [x[1] * 2.54, x[2] / 2.205]).filter(lambda x : x[0] >= 170 and x[0] <= 180)

counter = 0

def sum_values(accumulator, lst):
    global counter
    counter += 1
    return accumulator + get_IMT(*lst)

sum_IMT = mapped_obj.reduce(0, sum_values)

average = sum_IMT / counter

with open('result.txt','w') as file:
    file.write(average.__str__())

