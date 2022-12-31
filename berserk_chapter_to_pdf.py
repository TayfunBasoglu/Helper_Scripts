import requests
from bs4 import BeautifulSoup
import os
import time
from PIL import Image
import shutil


#chapter url 
#https://readberserk.com/ or https://berserkchapters.com/
page_url = "https://readberserk.com/chapter/berserk-chapter-015/"


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
        print(url_image)
