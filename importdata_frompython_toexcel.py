import pandas as pd
d={'id':[333,444,555,89],'name':['raj','priya','momu','shyam'],'age':[33,44,11,65],'city':['noida','delhi','merrut','gzbd']}
df=pd.DataFrame(d)
print(df)
df.to_csv(r"C:\Users\diwak\Desktop\tada.csv") 
