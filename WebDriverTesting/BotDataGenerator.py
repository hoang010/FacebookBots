import random
import string
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))

#generate names
def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    word += "/"

    for i in range(int(length/2)):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    return word
#generate emails
def generate_email():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito") #prevent pop-up windows from interferring
    driver = webdriver.Chrome("H:\Testing Tools\chromedriver.exe", chrome_options = chrome_options)
    driver.get("https://10minutemail.net/")
    elem = driver.find_element_by_id("fe_text")
    email = elem.get_attribute("value")
    driver.close()
    return email

#generate password
pwd = "Abcdefghijk2019!"
#generate gender
gen = str(random.randint(0,1))

def generateBot():
    try:
        count = int(sys.argv[1])
    except:
        count = 10

    try:
        length = int(sys.argv[2])
    except:
        length = 6
    
    f = open("NewBots.txt", "w")


    data = generate_word(length) + "/" + generate_email() + "/" + pwd + "/" +gen+"\n"
    f.writelines(data)
    f.close()
    print("Finished writting names!")
