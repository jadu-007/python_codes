from PIL import Image, ImageDraw, ImageFont
from urllib.request import Request,urlopen
url="http://www.moneycontrol.com/news_image_files/2016/s/Sensex_BSE_Stockmarket_bulls_bear_down_red_200x200.jpg"
img=Image.open(urlopen(url))
img.save(("Urlib.jpg"))
