from PIL import Image, ImageDraw, ImageFont
import csv
from random import randint
##import tkinter.font as font
import telegram
import time
from urllib.request import Request,urlopen
TOKEN = ' ' ##Enter your telegram token here 
bot = telegram.Bot(TOKEN)
import shutil 
def get_concat_h(im1, im2):
    im3=Image.open("IST.png")
    im3 = im3.resize((250,100), Image.ANTIALIAS)
    im2 = im2.resize((980,700), Image.ANTIALIAS)
    dst = Image.new('RGB', (im1.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (10,10))
    dst.paste(im3, (740,890))
##    dst.show()
    return dst




def text_wrap(text, font, max_width):
        """Wrap text base on specified width. 
        This is to enable text of width more than the image width to be display
        nicely.
        @params:
            text: str
                text to wrap
            font: obj
                font of the text
            max_width: int
                width to split the text with
        @return
            lines: list[str]
                list of sub-strings
        """
        lines = []
        
        # If the text width is smaller than the image width, then no need to split
        # just add it to the line list and return
        if font.getsize(text)[0]  <= max_width:
            lines.append(text)
        else:
            #split the line by spaces to get words
            words = text.split(' ')
            i = 0
            # append every word to a line while its width is shorter than the image width
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                    line = line + words[i]+ " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines

def createImage(text,subtitle,fileName):
    
    #create image object from the input image path
    try:
        image = Image.open(fileName)   
    except IOError as e:
        print(e)
        
    # Resize the image 
    width = 1000
    img_w = image.size[0]
    img_h = image.size[1]
    wpercent = (width/float(img_w))
    hsize = int((float(img_h)*float(wpercent)))
    rmg = image.resize((width,hsize), Image.ANTIALIAS)
    
    # Set x boundry
    # Take 10% to the left for min and 50% to the left for max
    x_min = (rmg.size[0] * 2) // 100
    x_max = (rmg.size[0] * 2) // 100
    # Randomly select x-axis
    ran_x = randint(x_min, x_max)

    # Create font object with the font file and specify desired size
    # Font style is `arial` and font size is 20
    font_path = 'Montserrat-Bold.ttf'
##    font_path = 'times-bold.ttf' ## Montserrat-Bold
    font = ImageFont.truetype(font=font_path, size=55)
    lines = text_wrap(text, font, rmg.size[0]-ran_x)
    line_height = font.getsize('hg')[1]


    y_min = (rmg.size[1] * 72) // 100   # 4% from the top
    y_max = (rmg.size[1] * 100) //100   # 90% to the bottom
    y_max -= (len(lines)*line_height)  # Adjust
    ##ran_y = randint(y_min, y_max)      # Generate random point
    ran_y = y_min     ## I have change this Akshay 

    #Create draw object
    draw = ImageDraw.Draw(rmg)
    #Draw text on image
    color = 'rgb(255,255,255)'  # Red color ## 245, 203, 66  255,255,255
    x = ran_x
    y = ran_y
    for line in lines:
        draw.text((x,y), line, fill=color, font=font)

        y = y + line_height    # update y-axis for new line
    # Redefine x and y-axis to insert author's name
    y += 5                       # Add some line space
    x += 5                      # Indent it a bit to the right
    font = ImageFont.truetype(font=font_path, size=45)


##    lines2 = text_wrap("@indians_stock_talk", font, rmg.size[0]-40)
##
##    for line in lines2:
##        draw.text((x,y), line, fill=color, font=font)
##        y = y + line_height

        
##    rmg.show()
    rmg.save(fileName)

import re
from bs4 import BeautifulSoup

urls = ["http://www.moneycontrol.com/rss/MCtopnews.xml",
        "http://www.moneycontrol.com/rss/latestnews.xml",
        "http://www.moneycontrol.com/rss/mostpopular.xml",
        "http://www.moneycontrol.com/rss/business.xml", ##
        "http://www.moneycontrol.com/rss/mfcolumns.xml",
        "http://www.moneycontrol.com/rss/pfcolumns.xml",
        "http://www.moneycontrol.com/rss/brokeragerecos.xml", ##
        "http://www.moneycontrol.com/rss/buzzingstocks.xml", ##
        "http://www.moneycontrol.com/rss/economy.xml",
        "http://www.moneycontrol.com/rss/marketreports.xml",
        "http://www.moneycontrol.com/rss/internationalmarkets.xml",
        "http://www.moneycontrol.com/rss/marketedge.xml",
        "http://www.moneycontrol.com/rss/marketoutlook.xml",##
        "http://www.moneycontrol.com/rss/technicals.xml",
        "http://www.moneycontrol.com/rss/insurancenews.xml",
        "http://www.moneycontrol.com/rss/mfnews.xml",
        "http://www.moneycontrol.com/rss/commodities.xml",
        "http://www.moneycontrol.com/rss/results.xml", ##
        "http://www.moneycontrol.com/rss/technology.xml",
        "http://www.moneycontrol.com/rss/currency.xml"]

while True:
    try:
        i=1
        for url in urls:
            try:
                print("\n\n\n",url)
                req = Request(url, headers={'User-Agent': 'Mozilla/7.0', 'Connection': 'close'})
                page = urlopen(req).read()
                soup = BeautifulSoup(page, features="lxml")
                items = soup.findAll('item')
                news_items=[]
                old_csv_data=[]
                print("Before Create")
                try:
                    with open('Combine_News.csv', newline='', encoding='utf-8') as f:
                        pass
                except:
                    print("No File Error")
                    with open('Combine_News.csv', 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)            
                        writer.writerow(["Data"])
                        print("New File Created")
                print("After Create")
                with open('Combine_News.csv', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for data in reader:
            ##            print(str(data))
                        old_csv_data.append(data[0])
                print("After Read")
                for item in items:
                ##    print(item)
                    fileName1=r"imagesRss/"+str(i)
                    fileName="imagesRss/"+str(i)+".jpg"
                    try:
                        news_item = {}
                        news_item['title'] = item.title.text
                        news_item['description'] = item.description.text
            ##            print(item.description.text)
                        resultImg = re.search('<img src="(.*)g"', news_item['description'])
                        news_item['image']=resultImg.group(1)+"g"
            ##            print("Link is ",news_item['link'])
                        news_items.append(news_item)
                        
                        img=Image.open(urlopen(news_item['image']))
                        fileName+="."+img.format
                        img.save((fileName))
                        
                    except Exception as e:
                        print("{0}".format(e))
                        img=Image.open("profile.jpg")
                        img.save((fileName1+"."+img.format)) 
                        print(item.title.text)
                        
                    if item.title.text !=  None:
                        if old_csv_data.count(item.title.text)==0:
##                            bot.send_message("@indians_stock_talk",item.title.text)
                            pass
                        else:
                            continue
                    with open('Combine_News.csv', 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        if item.title.text !=  None:
                            writer.writerow([item.title.text])
                    fileName2="imagesText/"+str(i)+".jpg"

                    img = Image.new('RGB', (1000, 1000), color = (0, 0, 0))

                    fnt = ImageFont.truetype('Montserrat-Bold.ttf', 30)
                    d = ImageDraw.Draw(img)
                    img.save(fileName2)
                    createImage(news_item['title'] ,news_item['description'],fileName2)
                    get_concat_h(Image.open(fileName2), Image.open(fileName)).save(("generated/New"+str(i)+".jpg"))
            ##        bot.send_document("@jobsinind", msg)
##                    bot.sendDocument(chat_id="@stockmarketip", document=open(("generated/New"+str(i)+".jpg"), 'rb'))
                    time.sleep(15)
    ##                bot.send_photo(chat_id="@stockmarketip", photo=open(("generated/New"+str(i)+".jpg"), 'rb'))
                    bot.send_photo(chat_id="@stockmarketip", photo=open(("generated/New"+str(i)+".jpg"), 'rb'))
                    
                    i+=1
            except Exception as e:
                print("Inner Error Redirect To Next URL ",e )
                continue
    except Exception as e:
        print("\n\nError is ",e,"\n\n")
        time.sleep(600)
        continue
    print("\n\nAll URL Executed Sleep for 10 minutes\n\n")
    time.sleep(600)
            
