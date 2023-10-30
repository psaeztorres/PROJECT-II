import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from src.helpers import save_and_open
import src.Cleaning_transforming as clean

def REO_price_plot(df):
    df_sorted = df.sort_values(by="average_price", ascending=False)
    REO_prices_plot =sns.barplot(y=df_sorted["average_price"],x=df_sorted["name"], palette="Set2",legend=False, data=df_sorted)
    REO_prices_plot.legend(loc='upper right', bbox_to_anchor=(0.8, 1), title="REO avg_price updated 27.10.2023")
    plt.ylabel("Average Price (USD/mt)")
    REO_prices_plot.set_xticklabels(REO_prices_plot.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.legend(fontsize =5)

    save_and_open("Reo_prices_plot")

def num_proj_cont(df_re):
    category_counts = df_re['Continent'].value_counts().index
    
    sns.countplot(x="Continent", data=df_re, order=category_counts)
    plt.title('nun.porjects / Continent')
    plt.xticks(rotation=45)
    plt.legend(fontsize =5)

    save_and_open("projects_continent")

def exp_reo_plot(df_re):
    q3_2_answer=clean.exp_reo_subset(df_re)
    plt.figure(figsize=(10, 6))

    locations = q3_2_answer['Location']
    mineral1 = q3_2_answer['Terbium_Oxide']
    mineral2 = q3_2_answer['Samarium_Oxide']
    mineral3 = q3_2_answer['Lutetium_oxide']

    top3_plt=plt.bar(locations, mineral1, label='Terbium_Oxide', color='b')
    plt.bar(locations, mineral2, bottom=mineral1, label='Samarium_Oxide', color='m')
    plt.bar(locations, mineral3, bottom=mineral1 + mineral2, label='Lutetium_oxide', color='r')

    plt.xticks(rotation=45)
    plt.xlabel('Location')
    plt.ylabel('Total Quantity of Minerals')
    plt.title('top 3 most expenisve REO in 5 biggest projects')
    plt.legend()
    save_and_open("project_exp_reo_plot")




def exp_reo_plot_fer_for_plot (q3_1_subset):
    
    q3_2_subset = q3_1_subset[['Location','Terbium_Oxide','Samarium_Oxide','Lutetium_oxide']]
    q3_2_subset['most_ex_REO_total'] =q3_2_subset['Lutetium_oxide']+q3_2_subset['Terbium_Oxide']+q3_2_subset['Samarium_Oxide']
    q3_2_answer=q3_2_subset.sort_values(by='most_ex_REO_total', ascending=False).head(5)
    q3_2_answer.loc[145,'Location'] = 'China_2'

    plt.figure(figsize=(10, 6))

    locations = q3_2_answer['Location']
    mineral1 = q3_2_answer['Terbium_Oxide']
    mineral2 = q3_2_answer['Samarium_Oxide']
    mineral3 = q3_2_answer['Lutetium_oxide']

    top3_plt=plt.bar(locations, mineral1, label='Terbium_Oxide', color='b')
    plt.bar(locations, mineral2, bottom=mineral1, label='Samarium_Oxide', color='m')
    plt.bar(locations, mineral3, bottom=mineral1 + mineral2, label='Lutetium_oxide', color='r')

    plt.xticks(rotation=45)
    plt.xlabel('Location')
    plt.ylabel('Total Quantity of Minerals')
    plt.title('top 3 most expenisve REO in 5 biggest projects')
    plt.legend()
    save_and_open("project_exp_reo_plot_fer")
