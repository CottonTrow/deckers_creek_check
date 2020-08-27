#importing modules
import bs4 as bs
import urllib.request
import time

#location of desired information in the series of tubes
'''source = urllib.request.urlopen('https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03062500&
parameterCd=00060&siteType=ST&siteStatus=all').read()
source1 = urllib.request.urlopen('https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03066000&parameterCd=
00060&siteType=ST&siteStatus=all').read()
source2 = urllib.request.urlopen('https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03070260&parameterCd=
00060&siteType=ST&siteStatus=all').read()

soup = bs.BeautifulSoup(source, 'xml')
soup1 = bs.BeautifulSoup(source1, 'xml')
soup2 = bs.BeautifulSoup(source2, 'xml')

#the location in the website of the data we desire
for wml2 in soup.find_all('wml2:value'):
    print('The level of Deckers is currently:')
    print(wml2.string)

for wml2 in soup1.find_all('wml2:value'):
    print('The level of the Blackwater is currently:')
    print(wml2.string)

for wml2 in soup2.find_all('wml2:value'):
    print('The level of the Cheat is currently:')
    print(wml2.string)'''

url_dict = {'link 1': 'https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03062500&parameterCd=00060&siteT'
                      'ype=ST&siteStatus=all', 'link 2': 'https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sit'
                      'es=03066000&parameterCd=00060&siteType=ST&siteStatus=all', 'link 3': 'https://waterservices.usgs.'
                      'gov/nwis/iv/?format=waterml,2.0&sites=03070260&parameterCd=00060&siteType=ST&siteStatus=all'}
for x in url_dict:
    print(url_dict[x])
for x in url_dict:
    print(x)
for k, v in url_dict.items():
    print(k, v)