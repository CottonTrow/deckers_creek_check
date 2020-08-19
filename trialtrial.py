from bs4 import BeautifulSoup
import requests

url = "https://waterservices.usgs.gov/nwis/iv/?format=rdb&sites=03062500&parameterCd=00060,00065&siteType=ST&siteStatus=all"
req = requests.get(url)

soup=BeautifulSoup(req.text, 'html.parser')

print(soup.get_text)

"""streamflow = float(input('What is the streamflow:'))

if streamflow > 270 and 600 > streamflow:
    print('GO RUN THAT SHIT')

else:
    print('You better find something else to do')"""