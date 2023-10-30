import requests
from bs4 import BeautifulSoup 
import pandas as pd
import requests
import re

def html_extracting (url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    ugly_metal = soup.find_all("div", {"class":"row___1xJWs close___30tSe"})
    metal_name = ugly_metal[0].getText()
    name= metal_name.split(")")[0].replace(" (USD/mt","")
    names=[ugly_metal[i].getText().split(")")[0].replace(" (USD/mt","").replace(" (USD/kg","") for i in range(len(ugly_metal))]
    units=[ugly_metal[i].getText().split(")")[0].split("(")[1] for i in range(len(ugly_metal))]
    ugly_prices =ugly_metal[0].find_all("div",{"class":"item___ku9Fy"})
    avg_price=[ugly_metal[i].find_all("div", {"class":"item___ku9Fy"})[1].getText() for i in range(len(ugly_metal))]
    date= [ugly_metal[i].find_all("div", {"class":"item___ku9Fy"})[3].getText() for i in range(len(ugly_metal))]
    range_prices= [ugly_metal[i].find_all("div", {"class":"item___ku9Fy"})[0].getText() for i in range(len(ugly_metal))]
    rare_earth_dic={
    "name": names,
    "units": units,
    "average_price": avg_price,
    "price_range": range_prices,
    "date":date       
    }
    Rare_earth_df = pd.DataFrame(rare_earth_dic)
    Rare_earth_df['name'] = Rare_earth_df['name'].str.replace(' ', '_')
    Rare_earth_df.to_csv("data/Rare_earth_df.csv")
    return Rare_earth_df

def csv_extracting (path):
    df_re = pd.read_csv(path, sep=';')
    df_re.to_csv("data/df_re.csv")
    return df_re
