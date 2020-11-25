from random import randint
import telegram
import time
from urllib.request import Request,urlopen
from datetime import datetime 
from bs4 import BeautifulSoup

option=input("Enter Option\n1) Stocks In News\n2) Day Highlights\n3) Stocks To Watch Today\n")


    
datetimenow=datetime.now()



url=input("Enter URL")


req = Request(url, headers={'User-Agent': 'Mozilla/7.0', 'Connection': 'close'})
page = urlopen(req).read()
soup = BeautifulSoup(page)


slideshow = soup.find(class_='slideshow-article')
items=slideshow.findAll("p")

if option == 1:
    print("**:bar_chart: STOCKS IN NEWS :bar_chart:**")
elif option == 2:
    print("**:bar_chart: DAY HIGHLIGHTS :bar_chart:**")
else:
    print("**:bar_chart: Stocks To Watch Today :bar_chart:**")
print("Date: "+str(datetimenow.day)+"/"+str(datetimenow.month)+"/"+str(datetimenow.year)+"\n")

for item in items:
    print("\n"+item.text.replace("| ","\n").replace("amp;",""))
