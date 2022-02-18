import requests
from bs4 import BeautifulSoup

##### Profile Username
username = "tayyfun"

#lists
following = []
followers = []

#get follow lists
def get_users(source,page_name):
    persons = source.find_all("div",attrs={"class":"person-summary"})
    for i in persons:
        if page_name == "following":   
            following.append(i.find("h3").find("a")["href"])
        else:
            followers.append(i.find("h3").find("a")["href"])

#get pages
def connect_page(page_name):
    print("Getting",page_name,"list...")
    page_num = 1
    while True:
        url = "https://letterboxd.com/"+str(username)+"/"+page_name+"/page/"+str(page_num)+"/"
        source = BeautifulSoup(requests.get(url).content,"lxml")
        if '<a class="next" href="/'+username+'/'+page_name+'/' in str(source):
            get_users(source,page_name)
            page_num += 1
        else:
            get_users(source,page_name)
            break

#pages loop
for page_names in ("following","followers"):
    connect_page(page_names)

#list
print("\n\n# List of unfollowers")
difference_list = set(following) - set(followers)

if len(difference_list) == 0:
    print("0 person")
else:
    for i in difference_list:
        print("  -",i[1:-1])
