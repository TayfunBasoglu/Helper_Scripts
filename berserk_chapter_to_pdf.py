import requests
from bs4 import BeautifulSoup
import os
import time
from PIL import Image
import shutil


#chapter url 
#https://readberserk.com/ or https://berserkchapters.com/
page_url = "https://readberserk.com/chapter/berserk-chapter-a0/"


#Create Directory and Go
if os.path.isdir('downloadfoldercreateee') == True:
    shutil.rmtree('downloadfoldercreateee')
os.mkdir("downloadfoldercreateee")
os.chdir("downloadfoldercreateee")

#Connect and Get Images
image_names_list = []
source = BeautifulSoup(requests.get(page_url).content,"lxml")
list_general = str(source).split(" ")
for i in list_general:
    
    if (".jpg" in i or ".jpeg" in i or ".png" in i) and ("http" in i or "https" in i) and 'content="htt' not in i and "baseUrl" not in i and "ImageObject" not in i and "XWnLr5m" not in i:
        url_image = i[i.find('"')+1:i.find('"',5)]
        url_image = i[i.find('"')+1:i.find('"',5)]
        img_data = requests.get(url_image).content
        time.sleep(0.3)
        file_name = url_image[url_image.rfind("/")+1:]
        print(file_name,"done")
        image_names_list.append(file_name)
        with open(file_name, 'wb') as handler:
            handler.write(img_data)


#Create Pdf
pdf_list = []
print("Preparing PDF")
for i in image_names_list:
    pdf_list.append(Image.open(i).convert("RGB"))
pdf_list[0].save("../"+page_url[page_url.find("berserk",20):-1]+".pdf",save_all=True,append_images=pdf_list[1:])
os.chdir("../")
shutil.rmtree('downloadfoldercreateee')
