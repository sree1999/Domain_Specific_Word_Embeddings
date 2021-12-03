import bs4 as bs
import requests
import string
urls=[]
def get_terms(alphabet):
    global urls
    page = requests.get("https://www.investopedia.com/terms/{}".format(alphabet))
    content = bs.BeautifulSoup(page.content,'lxml')
    links=[]
    for url in content.find_all('a',{'class':'dictionary-top300-list__list mntl-text-link'}):
    	link=url.get('href')
    	links.append(link)
    urls=links.copy()
        
        

def web_scraper(url,alphabet):
    r=requests.get(url)  
    soup=bs.BeautifulSoup(r.content,"lxml") 
    title=[item.text for item in soup.find_all("title")]
    para=[item.text for item in soup.find_all("p")] 
    listToStr = ' '.join([str(elem) for elem in para[:-6]]) #last 6 items are heading of links to other articles
    scraped_content=[url,title,para]
    try:
        f = open("Investopedia_Terms/{}/{}".format(alphabet,title[0]), "w")
    except:
        alt_title="exceptions"
        f = open("Investopedia_Terms/{}/{}".format(alphabet,alt_title), "a")
        pass
    f.write(listToStr)
    f.close()
    

for alphabet in list(string.ascii_lowercase):
    count=1
    links=get_terms(alphabet)
    for url in urls:
        X=web_scraper(url,alphabet)
        print('{} out of {} {}-terms done'.format(count,len(urls),alphabet))
        count+=1
