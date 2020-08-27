'''A program to check the last updated CFS level for Decker's Creek
This is a fun project to teach Bily how to code, with a shit ton of help from Arthur Elmes'''
#importing modules
import bs4 as bs
import urllib.request
from collections import Counter

#location of desired information in the series of tubes
source = urllib.request.urlopen('https://nwis.waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03062500&period='
                                'P365D&parameterCd=00060&siteType=ST&siteStatus=all') .read()
soup = bs.BeautifulSoup(source, 'xml')
#the list that will hold all of the values
cfs = []
runnablecfs = []
timestamp = []
#the location in the website of the data we desire
for wml2 in soup.find_all('wml2:value'):
#propogating the list
    cfs.append(float(wml2.string))

#check to see if items move into new list
print(len(cfs))
print(len(runnablecfs))

for x in cfs:
    if 270 < x < 600:
        runnablecfs.append(x)

print(len(cfs))
print(len(runnablecfs))

#Introducing the time stamp
for wml2 in soup.find_all('wml2:time'):
    timestamp.append(wml2.string)



