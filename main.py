from pprint import pprint

import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

count=0
while count<6:
    pprint(data['Date'])
    pprint(data['Valute']['USD']['Value'])
    data = requests.get('https:'+data['PreviousURL']).json()
    count+=1



