from PIL import Image, ImageDraw, ImageFont
import csv
from random import randint
import telegram
import time
from urllib.request import Request,urlopen




TOKEN = ' ' ##Enter your instagram bot token
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
    y_max = (rmg.size[1] * 90) //100   # 90% to the bottom
    y_max -= (len(lines)*line_height)  # Adjust
    ##ran_y = randint(y_min, y_max)      # Generate random point
    ran_y = y_min     ## I have change this Akshay 

    #Create draw object
    draw = ImageDraw.Draw(rmg)
    #Draw text on image
    color = 'rgb(255,255,255)'  # Red color
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


##import requests
from bs4 import BeautifulSoup



while True:
    urls = ["https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
        "https://economictimes.indiatimes.com/rssfeedsdefault.cms"]
    try:
        i=1
        for url in urls:
            print("\n\n\n",url)
            req = Request(url, headers={'User-Agent': 'Mozilla/7.0', 'Connection': 'close'})
            page = urlopen(req).read()
            soup = BeautifulSoup(page, features="lxml")
##            resp = requests.get(url)
##            soup = BeautifulSoup(resp.content, features="xml")
##            print("Soup\n\n",soup)
            items = soup.findAll('item')
            news_items=[]
            old_csv_data=[]
            try:
                with open('Combine_News1.csv', newline='', encoding='utf-8') as f:
                    pass
            except:
                print("No File Error")
                with open('Combine_News1.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)            
                    writer.writerow(["Data"])
                    print("New File Created")
            print("After Create New File")
            with open('Combine_News1.csv', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for data in reader:
        ##            print(str(data))
                    old_csv_data.append(data[0])
            print("After Reading Data")
            for item in items:
                fileName="imagesRss/"+str(i) 
            ##    print(item)
                try:
                    news_item = {}
                    news_item['title'] = item.title.text
                    news_item['description'] = item.description.text
                    news_item['link'] = item.link.text
                    news_item['image'] = item.image.text
                    news_items.append(news_item)
                    
                    img=Image.open(urlopen(news_item['image']))
                    fileName+="."+img.format
                    img.save((fileName))         
                except Exception as e:
                    print("{0}".format(e))
                    img=Image.open("profile.jpg")
                    img.save((fileName+"."+img.format)) 
                    print(item.title.text)
                if item.title.text !=  None:
                    if old_csv_data.count(item.title.text)==0:
##                        bot.send_message("@stockmarketip",item.title.text)
                        pass
                    else:
                        print("old")
                        continue
                with open('Combine_News1.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    if item.title.text !=  None:
                        writer.writerow([item.title.text])
                fileName2="imagesText/"+str(i)+".jpg"
                img = Image.new('RGB', (1000, 1000), color = (0, 0, 0))
                ##img = Image.new('RGB', (1000, 1000), color = (14, 27, 140))
                ##235, 52, 52
                fnt = ImageFont.truetype('times.ttf', 30)
                d = ImageDraw.Draw(img)
                img.save(fileName2)
                createImage(news_item['title'] ,news_item['description'],fileName2)
                get_concat_h(Image.open(fileName2), Image.open(fileName)).save(("generated/New"+str(i)+".jpg"))
        ##        bot.send_document("@jobsinind", msg)
        ##        bot.sendDocument(chat_id="@stockmarketip", document=open(("generated/New"+str(i)+".jpg"), 'rb'))
                time.sleep(15)
##                bot.send_photo(chat_id="@stockmarketip", photo=open(("generated/New"+str(i)+".jpg"), 'rb'))
                bot.send_photo(chat_id="@indians_stock_talk", photo=open(("generated/New"+str(i)+".jpg"), 'rb'))
                i+=1
    except Exception as e:
        print("\n\nError {0}".format(e))
        time.sleep(600)
        continue
    time.sleep(600)
            
