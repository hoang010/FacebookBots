from selenium import webdriver
from selenium.webdriver.common.keys import Keys

f = open("AccountDetails.txt", "r")
lines = f.readlines()

details = lines[0].split("/")

user = details[0] #first part is username
pwd = details[1] #secondpart is password

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito") #prevent pop-up windows from interferring
driver = webdriver.Chrome("H:\Testing Tools\chromedriver.exe", chrome_options = chrome_options)

driver.get("https://www.facebook.com/")

assert "Facebook" in driver.title #check that the page is Facebook
#log in
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)


elem = driver.find_element_by_css_selector("_1vp5")[0]
elem.click()
driver.implicitly_wait(10000)

driver.get("https://www.facebook.com/hoang.nguyenle.3")

elem = driver.find_elements_by_css_selector("button._42ft._4jy0.FriendRequestAdd.addButton._4jy4._517h._9c6")[0]
elem.click()

driver.get("https://www.facebook.com/hoang.nguyenle.3")
driver.implicitly_wait(10)
driver.close()
