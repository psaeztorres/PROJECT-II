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
    df_re.to_csv("data/df_re", index=False)
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

def dps_and_subs (df_re):
    df_re=df_re.dropna(axis=0, how='all')
    q3_df_re = df_re.drop(columns=['Company Name','Project Name','Project No.','Deposit No.'])
    q3_df_re=q3_df_re.dropna(subset=["Resource (*10^4 t, REO, Total)"])
    q3_1_subset=q3_df_re[['Location','Resource (*10^4 t, REO, Total)','Lanthanum_Oxide',
       'Cerium_Oxide', 'Praseodymium_Oxide', 'Neodymium_Oxide',
       'Samarium_Oxide', 'Europium_Oxide', 'Gadolinium_Oxide', 'Terbium_Oxide',
       'Dysprosium_Oxide', 'Holmium_Oxide', 'Erbium_Oxide', 'Thulium_oxide',
       'Ytterbium_oxide', 'Lutetium_oxide', 'Yttrium_Oxide']].sort_values(by='Resource (*10^4 t, REO, Total)', ascending=False).head(10)
    q3_1_subset.to_csv("data/q3_1_subset.csv", index=False)
    #q3_1_subset.loc[112] = q3_1_subset.loc[112].fillna(0)
    q3_1_answer=q3_1_subset[['Location','Lanthanum_Oxide','Cerium_Oxide','Neodymium_Oxide','Resource (*10^4 t, REO, Total)']]
    #q3_1_answer.loc[139,'Location'] = 'China_1'
    #q3_1_answer.loc[145,'Location'] = 'China_2'
    q3_1_answer.to_csv("data/answer_to_question_3.csv", index=False)
    return q3_1_answer


def exp_reo_subset(df_re):
    df_re=df_re.dropna(axis=0, how='all')
    q3_df_re = df_re.drop(columns=['Company Name','Project Name','Project No.','Deposit No.'])
    q3_df_re=q3_df_re.dropna(subset=["Resource (*10^4 t, REO, Total)"])
    q3_1_subset=q3_df_re[['Location','Resource (*10^4 t, REO, Total)','Lanthanum_Oxide',
       'Cerium_Oxide', 'Praseodymium_Oxide', 'Neodymium_Oxide',
       'Samarium_Oxide', 'Europium_Oxide', 'Gadolinium_Oxide', 'Terbium_Oxide',
       'Dysprosium_Oxide', 'Holmium_Oxide', 'Erbium_Oxide', 'Thulium_oxide',
       'Ytterbium_oxide', 'Lutetium_oxide', 'Yttrium_Oxide']].sort_values(by='Resource (*10^4 t, REO, Total)', ascending=False)
    q3_2_subset = q3_1_subset[['Location','Terbium_Oxide','Samarium_Oxide','Lutetium_oxide']]
    q3_2_subset['most_ex_REO_total'] =q3_2_subset['Lutetium_oxide']+q3_2_subset['Terbium_Oxide']+q3_2_subset['Samarium_Oxide']
    q3_2_answer=q3_2_subset.sort_values(by='most_ex_REO_total', ascending=False).head(5)
    q3_2_answer.to_csv("data/project_ex_reo.csv", index=False)
    print("q3_2_answer is: ", q3_2_answer)
    return  q3_2_answer
#######################################################3

def exp_reo_plot_fer_for_subset (df_re):
    df_re=df_re.dropna(axis=0, how='all')
    q3_df_re = df_re.drop(columns=['Company Name','Project Name','Project No.','Deposit No.'])
    q3_df_re=q3_df_re.dropna(subset=["Resource (*10^4 t, REO, Total)"])

    q3_1_subset=q3_df_re[['Location','Resource (*10^4 t, REO, Total)','Lanthanum_Oxide',
       'Cerium_Oxide', 'Praseodymium_Oxide', 'Neodymium_Oxide',
       'Samarium_Oxide', 'Europium_Oxide', 'Gadolinium_Oxide', 'Terbium_Oxide',
       'Dysprosium_Oxide', 'Holmium_Oxide', 'Erbium_Oxide', 'Thulium_oxide',
       'Ytterbium_oxide', 'Lutetium_oxide', 'Yttrium_Oxide']].sort_values(by='Resource (*10^4 t, REO, Total)', ascending=False).head(10)
    try:
        q3_1_subset.loc[112] = q3_1_subset.loc[112].fillna(0)
    except:
        pass
    return q3_1_subset


def exp_reo_fer_for_answer(q3_1_subset):

    q3_1_answer=q3_1_subset[['Location','Lanthanum_Oxide','Cerium_Oxide','Neodymium_Oxide','Resource (*10^4 t, REO, Total)']]
    q3_1_answer.loc[139,'Location'] = 'China_1'
    q3_1_answer.loc[145,'Location'] = 'China_2'

    return q3_1_answer