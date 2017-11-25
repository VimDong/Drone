__author__ = 'Vim'
import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.jiandan.net'

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
# get
source_code = requests.get(url, headers = header)
plain_text = source_code.text

Soup = BeautifulSoup(plain_text, "html.parser")

download_links = []
folder_path = '/Users/Vim/Downloads/download_pic/'
for pic_tag in Soup.find_all('img'):
    pic_link = pic_tag.get('src')
    download_links.append(pic_link)

for item in download_links:
    urllib.request.urlretrieve(item,folder_path + item[-6:])
    print('Done')
