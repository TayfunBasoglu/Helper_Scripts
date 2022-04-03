from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

# Detect non-followers and unfollow one by one.
# Chome Version 100.0.4896.60 (Official Build) (64-bit)
# chromedriver.exe must be in the same directory

#######################
username = "username"
password = "password"
delay = 3 #min
#######################

def scroll():
    js = """
    page = document.querySelector(".isgrP");
    page.scrollTo(0,page.scrollHeight);
    var end_page = page.scrollHeight;
    return end_page;
    """
    end_page = browser.execute_script(js)
    while True:
        end = end_page 
        time.sleep(delay)
        end_page = browser.execute_script(js)
        if end == end_page:
            time.sleep(delay)
            break

def go_profile(usern):
    browser.get("https://www.instagram.com/"+str(usern))
    time.sleep(delay+2)

def login():
    username_send = browser.find_element_by_name('username').send_keys(username)
    time.sleep(delay)
    password_send = browser.find_element_by_name('password').send_keys(password)
    time.sleep(delay)
    click = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(delay+2)

def get_f_f():
    followers = []
    following = []
    for i in [3,2]:   
        click_followers = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li["+str(i)+"]/a/div")
        action.click(on_element = click_followers).perform()
        time.sleep(delay+3)
        scroll()
        time.sleep(delay+2)
        source = BeautifulSoup(browser.page_source, 'lxml')
        source = source.find("div",{"class":"isgrP"}).find_all("a")
        if i == 3:
            for i in source:
                following.append(str(i.get("href"))[1:-1])
                
        else:
            for i in source:
                followers.append(str(i.get("href"))[1:-1])
    return following

def unfollowbot(unf_list):
    for i in list(unf_list)[:50]:
        go_profile(str(i))
        time.sleep(delay+2)
        click_following = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")
        action.click(on_element = click_following).perform()
        time.sleep(delay)
        click_following = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
        action.click(on_element = click_following).perform()
        time.sleep(delay)

# Open Instagram
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
action = ActionChains(browser)
browser.get("http://instagram.com")
time.sleep(delay+2)


#Do
login() #Login instagram
go_profile(username) #Go profile
who_dont_follow_you = get_f_f() #Get List
unfollowbot(who_dont_follow_you) #Unfollow
