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
delay = 4 #minumum
#######################

def scroll():
    js = '''
    page = document.querySelector(".isgrP");
    page.scrollTo(0,page.scrollHeight);
    var end_page = page.scrollHeight;
    return end_page;
    '''
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
    following = []
    followers = []
    for i in [2,3]:
        go_profile(username)
        click_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li["+str(i)+"]/a/div")
        action.click(on_element = click_button).perform()
        time.sleep(delay+3)
        scroll()
        time.sleep(delay+2)
        source = BeautifulSoup(browser.page_source, 'lxml')
        source = source.find("div",{"class":"isgrP"})
        source = source.find_all("a")
        if i == 2:
            for i in source:
                try:
                    followers.append(i.find("span").text)
                except:
                    pass
        else:
            for i in source:
                try:
                    following.append(i.find("span").text)
                except:
                    pass

    difference = set(following) - set(followers)
    return [len(following),len(followers),len(difference),difference]


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
result = get_f_f()
print("####### Unfollowers List #######");print(result[3])
print("#Following : "+str(result[0]))
print("#Followers : "+str(result[1]))
print("#Unfollowers : "+str(result[2]))


"""
### Unfollow every non followers
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
#Do
login() #Login instagram
go_profile(username) #Go profile
who_dont_follow_you = get_f_f() #Get List
print(who_dont_follow_you)
#unfollowbot(who_dont_follow_you) #Unfollow
"""
