import bs4, requests
from subprocess import check_output
f=requests.get('http://automatetheboringstuff.com/chapter11/')
test01=bs4.BeautifulSoup(f.text, 'html5lib')
print(test01.find_all('a'))
path = 'C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'

# for i in range(len(test01.find_all('a'))):
#     check_output(' '.join((path, test01.select('a')[i].get('href'))), shell=True)