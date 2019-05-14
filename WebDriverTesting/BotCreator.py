from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import BotDataGenerator as btgen

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito") #prevent pop-up windows from interferring
driver = webdriver.Chrome("H:\Testing Tools\chromedriver.exe", chrome_options = chrome_options)

#go to site
driver.get("https://www.facebook.com/")

btgen.generateBot()
new_bot = open("NewBots.txt", "r")
bot = new_bot.readline().split("/")
#format of details
#0: first name
#1: surname
#2: email
#3: password
#4: gender
print(bot)
elem = driver.find_element_by_id("u_0_j")
elem.send_keys(bot[0])

elem = driver.find_element_by_id("u_0_l")
elem.send_keys(bot[1])

elem = driver.find_element_by_id("u_0_o")
elem.send_keys(bot[2])
driver.implicitly_wait(10)
elem = driver.find_element_by_id("u_0_r")
elem.send_keys(bot[2])

elem = driver.find_element_by_id("u_0_v")
elem.send_keys(bot[3])

if bot[4] == 0:
    elem = driver.find_element_by_css_selector("input[type='radio'][value='2']").click()
else:
    elem = driver.find_element_by_css_selector("input[type='radio'][value='1']").click()

elem = driver.find_element_by_name("websubmit")
elem.click()

driver.implicitly_wait(10)

elem = driver.find_element_by_css_selector("button._42ft._4jy0.layerConfirm._2rsa.uiOverlayButton._4jy3._4jy1.selected._51sy")
elem.click()


