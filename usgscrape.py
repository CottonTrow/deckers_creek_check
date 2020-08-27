'''A program to check the last updated CFS level for Decker's Creek
This is a fun project to teach Bily how to code, with a shit ton of help from Arthur Elmes'''
#importing modules
import bs4 as bs
import urllib.request
import time

# So I'm not sure where you're generating these urls
# Ideal would be to have some sort of automated link crawler or something?
# But if there are a few that never change, I'd make a list or dictionary to cycle
# through them

# A list is contstructed with square brackets, and can contain however many
# of whatever type of things. Access individual items with an index number like
# list_item = url_list[3] would retrieve the 4th item in the list (0-based)
url_list = ['https://waterservices.usgs.gov/nwis/iv/' +
            '?format=waterml,2.0&sites=03062500&parameterCd' +
            '=00060&siteType=ST&siteStatus=all', 'https://someotherlink',
            'https://someotherlink2', 'https://someotherlink3']

# A dictionary is sexier because it gets accessed a lot faster and with a key,
# rather than with an index, and is constructed using curly brackets {}
# list_item = url_dict.get('Link 1')
url_dict = {'Link 1': 'https://waterservices.usgs.gov/nwis/iv/' +
            '?format=waterml,2.0&sites=03062500&parameterCd' +
            '=00060&siteType=ST&siteStatus=all',
            'Link 2': 'https://waterservices.usgs.gov/blahblahblah1' +
            '=00060&siteType=ST&siteStatus=all',
            'Link 3': 'https://waterservices.usgs.gov/blahblahblah2'}

test_url_1 = url_list[2]
test_url_2 = url_dict.get('Link 3')
print(test_url_1)
print(test_url_2)

#location of desired information in the series of tubes
source = urllib.request.urlopen('https://waterservices.usgs.gov/nwis/iv/' +
                                '?format=waterml,2.0&sites=03062500&parameterCd' +
                                '=00060&siteType=ST&siteStatus=all').read()
# I split that long-ass url. Generally it's good to stack long things or long lists of
# text vertically

soup = bs.BeautifulSoup(source, 'xml')

# the location in the website of the data we desire
for wml2 in soup.find_all('wml2:value'):
    print('The level is currently:')
    print(wml2.string)

# creating my analysis
cfs = float(wml2.string)

if 270 < cfs < 600:
    print("Decker's is running. You should go paddling")
else:
    print("Maybe you should find something else to do.")

# One thing that comes to mind is to start making your own database of these observations
# using a csv. You can open it in writing mode and append the most recent value
# then with another script you could plot out the trends etc.

time.sleep(15)

