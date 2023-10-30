import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from src.helpers import save_and_open


def REO_price_plot(df):
    df_sorted = df.sort_values(by="average_price", ascending=False)
    REO_prices_plot =sns.barplot(y=df_sorted["average_price"],x=df_sorted["name"], palette="Set2",legend=False, data=df_sorted)
    REO_prices_plot.legend(loc='upper right', bbox_to_anchor=(0.8, 1), title="REO avg_price updated 27.10.2023")
    plt.ylabel("Average Price (USD/mt)")
    REO_prices_plot.set_xticklabels(REO_prices_plot.get_xticklabels(), rotation=45, horizontalalignment='right');
    #REO_prices_plot.figure.savefig(name1, dpi=1000)
    plt.legend(fontsize =5)

    save_and_open("Reo_prices_plot")

def num_proj_cont(df_re):
    category_counts = df_re['Continent'].value_counts().index
    
    sns.countplot(x="Continent", data=df_re, order=category_counts)
    plt.title('nun.porjects / Continent')
    plt.xticks(rotation=45)
    plt.legend(fontsize =5)

    save_and_open("projects_continent")


