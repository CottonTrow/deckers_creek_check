"""Test script to pull streamflow values from https://waterdata.usgs.gov/wv/nwis/current/?type=flow
Authors:
Arthur Elmes
Bily Brown
2020-08"""

# import stuff
from bs4 import BeautifulSoup
import requests
import sys

# set the url and send a GET request using requests module
url = "https://waterdata.usgs.gov/wv/nwis/current/?type=flow"
req = requests.get(url)

# construct a soup object to parse the contents
soup = BeautifulSoup(req.text, "html.parser")

# find all the list items with html tag <td>
tds = soup.find_all("td")

# find all tables
tables = soup.find_all("table")

# find the table of interest, but this is currently wonky because the only
# defining characteristic is the cellspacing attribute
table_stmflow = soup.find("table", attrs={"cellspacing": "1"})
table_stmflow_data = table_stmflow.tbody.find_all("tr")
#print(table_stmflow_data)

entries = []
i = 0
while i < len(table_stmflow_data):
    for td in table_stmflow_data[i].find_all("td"):
        for td2 in td.children:
            #print(type(td2))
            entries.append(td2)
        i += 1

for entry in entries:
    print(entry)

#print(soup.prettify())
# for table in tables:
#     print(table.name)
#     for child in table.children:
#         print(child)
