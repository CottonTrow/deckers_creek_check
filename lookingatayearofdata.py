'''A program to check the last updated CFS level for Decker's Creek
This is a fun project to teach Bily how to code, with a shit ton of help from Arthur Elmes'''
#importing modules
import bs4 as bs
import urllib.request
from datetime import datetime
import numpy as np
import pandas as pd
import sys

# location of desired information in the series of tubes
source = urllib.request.urlopen('https://nwis.waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03062500&period='
                                'P365D&parameterCd=00060&siteType=ST&siteStatus=all').read()
soup = bs.BeautifulSoup(source, 'xml')

# the lists that will hold all of the values
cfs = []
runnablecfs = []
timestamp = []


# gathering the cfs values
for wml2 in soup.find_all('wml2:value'):
    cfs.append(float(wml2.string))

# check to see if items move into new list
# print(len(cfs))
# print(len(runnablecfs))

for x in cfs:
    if 270 < x < 600:
        runnablecfs.append(x)

# print(len(cfs))
# print(len(runnablecfs))

#gathering the timestamps
for wml2 in soup.find_all('wml2:time'):
    timestamp.append(wml2.string)

i = 0
while i < len(timestamp):
    date_str = timestamp[i][:19]
    timestamp[i] = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    i += 1
del i

#print(timestamp)


# for s in timestamp:
#     s = s[:19]
#     s = datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')


#splicing the timestamps and cfs values
decker_dict = dict(zip(timestamp, cfs))
#print(decker_dict)


#filtering out duplicate days
"""Figuring out how to use panda, I trying out two different methods for creating the dataframe"""

df = pd.DataFrame.from_dict(decker_dict, orient='index')
df = df.reset_index()
df = df.rename(columns = {'index':'Date',0:'CFS'})
#df['date_no_time'] = datetime.strptime(df['index'], "%Y-%m-%d")

# print(type(df['Date','CFS']))
print(df)
#df['date'] = df['index'].dt.normalize()
#df['date_no_time'] = pd.to_datetime(df['index']).dt.date

# d = {'col1': [timestamp], 'col2': [cfs]}
# dp = pd.DataFrame(d)

#print(dp.head())
sys.exit()



#print(dp)
#s = pd.DataFrame(df.items(), columns=['Date', 'Value'])
#print(s)

