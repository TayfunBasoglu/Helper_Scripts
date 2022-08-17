# selenium 4.4.0
# chrome driver (put in same folder) 104.0.5112.102
# 08.2022

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

username = "username"
password = "password"
delay = 4 #minumum


def go_profile(usern):
    time.sleep(delay)
    browser.get("https://www.instagram.com/"+str(usern))
    time.sleep(delay+5)
    source = BeautifulSoup(browser.page_source, 'lxml')
    source = source.find("ul",{"class":"_aa_7"})
    follow = []
    for i in source.find_all('span'):
        follow.append(i.text)  
    globals()["followers_total"] = follow[1]
    globals()["following_total"] = follow[2]
    

def login():
    time.sleep(delay)
    username_send = browser.find_element('name','username').send_keys(username)
    time.sleep(delay)
    password_send = browser.find_element('name','password').send_keys(password)
    time.sleep(delay)
    click = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()


def followdata():

    followers_list = []
    following_list = []
    
    for page in ["followers","following"]:
        browser.get("https://www.instagram.com/"+username+"/"+page)
        time.sleep(delay+2)

        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB * 2).perform()
        
        if page == "followers":
            for a in range(1,int(int(followers_total)/2)):
                actions.send_keys(Keys.SPACE).perform()
                time.sleep(0.7)
        elif page == "following":
            for a in range(1,int(int(following_total)/2)):
                actions.send_keys(Keys.SPACE).perform()
                time.sleep(0.7)      

        source = BeautifulSoup(browser.page_source, 'lxml')
        source = source.find("div",{"class":"_aano"})
        
        for x in source.find_all("a"):
            if page == "followers":
                followers_list.append(x.text)
            elif page == "following":
                following_list.append(x.text)

    difference = set(following_list) - set(followers_list)
    print("\n\n\n",difference)
    print("Followers :", followers_total)
    print("Following :", following_total)
    print("Difference :", len(difference))


# Open Instagram
browser = webdriver.Chrome()
browser.get("http://instagram.com")
time.sleep(delay+2)


#Do
login() #Login instagram
go_profile(username) #Go profile
followdata()
