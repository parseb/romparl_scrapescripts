from bs4 import BeautifulSoup as soup
import urllib.request
from urllib.error import HTTPError
import re
import time

def getcdepdata(so):
    req = urllib.request.Request(url=so, 
                                 headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    try:
        handler = urllib.request.urlopen(req)
    except HTTPError as e:
        content = e.read()
    page_html= handler
    
    page_soup= soup(page_html, "html.parser")
    title_date= page_soup.find("span", {"class": "headline"}).text.strip()
    texts= page_soup.findAll("td", {"class": "textn"})

    if len(re.findall('\d+', str(title_date))) > 0:
        year= int(re.findall('\d+', str(title_date))[1])
        day= int(re.findall('\d+', str(title_date))[0])
        print("===== At YEAR: " + str(year) + " =====")
        f= "compol_cdep.csv"
        #return f, year
        file= open(f, 'a')

        if texts:
            for text in texts:
                if text.text.strip():
                    try:
                        speaker= str(text.p.a.string.strip())
                        print("Speaker: "+ speaker)
                    except:
                        speaker= "-"
                    try:
                        x=text.find('a')['href']
                        speech= str(text.p.text.strip())
                        print("Speech: " + speech)      #.replace(speaker, '')
                    except:
                        speech= "NA"
                        print("No Speech")

                    print(speech)
                    if (speech != "NA" and (len(speech) > 200)):
                        file.write(str(title_date) + 
                                   "~|~" + speaker + "~|~" + 
                                   speech.replace(",", " ") + "~|~" 
                                   + str(year) + "~|~" + str(day) + "~|~" + ('www.cdep.ro'+str(x)) + "\n" )
        file.close() #problem? nothing to close case

count = 0
while count < 8126 :
    src= 'http://www.cdep.ro/pls/steno/steno.stenograma?ids='+ str(count)
    getcdepdata(src)
    time.sleep(2)
    print("+++" + str(count) + " out of 8126 +++")
    count = count + 1
