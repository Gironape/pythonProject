import csv
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import urllib.request

URL_DL='https://www.cbr-xml-daily.ru'
headers={'User-Agent':"Mozilla/5.0"}
html_page = requests.get(URL_DL, headers)
soup = BeautifulSoup(html_page.text, "html.parser")
search = soup.find_all(id="example")
search=urllib
print(search)
data=requests.get(search).json()
count=0
with open("dataset.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(["Дата","\t""Курс Доллара"])
    while count<6:
        pprint(data['Date'])
        pprint(data['Valute']['USD']['Value'])
        file_writer.writerow([data['Date'] , data['Valute']['USD']['Value']])
        data = requests.get('https:'+data['PreviousURL']).json()
        count+=1



