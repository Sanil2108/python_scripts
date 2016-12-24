import bs4, requests, time

def get_links(initial_path):
    if(len(all_links)>max_crawls):
        return
    else:
        soup_init=bs4.BeautifulSoup(requests.get(initial_path).text, 'html5lib')
        list_of_all_links=soup_init.find_all('a')

        # print(list_of_all_links)
        # print(list_of_all_links[0].get('href'))

        for j in range(len(list_of_all_links)):
            all_links.append(list_of_all_links[j])
            try:
                get_links(list_of_all_links[j].get('href'))

            except Exception as e:
                #exception occured.
                #havent looked at exceptions yet. basically it gets a <a> which isnt a link.
                #weird. will look into later
                log.append(''.join(('\n', ' - '.join((time.asctime( time.localtime(time.time()) ), e.args[0])))))
                return


max_crawls=10000

log = []
initial_path='http://www.sheldonbrown.com/web_sample1.html'

all_links=[]

get_links(initial_path)

logFile=open('randomLogFile.txt', 'w')

for i in range(len(log)):
    logFile.write(log[i])

print(all_links)
print(log)