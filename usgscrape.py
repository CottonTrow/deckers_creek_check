'''A program to check the last updated CFS level for Decker's Creek
This is a fun project to teach Bily how to code, with a shit ton of help from Arthur Elmes'''
#importing modules
import bs4 as bs
import urllib.request

#location of desired information in the series of tubes
source = urllib.request.urlopen('https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03062500&parameterCd=00060&siteType=ST&siteStatus=all') .read()
soup = bs.BeautifulSoup (source, 'lxml')

#the location in the website of the data we desire
for wml2 in soup.find_all('wml2:value'):
    print('The level is currently:')
    print(wml2.string)

#creating my analysis
cfs = float(wml2.string)

if cfs > 270 and 600 > cfs:
    print("Decker's is running. You should go paddling")
else: print("Maybe you should find something else to do.")

