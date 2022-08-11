# webscraping -> what you can do after you retrieve informatio from a webpage
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# http://www.dr-chuck.com/page1.htm
url = input('Enter url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
print(tags)
for tag in tags:
    print(tag.get('href'))