from bs4 import BeautifulSoup
from PIL import Image
import requests
import shutil
import os

# Connect
website = "https://readberserk.com/"
website_source = BeautifulSoup(requests.get(website).content,"lxml")
chapters_links = website_source.find_all("a",{"class":"btn btn-sm btn-primary mr-2"})

# Loop for all chapters
for chapter_link in chapters_links[::-1]:
    print("\n\n#############################")

    # Create Directory and Go
    if os.path.isdir('imagesfolder') == True:
        shutil.rmtree('imagesfolder')
    os.mkdir("imagesfolder")
    os.chdir("imagesfolder")

    # Chapter
    chapter_link = chapter_link.get("href")
    print(chapter_link)
    chapter_source = BeautifulSoup(requests.get(chapter_link).content,"lxml")

    # Take Images
    images_names = []
    print("Total images :", len(chapter_source.find_all("img",{"class":"pages__img"})))
    for i in chapter_source.find_all("img",{"class":"pages__img"}):
        image_link = i.get("src")
        if "?" in image_link:
            image_link = image_link[:image_link.find("?")]
        image_link = image_link.strip()
        file_name = image_link[image_link.rfind("/")+1:]
        if "proxy" in file_name:
            continue
        images_names.append(file_name)

    # Save Images
        try:
            img_data = requests.get(image_link).content
            with open(file_name, 'wb') as handler:
                handler.write(img_data)
                print(file_name,"Done")
        except:
            print(file_name)

    # Create Pdf
    print("PDF Preparing...")
    pdf_name = chapter_link[chapter_link.find("-chapter")+1:-1]
    pdf_list = []
    for i in images_names:
        pdf_list.append(Image.open(i).convert("RGB"))
    pdf_list[0].save("../"+pdf_name+".pdf",save_all=True,append_images=pdf_list[1:])
    print("PDF Done")

    # Remove Directory
    os.chdir("../")
    shutil.rmtree('imagesfolder')
