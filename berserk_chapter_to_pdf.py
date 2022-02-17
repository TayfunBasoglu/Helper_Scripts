import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

#chapter url
page_url = "http://berserkmanga.net/manga/berserk-chapter-1/"

#Create Directory and Go
os.mkdir("downloadfoldercreateee")
os.chdir("downloadfoldercreateee")

#Connect and Get Images
source = BeautifulSoup(requests.get(page_url).content,"lxml")
images_list = []
for i in source.find_all("div",attrs={"class":"img_container"}):
  images_list.append(i.find("img")["src"])
  
#Download Images
value = 1
for u in images_list:
    print("downloading",u,"as",str(value)+".jpg")
    r = requests.get(u, allow_redirects=True)
    open(str(value)+".jpg", 'wb').write(r.content)
    value +=1

#Make pdf_name
pdf_name = None
if page_url[page_url[:-2].rfind("/")+1:].endswith("/"):
    pdf_name = page_url[page_url[:-2].rfind("/")+1:-1]+".pdf"
else:
    pdf_name = page_url[page_url[:-2].rfind("/")+1:]+".pdf"

#Sort Images 
file_list_sorted = sorted(os.listdir().copy(), key=lambda x: int(os.path.splitext(x)[0]))

#Create Pdf
liste = []
print("Preparing PDF")
for i in file_list_sorted[0:]:
    if str(i).endswith("jpg"):
        liste.append(Image.open(i).convert("RGB"))
liste[0].save("../"+str(pdf_name),save_all=True,append_images=liste[1:])

#Remove Files and Directory
for files in os.listdir():
    os.remove(files)
os.chdir("../")
os.rmdir("downloadfoldercreateee")
print("Done")
