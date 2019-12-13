import pandas as pd
import re
df = pd.read_csv('Florence.csv')
df['Total social media users'] = 0
df.loc[df['socialmedia_use']=='Yes', 'Total social media users'] = 1
unique = [-1]
c=0
for index,row in df.iterrows():
    for el in unique:
        if row['zipcode'] not in unique:
            unique.append(row['zipcode'])
del unique[0]
ndf=pd.DataFrame(columns=['Zipcode','Total Social Media Users','Facebook','Twitter', \
                          'Instagram','Nextdoor','Other Apps','Race_White','Race_Black', \
                          'Race_Asian','Race_Latino','Race_Other','Race_Minority','income_<25K', \
                          'income_25K-49K','income_50K-74K','income_75K-99K','income_100K-125K', \
                          'income_125K+','college_degree','Children(age1 & 2)','Teen(age3)', \
                          'Elderly(age5)','Health_Disability','Health_Chronic','male','female', \
                          'Median of stat_res', \
                          'social_mediainfo: Flooding Status','social_mediainfo: damages due to hurricane', \
                          'social_mediainfo: road conditions', \
                          'social_mediainfo: weather forecast & predicted duration', \
                          'social_mediainfo: status of services','social_mediainfo: supermarket', \
                          'social_mediainfo: checking on friends/family','total zipcode population', \
                          'Social media users with income<25K', 'Social media users with income 25K-49K', \
                          'Social media users with income 50K-74K', 'Social media users with income 75K-99K', \
                          'Social media users with income 100K-125K', 'Social media users with income 125K+', \
                          'Social media users with college degree', 'Social media users with disability', \
                          'Children who use social media', 'Teens who use social media', \
                          'Elderly people who use social media'])
ndf['Zipcode']=unique
ndf['Total Social Media Users']=0
ndf['Facebook']=0
ndf['Twitter']=0
ndf['Instagram']=0
ndf['Nextdoor']=0
ndf['Other Apps']=0
ndf['Race_Asian']=0
ndf['Race_Latino']=0
ndf['Race_White']=0
ndf['Race_Black']=0
ndf['Race_Other']=0
ndf['Race_Minority']=0
ndf['male']=0
ndf['female']=0
ndf['total zipcode population']=0
ndf['Children(age1 & 2)']=0
ndf['Teen(age3)']=0
ndf['Elderly(age5)']=0
res=[] #to calculate median of stat_res
ndf['income_<25K']=0
ndf['income_25K-49K']=0
ndf['income_50K-74K']=0
ndf['income_75K-99K']=0
ndf['income_100K-125K']=0
ndf['income_125K+']=0
ndf['Health_Disability']=0
ndf['social_mediainfo: Flooding Status']=0
ndf['social_mediainfo: damages due to hurricane']=0
ndf['social_mediainfo: road conditions']=0
ndf['social_mediainfo: weather forecast & predicted duration']=0
ndf['social_mediainfo: status of services']=0
ndf['social_mediainfo: supermarket']=0
ndf['social_mediainfo: checking on friends/family']=0
ndf['college_degree']=0
ndf['Social media users with income<25K']=0 
ndf['Social media users with income 25K-49K']=0 
ndf['Social media users with income 50K-74K']=0 
ndf['Social media users with income 75K-99K']=0 
ndf['Social media users with income 100K-125K']=0 
ndf['Social media users with income 125K+']=0 
ndf['Social media users with college degree']=0 
ndf['Social media users with disability']=0
ndf['Children who use social media']=0
ndf['Teens who use social media']=0
ndf['Elderly people who use social media']=0

for indexn,rowsn in ndf.iterrows():
    for indexd,rowsd in df.iterrows():
        if rowsd['zipcode']==rowsn['Zipcode']:
            ndf.loc[indexn,'Total Social Media Users'] = ndf.loc[indexn,'Total Social Media Users']+ df.loc[indexd,'Total social media users']
            
            res.append(rowsd['stat_res'])
            
            if rowsd['socialmedia_use']=='Yes':
                if rowsd['income']=='Less than $25,000':
                    ndf.loc[indexn,'Social media users with income<25K']+=1
            
                if rowsd['income']=='$25,000 - $49,999':
                    ndf.loc[indexn,'Social media users with income 25K-49K']+=1

                if rowsd['income']=='$50,000 - $74,999':  
                    ndf.loc[indexn,'Social media users with income 50K-74K']+=1

                if rowsd['income']=='$75,000 - $99,999':
                    ndf.loc[indexn,'Social media users with income 75K-99K']+=1

                if rowsd['income']=='$100,000 - $124,999':
                    ndf.loc[indexn,'Social media users with income 100K-125K']+=1

                if rowsd['income']=='$125,000 - $149,999' or rowsd['income']=='More than $150,000':
                    ndf.loc[indexn,'Social media users with income 125K+']+=1
                    
                if (rowsd['education']=='Trade/technical/vocational training' \
                or rowsd['education']=='High school graduate or GED' \
                or rowsd['education']=='Less than high school'):
                    ndf.loc[indexn,'Social media users with college degree']+=0
                else:
                    ndf.loc[indexn,'Social media users with college degree']+=1
                    
                if rowsd['mobility']=='Yes':
                    ndf.loc[indexn,'Social media users with disability']+=1
                
                ndf.loc[indexn,'Children who use social media']+= rowsd['age_1']+rowsd['age_2']
                ndf.loc[indexn,'Teens who use social media']+=rowsd['age_3']
                ndf.loc[indexn,'Elderly people who use social media']+=rowsd['age_4'] + rowsd['age_5']
                
            
            if 'Facebook' in str(rowsd['socialmedia_platforms']):
                ndf.loc[indexn,'Facebook']+=1
            if 'Twitter' in str(rowsd['socialmedia_platforms']):
                ndf.loc[indexn,'Twitter']+=1
            if 'Nextdoor' in str(rowsd['socialmedia_platforms']):
                ndf.loc[indexn,'Nextdoor']+=1
            if 'Instagram' in str(rowsd['socialmedia_platforms']):
                ndf.loc[indexn,'Instagram']+=1
            if 'Other' in str(rowsd['socialmedia_platforms']):
                ndf.loc[indexn,'Other Apps']+=1
#             if rowsd['socialmedia_platforms']!='':
#                 ndf.loc[indexn,'Other Apps']+=1
            
            if (rowsd['race']=='White' or rowsd['race2']=='Just plain American.  Knock off the racial crap.' \
                or rowsd['race2']=='White and Black/African American' or rowsd['race2']=='white & hispanic' \
                or rowsd['race2']=='White, Hispanic and Black' or rowsd['race2']=='Black and White' \
                or rowsd['race2']=='I am White; the other household member is Hispanic.' \
                or rowsd['race2']=='black/american indian/white' or rowsd['race2']=='AMERICAN' \
                or rowsd['race2']=='White and black'):
                ndf.loc[indexn,'Race_White']+=1
            if (rowsd['race']=='Black or African American' or rowsd['race2']=='White, Hispanic and Black' \
                or rowsd['race2']=='Black and White' or rowsd['race2']=='Native American Black' \
                or rowsd['race2']=='black/american indian/white' or rowsd['race2']=='White and black'):
                ndf.loc[indexn,'Race_Black']+=1
            if (rowsd['race']=='Hispanic or Latino' or rowsd['race2']=='White, Hispanic and Black' \
                or rowsd['race2']=='I am White; the other household member is Hispanic.'):
                ndf.loc[indexn,'Race_Latino']+=1
            if rowsd['race']!='':
                ndf.loc[indexn,'Race_Other']+=1
            if rowsd['race2']=='Asian American' or rowsd['race']=='Asian':
                ndf.loc[indexn,'Race_Asian']+=1
                
            if (rowsd['race2']=='Multiracial' or rowsd['race2']=='Californian and New Yorker(City)' \
                or rowsd['race2']=='Spanish American' or rowsd['race2']=='mixed' \
                or rowsd['race2']=='Multi racial' or rowsd['race2']=='refused' \
                or rowsd['race2']=='Dutch, Panamanian and Black' \
                or rowsd['race2']=='Mixed family. Native and Mexican American. ' \
                or rowsd['race2']=='black/american indian/white' or rowsd['race2']=='Hebrew' \
                or rowsd['race2']=='AMERICAN AND JAMAICAN' or rowsd['race2']=='Multi-Racial' \
                or rowsd['race2']=='American Indian/European'):
                ndf.loc[indexn,'Race_Minority']+=1
                
            if (rowsd['education']=='Trade/technical/vocational training' \
                or rowsd['education']=='High school graduate or GED' \
                or rowsd['education']=='Less than high school'):
                ndf.loc[indexn,'college_degree']+=0
            else:
                ndf.loc[indexn,'college_degree']+=1
            
            ndf.loc[indexn,'Children(age1 & 2)']+= rowsd['age_1']+rowsd['age_2']
            ndf.loc[indexn,'Teen(age3)']+=rowsd['age_3']
            ndf.loc[indexn,'Elderly(age5)']+=rowsd['age_4'] + rowsd['age_5']
            
            ndf.loc[indexn,'male']+=rowsd['male']
            ndf.loc[indexn,'female']+=rowsd['female']
            
            if rowsd['chronic']=='Yes':
                ndf.loc[indexn,'Health_Chronic']+=1
            else:
                ndf.loc[indexn,'Health_Chronic']=0
                
            ndf.loc[indexn,'total zipcode population']+=1
            
            if rowsd['income']=='Less than $25,000':
                ndf.loc[indexn,'income_<25K']+=1
            
            if rowsd['income']=='$25,000 - $49,999':
                ndf.loc[indexn,'income_25K-49K']+=1
                
            if rowsd['income']=='$50,000 - $74,999':  
                ndf.loc[indexn,'income_50K-74K']+=1
                
            if rowsd['income']=='$75,000 - $99,999':
                ndf.loc[indexn,'income_75K-99K']+=1
            
            if rowsd['income']=='$100,000 - $124,999':
                ndf.loc[indexn,'income_100K-125K']+=1
                
            if rowsd['income']=='$125,000 - $149,999' or rowsd['income']=='More than $150,000':
                ndf.loc[indexn,'income_125K+']+=1
                
            if rowsd['mobility']=='Yes':
                ndf.loc[indexn,'Health_Disability']+=1
            
            if 'Flooding status' in str(rowsd['socialmedia_nfo']):
                ndf.loc[indexn,'social_mediainfo: Flooding Status']+=1
            
            if 'Damages due to Hurricane Harvey' in str(rowsd['socialmedia_nfo']):
                ndf.loc[indexn,'social_mediainfo: damages due to hurricane']+=1
            
            if 'Road conditions' in str(rowsd['socialmedia_nfo']):
                ndf.loc[indexn,'social_mediainfo: road conditions']+=1
            
            if 'Weather forecast and predicted duration of the Hurricane' in str(rowsd['socialmedia_nfo']):
                ndf.loc[indexn,'social_mediainfo: weather forecast & predicted duration']+=1
            
            if "services" in str(rowsd['socialmedia_nfo']) or "service" in str(rowsd['socialmedia_nfo']) or "facilities" in str(rowsd['socialmedia_nfo']):
                ndf.loc[indexn,'social_mediainfo: status of services']+=1
            
            if 'Supermarket' in str(rowsd['socialmedia_nfo']):
                ndf.loc[indexn,'social_mediainfo: supermarket']+=1
            
            if 'friends' in str(rowsd['socialmedia_nfo2']) or 'friends' in str(rowsd['socialmedia_nfo']) or 'family' in str(rowsd['socialmedia_nfo2']) or 'family' in str(rowsd['socialmedia_nfo']):
                ndf.loc[indexn,'social_mediainfo: checking on friends/family']+=1
            
            
    
    #we have to find median of res
    res.sort() #ascending
    if len(res)%2==0: #even length
        ndf.loc[indexn,'Median of stat_res']= (res[(len(res))//2] + res[((len(res))//2)-1])/2
    else:
        ndf.loc[indexn,'Median of stat_res']= res[(len(res))//2]
    res=[]
    
ndf = ndf.sort_values('Total Social Media Users', ascending=False)
ndf.to_excel('New Florence.xlsx', index=False)