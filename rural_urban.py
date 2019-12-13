import pandas as pd
df=pd.read_csv('All_hurricanes_SM.csv')
df.head()
df['Rural/Urban']=None
df.head()
#rural and urban counties of Georgia
rural_g=['Walker', 'Chattoga', 'Gordon', 'Bartow', 'Murray', 'Polk', 'Haraison', \
         'Carroll', 'Heard', 'Coweta', 'Troup', 'Meriwether', 'Talbot', 'Taylor', \
         'Upson', 'Lamar', 'Monroe', 'Butts', 'Jasper', 'Crawford', 'Peach', 'Houston', \
         'Macon', 'Schley', 'Marion', 'Webster', 'Stewart', 'Randolph', 'Quitman', \
         'Terrell', 'Clay', 'Early', 'Miller', 'Seminole', 'Decatur', 'Grady', 'Calhoun', \
         'Baker', 'Mitchell', 'Thomas', 'Brooks', 'Colquitt', 'Worth', 'Cook', \
         'Tift', 'Lanier', 'Berrien', 'Turner', 'Irwin', 'Atkinson', 'Clinch', \
         'Coffee', 'Ben Hi II', 'Wilcox', 'Crisp', 'Ware', 'Charlton', 'Camden', \
         'Camcen', 'Brantley', 'Pierce', 'Bacon', 'Wayne', 'McIntosh', 'Appling', \
         'Jeff Davis', 'Tel fair', 'Sumter', 'Dooly', 'Pulaski', 'Bleckley', 'Dodge', \
         'Wheeler', 'Laurens', 'Wilkinson', 'Baldwin', 'Putnam', 'Hancock', 'Washington', \
         'Johnson', 'Treutlen', 'Montgomery', 'Toombs', 'Tattnall', 'Evans', 'Bryan', \
         'Bulloch', 'Candler', 'Emanuel', 'Screven', 'Jenkins', 'Burke', 'Jefferson', \
         'Glascock', 'Warren', 'McDuffie', 'Taliaferro', 'Wilkes', 'Lincoln', 'Greene', \
         'Morgan', 'Walton', 'Jackson', 'Elbert', 'Hart', 'Franklin', 'Stephens', 'Banks', \
         'Habersham', 'White', 'Lumpkin', 'Union', 'Dawson', 'Pickens', 'Rabun', 'Towns', \
         'Gilmer', 'Fannin']
urban_g=['Dade', 'Catoosa', 'Whitfield', 'Floyd', 'Cherokee', 'Forsyth', 'Hall', 'Gwinnett', \
         'Barrow', 'Clarke', 'Madison', 'Oglethorpe', 'Oconee', 'Newton', 'Rockdale', 'DeKalb', \
         'Henry', 'Spalding', 'Pike', 'Fayette', 'Fulton', 'Cobb', 'Douglas', 'Paulding', 'Harris', \
         'Muscogee', 'Chattahoochee', 'Lee', 'Dougherty', 'Lowndes', 'Echols', 'Glynn', 'Long', \
         'Liberty', 'Chatham', 'Effingham', 'Richmond', 'Columbia']
#rural and urban counties of North Carolina
rural_nc=['cherokee', 'clay', 'graham', 'dwain', 'yancey', 'alleghany', 'warren', 'greene', 'jones', 'pamlico', \
       'hyde', 'gates', 'tyrrell', 'pasquotank', 'macon', 'jackson', 'transylvania', 'haywood', 'madison', 'polk' \
       'rutherford', 'cleveland', 'mcdowell', 'lincoln', 'mitchell', 'avery', 'watauga', 'ashe', 'wilkes', \
       'alexander', 'surry', 'yadkin', 'davie', 'stokes', 'rockingham', 'caswell', 'person', 'granville', 'vance', \
       'franklin', 'anson', 'stanly', 'montgomery', 'moore', 'randolph', 'chatham', 'harnett', 'johnston', \
       'sampson', 'duplin', 'pender', 'bladen', 'robeson', 'columbus', 'halifax', 'northampton', 'hertford', \
       'bertie', 'martin', 'beaufort', 'chowan', 'washington', 'currituck']
urban_nc=['henderson', 'buncombe', 'burke', 'caldwell', 'catawba', 'gaston', 'iredell', 'mecklenburg', 'union', \
       'rowan', 'cabarrus', 'davidson', 'forsyth', 'guilford', 'alamance', 'orange', 'durham', 'wake', 'lee', \
       'richmond', 'scotland', 'hoke', 'cumberland', 'brunswick', 'newHanover', 'onslow', 'carteret', 'dare', \
       'camden', 'nash', 'edgecomb', 'wilson', 'pitt', 'wayne', 'lenoir', 'craven']
#rural and urban counties of Florida
rural_f=['Monroe', 'Hendry', 'Glades', 'Highlands', 'Okeechobee', 'Hardee', 'DeSoto', \
         'Sumter', 'Citrus', 'Levy', 'Dixie', 'Lafayette', 'Taylor', 'Madison', 'Hamilton', \
         'Suwannee', 'Columbia', 'Union', 'Bradford', 'Putnam', 'Flagler', 'Franklin', 'Gulf', \
         'Liberty', 'Calhoun', 'Washington', 'Jackson', 'Holmes', 'Walton']
urban_f=['Santa Rosa', 'Es cambia', 'Okaloosa', 'Bay', 'Gadsden', 'Leon', 'Wakulla', \
         'Jefferson', 'Baker', 'Clay', 'Duval', 'Nassau', 'St. Johns', 'Gilchrist', \
         'Alachua', 'Marion', 'Lake', 'Volusia', 'Seminole', 'Orange', 'Osceola', \
         'Brevard', 'Indian River', 'Polk', 'Hernando', 'Pasco', 'Hillsborough', \
         'Pinellas', 'Manatee', 'Sarasota', 'Charlotte', 'Lee', 'Collier', 'Broward', \
         'Palm Beach', 'Martin', 'St. Luice', 'Miami-Dade']
for index,row in df.iterrows():
    if row['stat_res']=='Georgia' and row['county'] in rural_g:
        df.loc[index,'Rural/Urban']=0
    if row['stat_res']=='Georgia' and row['county'] in urban_g:
        df.loc[index,'Rural/Urban']=1
    if row['stat_res']=='Florida' and row['county'] in rural_f:
        df.loc[index,'Rural/Urban']=0
    if row['stat_res']=='Florida' and row['county'] in urban_f:
        df.loc[index,'Rural/Urban']=1
    if row['stat_res']=='NC' and row['county'] in rural_nc:
        df.loc[index,'Rural/Urban']=0
    if row['stat_res']=='NC' and row['county'] in urban_nc:
        df.loc[index,'Rural/Urban']=1
df.head()
df.to_csv('All Hurricanes.csv', index=False)