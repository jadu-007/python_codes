from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time
from os.path import isfile, join
from os import listdir

from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time

username = " " #Enter instagram username
passwd = " " ##Enter instagram password
driverpth = "chromedriver.exe"
photopath = "C:\\Users\\Akshay\\Desktop\\Workspace\\Instagram\\imagesAk\\akshay.jpg" #examp "C:\\Users\\alire\\PycharmProjects\\instagrambot2\\logo.png"
phototext = "Hey Follow our page for more funny stuffs"

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(executable_path=driverpth,options=options)
driver.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(passwd)
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()


while 1:
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/button").click()
        break
    except:
        pass
print("First While")
while 1:
    time.sleep(1)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        break
    except:
        pass
print("Second While")
while 1:
    time.sleep(1)
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        break
    except:
        pass
print("Third While")

    
def upload(photopath):
    
    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    time.sleep(1.5)
    autoit.win_active("Open") #open can change by your os language if not open change that
    time.sleep(7)
    autoit.control_send("Open", "Edit1", str(photopath))
    time.sleep(3)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div[1]/div[2]//button").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(phototext)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(600)
photopath = "G:\\Workspace\\Instagram\\imagesAk\\"
##C:\\Users\\Akshay\\Desktop\\Workspace\\Instagram\\imagesAk\\  G:\\Workspace\\Instagram\\imagesAk
ListFiles = sorted([f for f in listdir(photopath) if isfile(join(photopath, f))])
for i in (ListFiles):
    upload(photopath+str(i))
    time.sleep(5)
