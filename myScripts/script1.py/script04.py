import bs4, requests
f=requests.get('https://www.google.co.in/search?q=weather')
bsoup=bs4.BeautifulSoup(f.text, 'html5lib')
print(bsoup.find('span', {'class', 'wob_t'}, {'id', 'wob_tm'}).contents[0])