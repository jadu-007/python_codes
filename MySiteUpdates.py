from urllib.request import urlopen
import time
import datetime



import telegram
TOKEN = ''  ##Enter your telegram token here 
bot = telegram.Bot(TOKEN)
#            bot.send_message("@customjobupdates", msg)



channel="https://programmersguide.000webhostapp.com/"
page = urlopen(channel) #For python 3 use urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
#oldData=soup.find_all('a')

oldData="oldData"

from twilio.rest import Client
while(True):
    flag=False
    msg=""
    page = urlopen(channel)
    soup = BeautifulSoup(page)
    if(str(oldData)!=str(soup.find_all('a'))):
        oldData=soup.find_all('a')
        
        print("Site is Updated")
        print("Old data is ",oldData)
        for link in soup.find_all('a'):
            #print(link.get('title'))
            if(link.get('a') in ["YouTube Home","Upload",None,"Home","Trending","History","Get YouTube Premium","Music","Sports","Gaming","Movies","News","Live","Fashion","Spotlight","360° Video","Browse channels","Facebook","Twitter","Telegram","InstaGram","Website","Prep Insta","YouTube home","360Â° Video","Job Updates Web","Courses for Exams","Well Academy","Instagram","Talk with Abdul"]):
                pass
            else:
                flag=True
                #print(link.get('title'))
                #msg=msg+" "+link.get('title')
                msg=msg+" "+link.get('title')
        if flag:
            client = Client('ACbcba02ee36e281212a13285446bce1dc','cb2a8c21b2fdbc036f3602073ef5ea0d')
            TOKEN = ' ' ##Enter Twilio token here 
            msg=""+msg[0:159]
            print("sms msg is ",msg," Size is ",len(msg))
            client.messages.create(to='+919029321998',
                       from_= '+12067453863',
                       body=msg)
            bot.send_message("@customjobupdates", msg)
    else:
        print("No change I'm sleeping for 800 secs")
        time.sleep(30)
        
