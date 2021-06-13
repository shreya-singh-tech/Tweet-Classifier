import pandas as pd
from sys import argv

script,csv_file,file_name=argv

df = pd.read_csv(csv_file,usecols=["text"])
saved_cols=df.text
#write contents into file
f=open(file_name,'w+')
for i in saved_cols:
	f.write(i)

