import requests
import os
import pandas as pd

excel_path="./Airport_Data.xlsx"

if not os.path.isfile(excel_path):
    r=requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/analysing-spreadsheet-data-with-python/Airport_Data.xlsx")
    f=open(excel_path,"wb+")
    f.write((r.content))
    f.close()

df_facilities=pd.read_excel(excel_path, sheet_name="Facilities")
#print(df_facilities)

## 1 What are the types for aviation facilities in Alaska?
print(df_facilities["Type"].unique())

## 2 Provide a table containing the information for all Seaplane Bases in Alaska
filter=df_facilities["Type"]=="SEAPLANE BASE"
print(df_facilities[filter])

## 3 What are the 5 highest aviation facilities in Alaska?
print(df_facilities.sort_values(by="ARPElevation", ascending=False).head(5))

## 4 What is the average elevation of aviation facilities?
print(f'Mean: {df_facilities["ARPElevation"].mean()}')

## 5 What are the highest and lowest elevation values of the aviation facilities?
print(f'Highest elevation: {df_facilities["ARPElevation"].max()}')
print(f'Lowest elevation: {df_facilities["ARPElevation"].min()}')

## 6 Write to xlsx Files!
df_seaplane=df_facilities[filter]
df_seaplane.to_excel("./seaplane.xlsx")