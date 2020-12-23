'''A program to check the last updated CFS level for Blackwater River at Davis
This is a fun project to teach Bily how to code, with a shit ton of help from Arthur Elmes'''
# importing modules
import bs4 as bs
import urllib.request
from datetime import datetime
import numpy as np
import pandas as pd
import sys

# location of desired information in the series of tubes for the alley
source = urllib.request.urlopen('https://nwis.waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03070260&startDT'
             '=2020-01-01T00:00-0500&endDT=2020-12-31T23:59-0500&parameterCd=00060&siteType=ST&siteStatus=all').read()
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
    if 700 < x < 2000:
        runnablecfs.append(x)

# print(len(cfs))
# print(len(runnablecfs))

# gathering the timestamps
for wml2 in soup.find_all('wml2:time'):
    timestamp.append(wml2.string)

i = 0
while i < len(timestamp):
    date_str = timestamp[i][:19]
    timestamp[i] = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    i += 1
del i

#print(timestamp)


#for s in timestamp:
 #    s = s[:19]
  #   s = datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')


# splicing the timestamps and cfs values
bw_dict = dict(zip(timestamp, cfs))
# print('The previous 365 days of data for the Blackwater river at Davis')
#print(bw_dict)


# filtering out duplicate days
"""Figuring out how to use panda, I trying out two different methods for creating the dataframe"""




df = pd.DataFrame.from_dict(bw_dict, orient='index')
df = df.reset_index()
df = df.rename(columns = {'index':'Date',0:'CFS'})
# get it? redundant? Redonedate!
df['ReDoneDates'] = pd.DatetimeIndex(df['Date']).to_period('D')
df = (df.drop_duplicates(subset=['ReDoneDates'], keep='first'))
df['Month'] = pd.DatetimeIndex(df['Date']).month


df1 = (df.loc[(df['CFS'] > 700) & (df['CFS'] < 2000)])
# print (df)
# print (len(df1))
print(df1.head(5))
# df1.to_excel("AlleyDaze.xlsx",
#            sheet_name='Sheet_name_1')




sys.exit()





