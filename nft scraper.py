import cloudscraper
import requests
from bs4 import BeautifulSoup
import os
import urllib.request

#######################################################
#  CHANGE THIS VARIABLE TO CHANGE DOWNLOAD DIRECTORY  #
#######################################################
DOWNLOADS_DIR = 'D:/bored_apes'






def clear(): return os.system('cls')

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
def getdata(url):
    r = requests.get(url)
    return r.text


def get_links():
    page = 1
    while page <= 200:
        htmldata = scraper.get("https://nftrarity.net/boredapeyachtclub?page="+str(page)).text

        soup = BeautifulSoup(htmldata, 'html.parser')

        for item in soup.find_all('img'):
            with open("links.txt", "a") as links:
                links.write(item['src']+'0'+'\n')

        clear()
        print(str(page)+" out of 200 files found  "+str(page/2)+"% complete")
        page = page + 1

def download_images():
    download_number = 1
    
    links = open('links.txt', 'r')
    for link in links:
        link = link.strip()
        name = link.rsplit('/', 1)[-1]
        filename = os.path.join(DOWNLOADS_DIR, name+'.png')

        if not os.path.isfile(filename):
            print('Downloading: ' + filename)
            try:
                urllib.request.urlretrieve(link, filename)
            except Exception as inst:
                print(inst)
                print('  Encountered unknown error. Continuing.')


print('********************************************')
print('***********  BORED APE DOWNLOADER  *********')
print('***********      BY BASIL <3       *********')
print('********************************************')
print('1. Do All Options')
print('2. Download List of All Images')
print('3. Download Images From links.txt')
choice = int(input('Please select an option'))

if choice == 1:
    get_links()
    download_images()
    print('1')
elif choice == 2:
    get_links()
elif choice == 3:
    download_images()
else:
    print('err: not a number')




