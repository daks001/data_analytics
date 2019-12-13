import pandas as pd
import json
from math import isclose
df = pd.read_csv('uszips.csv')
ndf = pd.DataFrame(columns=['Zipcode','# of tweets', '# of users'])
zips = []
count = 0
j = open('Florence_geo_0913.json','r')
jr = json.load(j)
location = []
for i in jr:
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
    location.append(loc)
print(location)
# data = pd.read_csv('USzip.csv')
# for i in location:
#     for index, row in data.iterrows():
#         if isclose(i[0], data.loc[index,'lat'], abs_tol=1e-1) and isclose(i[1], data.loc[index,'lng'], abs_tol=1e-1):
#             zips.append(data.loc[index,'zip'])
#             print(data.loc[index,'zip'])
#             break
data = pd.read_csv('USzip.csv')
latitude = data['lat']
longitude = data['lng']
zipcode = data['zip']
zips=[]
for i in range(len(latitude)):
    if isclose(latitude[i], data.loc[index,'lat'], abs_tol=1e-1) and isclose(longitude[i], data.loc[index,'lng'], abs_tol=1e-1):
        zips.append(zipcode[i])
# zips
import json
import pandas as pd
from math import isclose
df = pd.read_csv('uszips.csv')
ndf = pd.DataFrame(columns=['Zipcode','# of tweets','Zips'])
zips=[]
tweets=[]
count=0
# print(df['lat'])
with open('Florence_geo_0916.json') as access_json:
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
    
    unique = []
    for index,row in ndf.iterrows():
        for el in unique:
            if row['Zips'] not in unique:
                unique.append(row['Zips'])
#     del unique[0]
    ndf['Zipcode']=unique
    ndf['# of tweets']=0
    
    for index,row in ndf.iterrows():
        for i in zips:
            if i==ndf.loc[index,'Zipcode']:
                ndf.loc[index,'# of tweets']+=1
                print(ndf.loc[index,'# of tweets'])
    ndf = ndf.sort_values('# of tweets', ascending=False)            
    ndf.to_excel("New Twitter6.xlsx")