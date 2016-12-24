import bs4, requests, urllib
init_path = 'http://xkcd.com/'
final_val=100
i=1
for i in range(1, final_val, 1):
    temp_path=''.join((init_path, str(i)))
    all_source=requests.get(temp_path).text
    soup=bs4.BeautifulSoup(all_source)
    print(soup.find_all('img')[1])
    urllib.request.urlretrieve(''.join(('http:', soup.find_all('img')[1].get('src'))), ''.join(('C:\\Users\\Admin\\Desktop\\python\\XKCDCOMICS\\', str(i), '.jpg')))