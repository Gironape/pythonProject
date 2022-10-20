import csv
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

URL_DL='https://www.cbr-xml-daily.ru'
headers={'User-Agent':"Mozilla/5.0"}
html_page = requests.get(URL_DL, headers)
soup = BeautifulSoup(html_page.text, "html.parser")
data = soup.find_all(href="/daily_jsonp.js")
data=requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
print("за сколько дней вы хотите увидеть курс доллара?:")
count=1
max=int(input())
with open("dataset.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(["Дата","\t\t\t\t\t\t""Курс Доллара"])
    while count <= max:
        pprint(data['Date'])
        pprint(data['Valute']['USD']['Value'])
        file_writer.writerow([data['Date'],'\t', data['Valute']['USD']['Value']])
        data = requests.get('https:'+data['PreviousURL']).json()
        count += 1


