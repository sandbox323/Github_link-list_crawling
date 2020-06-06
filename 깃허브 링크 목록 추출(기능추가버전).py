import requests
from bs4 import BeautifulSoup

filter_str = '.'
head = 'https://github.com/'
url = input("추출할 깃허브의 url을 입력하세요 : ").strip()

if input("특정 제목의 링크만 가져오시겠습니까? (Y/N) : ") in ['Y', 'y', 'yes']:
    filter_str = input("어떤 값을 포함하는 링크를 가져올지, 그 값을 입력하세요 : ")
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
table = soup.select('.files tbody')[-1]
for link in table.select('tr td.content a'):
    if filter_str in link.text:
        print('[' + str(link.text) + '](' + head + link['href'] + ')')
