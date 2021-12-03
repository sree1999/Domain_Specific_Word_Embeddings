import requests
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import random

def see(url):
  response = requests.get(url=url,)
  soup = BeautifulSoup(response.content,"html.parser")
  see_also = soup.find(id="See_also")
  if see_also ==None:
    return(0)
  ul = see_also.find_next("ul")
  link = ul.find("li").find("a")
  if link['href'].find("/wiki/Portal:")==True:
    ul = ul.find_next("ul")
  all_li = ul.find_all("li")
  random.shuffle(all_li)
  return(all_li)

def disp(url,c):
  if c==100:
    print("DONE")
    return(0)
  response = requests.get(url=url,)
  soup = BeautifulSoup(response.content,"html.parser")
  title = soup.find(id="firstHeading")
  print(c,title.string)

def scrapeWiki(url,c=0):
  all_li = see(url)
  #print(len(all_li))
  for li in all_li:
    link = li.find("a")
    #print(link)
    scrape = "https://en.wikipedia.org" + str(link['href'])
    try:
      if see(scrape)==0 or link['href'].find("/Portal:")==True or link['href'].find(".svg")==True:
        print("OK")
        continue
    except:
      continue
    disp(scrape,c)
    c+=1
    if c==100:
      break
    scrapeWiki(scrape,c)

scrapeWiki("https://en.wikipedia.org/wiki/Banking")
