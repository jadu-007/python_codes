import requests
from bs4 import BeautifulSoup

url = "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('item')




import requests
news_items=[]
i=1
for item in items:
##    print(item)
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_item['image'] = item.image.text
    news_items.append(news_item)
    fileName="images/"+str(i)+".jpg"
    with open(fileName, 'wb') as handle:
        response = requests.get(item.image.text, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    i+=1
##print(news_items)
