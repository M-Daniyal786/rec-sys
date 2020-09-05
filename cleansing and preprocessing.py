    # -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:54:04 2020

@author: bilal
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt


df=pd.read_csv(r'C:/Users/bilal/Desktop/x.csv',encoding = "ISO-8859-1");


names =pd.DataFrame(df['name'].split(',').tolist(),index=df['cuisines'].stack())           
names = names.reset_index([0, 'name'])
names.columns = ['name', 'cuisines']


df.concat([pd.Series(row['var2'], row['var1'].split(','))              
                    for _, row in a.iterrows()]).reset_index()

new=pd.DataFrame



new['Res ID']=
r=df['res_id']
names=df['name']
res_id=

x=df['cuisines']    



df[['cui1','cui2','cui3','cui4','cui5','cui6','cui7','cui8']]=df['cuisines'].str.split(",",expand=True,)

cuisines.rename(columns={'0': 'cui1', '1': 'cui2', '2': 'cui3', '3': 'cui4', '4': 'cui5', '5': 'cui6', '6': 'cui7'})

cuisines.dtypes


df['cui1'],df['cui2'],df['cui3'],df['cui4'],df['cui5'],df['cui6'],df['cui7']=cuisines





# new=pd.DataFrame
# new['Rid']=Rid
# Rid=df['res_id']
# cuisines
# names
# new_df=pd.concat(Rid,cuisines,names)
# x=pd.DataFrame(cuisines)
# y=pd.DataFrame(Rid)
# z=pd.DataFrame(names)

# df_new=pd.concat(x,y,z)


# df.head
# x=df.iloc[df['city_id']==['34']]
# df.iloc[df['city']=='Agra']
# df.head
# x=df[df['name'],df['city'],df['cuisines']]
# x.head


df.to_csv(r"C:\Users\bilal\Desktop\last.csv",index=False, header=True)

