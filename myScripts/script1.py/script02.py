import requests, sys
some_random_file=open('some_random_file.txt', 'wb')
if len(sys.argv)<1:
    str=requests.get('google.com')
else:
    str=requests.get(sys.argv[0])
for chunk in str.iter_content(100000):
    some_random_file.write(chunk)
some_random_file.close()