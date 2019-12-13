import json
import pandas as pd
from math import isclose
df = pd.read_csv('uszips.csv')
ndf = pd.DataFrame(columns=['Zipcode','Number of tweets from that zipcode','Zips'])
zips=[]
tweets=[]
count=0
# print(df['lat'])
with open('Florence_geo_0917.json') as access_json:
    read_content = json.load(access_json)
    
    for i in read_content:
        #i is a dictionary
        place = i['place']
        box = place['bounding_box']
        shape = box['type']
        c = box['coordinates']
        c = c[0]
        c0 = c[0]
        c2 = c[2]
        lon = (c0[0]+c2[0])/2
        lat = (c0[1]+c2[1])/2
        loc = [lat,lon]
        for index, row in df.iterrows():
            if isclose(lat, df.loc[index,'lat'], abs_tol=1e-1) and isclose(lon, df.loc[index,'lng'], abs_tol=1e-1):
                zips.append(df.loc[index,'zip'])
                print(df.loc[index,'zip'])
                break
    #now we have zipcodes
    ndf['Zips']=zips
    
    unique = [-1]
    for index,row in ndf.iterrows():
        for el in unique:
            if row['Zips'] not in unique:
                unique.append(row['Zips'])
    del unique[0]
    ndf['Zipcode']=unique
    ndf['Number of tweets from that zipcode']=0
    
    for index,row in ndf.iterrows():
        for i in zips:
            if i==ndf.loc[index,'Zipcode']:
                ndf.loc[index,'Number of tweets from that zipcode']+=1
                print(ndf.loc[index,'Number of tweets from that zipcode'])
                
    ndf.to_excel("New Twitter.xlsx")
        
d = pd.read_csv('zips found.csv')
zipc = d['zips']
uni = []
for index,row in d.iterrows():
    if row['zips'] not in uni:
        uni.append(row['zips'])
print(uni)
nd = pd.DataFrame(columns=['Zipcode','# of tweets'])
nd['Zipcode'] = uni
nd['# of tweets']=0
for index,row in nd.iterrows():
    for i in zipc:
        if i==nd.loc[index,'Zipcode']:
            nd.loc[index,'# of tweets']+=1
            print(nd.loc[index,'# of tweets'])
                
nd = nd.sort_values('# of tweets', ascending=False)
nd.to_excel("New Twitter Data.xlsx")
