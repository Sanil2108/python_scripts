import urllib, requests, bs4
init_path='https://automatetheboringstuff.com'
for i in range(1, 19, 1):
    temp_path=''.join((init_path, '/chapter', str(i)))
    urllib.request.urlretrieve(temp_path, ''.join(('C:\\Users\\Admin\\Desktop\\python\\automateTheBoringStuff\\', str(i), '.html')))
    print(temp_path)