# first import Pandas
import pandas as pd

# Retrieve the team colors that were downloaded in an XML file

import xml.etree.ElementTree as ET
tree = ET.parse('colors.xml')
root = tree.getroot()

# Parse through the XML

teams = []
name = []
colors = []
for node in root:
    teams.append(node.text.strip())
    name.append(node[0].text.strip())
    tmp = []
    for i in range(1, len(node)):
        tmp.append(node[i].text.strip())
    while len(tmp) < 5:
        tmp.append('')
    colors.append(tmp)

# load the data in a Pandas dataframe

df = pd.DataFrame()

df['Teams'] = teams
df['Abbrv'] = name
df2 = pd.DataFrame(colors)
df = pd.concat([df, df2], axis=1)
df.index = df['Abbrv']
df.to_csv('colors.csv')
