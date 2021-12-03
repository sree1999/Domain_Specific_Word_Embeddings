import bs4 as bs
import requests
import string

def get_terms(u,clas):
    
    page = requests.get(u)
    content = bs.BeautifulSoup(page.content,'lxml')
    links=[]
    for url in content.find_all('a',{'class':clas}):
    	link=url.get('href')
    	links.append(link)
    return links
        
        

def web_scraper(url):
    r=requests.get(url)  
    soup=bs.BeautifulSoup(r.content,"lxml") 
    title=[item.text for item in soup.find_all("title")]
    para=[item.text for item in soup.find_all("p")] 
    listToStr = ' '.join([str(elem) for elem in para[:-6]]) #last 6 items are heading of links to other articles
    scraped_content=[url,title,para]
    try:
        f = open("Investopedia_Articles/Investing/{}".format(title[0]), "w")
    except:
        alt_title="exceptions"
        f = open("Investopedia_Articles/Investing/{}".format(alt_title), "a")
        pass
    f.write(listToStr)
    f.close()

urls = get_terms("https://www.investopedia.com/investing-4427685",'breadcrumbs-nav__link')
temp=[]
count = 1
for url in urls:
    print("Getting links from section {} of {}".format(count,len(urls)))
    p=get_terms(url,'breadcrumbs-nav__link')
    count+=1
    try:
        if p!=[]:
            temp.append(p)
    except:
        temp.append([url])
        pass

temp_b=[]
for a in temp:
    for b in a:
        if b not in temp_b:
            temp_b.append(b)
#print(temp_b)
temp_c=[]
count = 1
for url in temp_b:
    print("Getting links from page {} of {}".format(count,len(temp_b)))
    count+=1
    q=get_terms(url,"comp card mntl-card card")
    temp_c.append(q)
all_links=[]
for a in temp_c:
    for b in a:
        all_links.append(b)
count=1
for url in all_links:
    print("Scrapping {} out of {} articles".format(count,len(all_links)))
    count+=1
    web_scraper(url)





