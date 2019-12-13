import pandas as pd
df = pd.read_excel('New Florence.xlsx')
totres = df['total zipcode population'].sum()
print(totres)
tsmu = df['Total Social Media Users'].sum()
tsmup = (tsmu*100)/totres
print(tsmup)
ttu = df['Twitter'].sum()
ttup = (ttu*100)/totres
print(ttup)
tfu = df['Facebook'].sum()
tfup = (tfu*100)/totres
print(tfup)
tnu = df['Nextdoor'].sum()
tnup = (tnu*100)/totres
print(tnup)
tou = df['Other Apps'].sum()
toup = (tou*100)/totres
print(toup)
tb = df['Race_Black'].sum()
tbp = (tb*100)/totres
print(tbp)
tw = df['Race_White'].sum()
twp = (tw*100)/totres
print(twp)
tl = df['Race_Latino'].sum()
tlp = (tl*100)/totres
print(tlp)
ta = df['Race_Asian'].sum()
tap = (ta*100)/totres
print(tap)
to = df['Race_Minority'].sum()
top = (to*100)/totres
print(top)
tc = df['college_degree'].sum()
tcp = (tc*100)/totres
print(tcp)
ti25 = df['income_<25K'].sum()
ti49 = df['income_25K-49K'].sum()
ti50 = ti25+ti49
ti50p = (ti50*100)/totres
print(ti50p)
ti74 = df['income_50K-74K'].sum()
ti98 = df['income_75K-99K'].sum()
ti99 = ti74+ti98
ti99p = (ti99*100)/totres
print(ti99p)
ti100 = df['income_100K-125K'].sum()
ti125 = df['income_125K+'].sum()
tih = ti100+ti125
tihp = (tih*100)/totres
print(tihp)
thd = df['Health_Disability'].sum()
thdp = (thd*100)/totres
print(thdp)
thc = df['Health_Chronic'].sum()
thcp = (thc*100)/totres
print(thcp)
tfs = df['social_mediainfo: Flooding Status'].sum()
tfsp = (tfs*100)/totrestddh = df['social_mediainfo: damages due to hurricane'].sum()
print(tfsp)
tddhp = (tddh*100)/totres
print(tddhp)
trc = df['social_mediainfo: road conditions'].sum()
trcp = (trc*100)/totres
print(trcp)
twc = df['social_mediainfo: weather forecast & predicted duration'].sum()
twcp = (twc*100)/totres
print(twcp)
tss = df['social_mediainfo: status of services'].sum()
tssp = (tss*100)/totres
print(tssp)
tsm = df['social_mediainfo: supermarket'].sum()
tsmp = (tsm*100)/totres
print(tsmp)
tcff = df['social_mediainfo: checking on friends/family'].sum()
tcffp = (tcff*100)/totres
print(tcffp)
tc = df['Children(age1 & 2)'].sum()
tcp = (tc*100)/totres
print(tcp)
tt = df['Teen(age3)'].sum()
ttp = (tt*100)/totres
print(ttp)
te = df['Elderly(age5)'].sum()
print(te)
print(totres)
tep = (te*100)/totres
print(tep)
