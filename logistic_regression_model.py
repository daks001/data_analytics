import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import math

data=pd.read_csv('All Hurricanes.csv')
data.head()
print(len(data.index))
sns.countplot(x='Rural/Urban', data=data)
sns.countplot(x='Rural/Urban', hue='socialmedia_reliable', data=data)
data['age_5'].plot.hist(bins=6)
data.info()
data.isnull()
data.isnull().sum()
sns.heatmap(data.isnull(), yticklabels=False)
sns.boxplot(x='socialmedia_reliable', y='Rural/Urban', data=data)
social=pd.get_dummies(data['socialmedia_reliable'], drop_first=True)
social.head()
data=pd.concat([data, social], axis=1)
data.head()
data.drop(['county', 'stat_res', 'zipcode', 'owner_stat', 'owner_stat2', 'home_type', 'home_type2', 'age_1', 'age_2',\
           'age_3', 'age_4', 'age_5', 'male', 'female', 'income', 'race', 'race2', 'education', 'education2', \
           'chronic', 'mobility', 'socialmedia_use', 'socialmedia_platforms', 'socialmedia_platforms2', \
           'socialmedia_info', 'socialmedia_info2', 'socialmedia_info3', 'socialmedia_reliable', \
           'socialmedia_misinfo', 'transp_days', 'transp_days.1', 'transp_info', 'transp_info.1', 'transp_reliable',\
           'transp_hardship', 'elec_days', 'elec_backup', 'elec_info', 'elec_info2', 'elec_reliable','elec_hardship',\
           'wireless_days', 'cell_days', 'internet_needs', 'internet_needs2', 'internet_needs3', 'commun_hardship', \
           'water_days', 'boilwater_days', 'water_info', 'water_info2', 'water_hardship', 'food_days', 'food_runout',\
           'food_info', 'food_info2', 'food_reliability', 'food_hardship', 'chem_expos', 'chem_days', 'chem_info', \
           'chem_info2', 'chem_reliable', 'chem_hardship', 'floodcontrol', 'days_know', 'days_prep', 'prep_shortage',\
           'prep_shortage2', 'disaster_impact', 'wb_helpless', 'wb_upset', 'wb_safety', 'wb_depressed', 'wb_tasks',\
           'wb_distant', 'wb_injury', 'wb_overall', 'infra_cap', 'infra_invest', 'infra_tax', 'infra_trust', \
           'evacuated', 'water_reliability'], axis=1, inplace=True)
data.head()
data.dropna(inplace=True)
data.isnull().sum()
x=data.drop('Rural/Urban', axis=1)
y=data['Rural/Urban']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.3, random_state=1) 
from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
logmodel.fit(x_train, y_train)
predictions=logmodel.predict(x_test)
from sklearn.metrics import classification_report
classification_report(y_test, predictions)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, predictions)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)*100
import statsmodels.api as sm
model = sm.OLS(y,x).fit()
print(model.summary())
