import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os


def column_names_cosistent(df_re):
    names_dcit={'La2O3':'Lanthanum_Oxide', 'Ce2O3':'Cerium_Oxide','Pr6O11':'Praseodymium_Oxide','Nd2O3':'Neodymium_Oxide',
 'Sm2O3':'Samarium_Oxide', 'Eu2O3':'Europium_Oxide', 'Gd2O3':'Gadolinium_Oxide', 'Tb4O7':'Terbium_Oxide',
 'Dy2O3':'Dysprosium_Oxide', 'Ho2O3': 'Holmium_Oxide', 'Er2O3':'Erbium_Oxide', 'Tm2O3':'Thulium_oxide', 
'Yb2O3':'Ytterbium_oxide', 'Lu2O3':'Lutetium_oxide', 'Y2O3':'Yttrium_Oxide'}
    df_re=df_re.rename(columns = names_dcit)
    df_re.to_csv("data/df_re")
    return df_re

def drop_col(df_re):
    df_re=df_re.drop(columns=[" Status (2022), 1: Exploration/ Define resource; 2: Feasibility/ Pre-feasibility; 3: Construction; 4: Production; S: Suspending mining; T: Test of Metallurgical; D: Development licence; N: Not Use"])
    return df_re

def drop_unn_pricerange(rare_earth_df):
    rare_earth_df['average_price'] = rare_earth_df['average_price'] .str.replace(',', '').astype(float)
    return rare_earth_df

def into_num_1(df):
    df['average_price'] = df['average_price'] .replace(',', '').astype(float)
    return df

def prices_mt(df):
    for index, row in df.iterrows():
        if row['units'] == 'USD/kg':
            df.at[index, 'average_price'] = row['average_price'] * 1000
            df.at[index, 'units'] = 'USD/mt'
    return df