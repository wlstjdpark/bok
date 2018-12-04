import datetime
import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.bok.or.kr/portal/singl/baseRate/list.do?dataSeCd=01&menuNo=200643')
bsObj = BeautifulSoup(r.content, 'html.parser')
for tr in bsObj.select('#content > div.table.tac > table > tbody > tr'):
    year, date, base_rate = [t.text for t in tr.select('td')]
    yyyymmdd = datetime.datetime.strptime(year + date, '%Y%m월 %d일').strftime('%Y-%m-%d')
    print(yyyymmdd, base_rate)
    break
