from subprocess import check_output
import bs4, requests

res=requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as e:
    print('There was a problem - ', e)


print(type(res))
print(len(res.text))