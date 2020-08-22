'''A program to check the last updated CFS level for Decker's Creek
This is a fun project to teach Bily how to code, with a shit ton of help from Arthur Elmes'''
#importing modules
import bs4 as bs
import urllib.request

#location of desired information in the series of tubes
source = urllib.request.urlopen('https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03062500&parameterCd=00060&siteType=ST&siteStatus=all') .read()
soup = bs.BeautifulSoup (source, 'lxml')

#I don't know why this is here, but it seemed like a good thing
nav = soup.nav

#the location in the website of the data we desire
for wml2 in soup.find_all('wml2:value'):
    print(wml2.string)

#remnants of testing
'''for paragraph in soup.find_all('p'):
    print(paragraph.string)'''

#print(soup.get_text())

