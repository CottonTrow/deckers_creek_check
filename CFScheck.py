'''A program to check the last updated CFS level for any river in the USGS database
This is a fun project to teach Bily how to code, with a shit ton of help from Arthur Elmes'''
'''To use this code you have to generate a WML2 website from USGS using this link 
-https://waterservices.usgs.gov/rest/IV-Test-Tool.html-
Enter in the USGS site number and 00060 under parameter code to get CFS
Paste that website as the source and then set your CFS range'''
# importing modules
import bs4 as bs
import urllib.request
from datetime import datetime
import numpy as np
import pandas as pd
import sys

# looking at data from a range of the past 365 days for the blackwater
source = urllib.request.urlopen('https://nwis.waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03066000&period='
                                'P365D&parameterCd=00060&siteType=ST&siteStatus=all').read()
soup = bs.BeautifulSoup(source, 'xml')

# the lists that will hold all of the values
cfs = []
timestamp = []


# gathering the cfs values
for wml2 in soup.find_all('wml2:value'):
    cfs.append(float(wml2.string))

# gathering the timestamps
for wml2 in soup.find_all('wml2:time'):
    timestamp.append(wml2.string)

i = 0
while i < len(timestamp):
    date_str = timestamp[i][:19]
    timestamp[i] = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    i += 1
del i

# splicing the timestamps and cfs values
new_dict = dict(zip(timestamp, cfs))

# filtering out duplicate days

df = pd.DataFrame.from_dict(new_dict, orient='index')
df = df.reset_index()
df = df.rename(columns = {'index':'Date',0:'CFS'})
# get it? redundant? Redonedate!
df['ReDoneDates'] = pd.DatetimeIndex(df['Date']).to_period('D')

new_df = df.loc[(df['CFS'] < 600) & (df['CFS'] > 250)]
newer_df = new_df.drop_duplicates(subset=['ReDoneDates'], keep='first')
# print(df.head(5))
# print(newer_df.head(5))
print(len(newer_df))

# print(df.sort_values(['CFS'], ascending=False))
# print(df.mean())
sys.exit()





