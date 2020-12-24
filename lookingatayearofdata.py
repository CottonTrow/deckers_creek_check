'''A program to check the last updated CFS level for Blackwater River at Davis
This is a fun project to teach Bily how to code, with a shit ton of help from Arthur Elmes'''
# importing modules
import bs4 as bs
import urllib.request
from datetime import datetime
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# location of desired information in the series of tubes for the alley
source = urllib.request.urlopen('https://nwis.waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&sites=03070260&startDT'
             '=2020-01-01T00:00-0500&endDT=2020-12-31T23:59-0500&parameterCd=00060&siteType=ST&siteStatus=all').read()
soup = bs.BeautifulSoup(source, 'xml')

# the lists that will hold all of the values
cfs = []
runnablecfs = []
timestamp = []


# gathering the cfs values
def acquire_data():
    for wml2 in soup.find_all('wml2:value'):
        cfs.append(float(wml2.string))
    for wml2 in soup.find_all('wml2:time'):
        timestamp.append(wml2.string)


'''for x in cfs:
    if 700 < x < 2000:
        runnablecfs.append(x)'''

# print(len(cfs))
# print(len(runnablecfs))


acquire_data()

i = 0
while i < len(timestamp):
    date_str = timestamp[i][:19]
    timestamp[i] = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    i += 1
del i

#I want to turn this into a function
new_dict = dict(zip(timestamp, cfs))
df = pd.DataFrame.from_dict(new_dict, orient='index')
df = df.reset_index()
df = df.rename(columns={'index': 'Date', 0: 'CFS'})
df['ReDoneDates'] = pd.DatetimeIndex(df['Date']).to_period('D')
df['Month'] = pd.DatetimeIndex(df['Date']).month
df['Month'] = df['Month'].astype('int32')
df['Day'] = pd.DatetimeIndex(df['Date']).day
df['Day'] = df['Day'].astype('int32')



new_df = df.loc[(df['CFS'] < 2000) & (df['CFS'] > 700)]
newer_df = new_df.drop_duplicates(subset=['ReDoneDates'], keep='first')

groupdf = newer_df.groupby(pd.Grouper(key='Date',freq='M')).count()
groupdf.drop(['ReDoneDates', 'Month', 'Day'], axis=1, inplace=True)
groupdf.plot()
#I want to figure out how to get the legend to draw the legend name from the date supplied by data
plt.legend(['2020'])
plt.xticks()
plt.ylabel('# of Days the CFS range was between 700 and 2000')
plt.xlabel('Month')
plt.show()

print(len(newer_df))
#newer_df.to_excel("AlleyDaze.xlsx",
#           sheet_name='Sheet_name_1')






sys.exit()