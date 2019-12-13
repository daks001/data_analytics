import pandas as pd
df = pd.read_excel('michael.xlsx')
count=0
for index,row in df.iterrows():
    if df.loc[index,'mobility']=='Yes':
        count+=1
print count
print df['mobility'].count
print 9400/705