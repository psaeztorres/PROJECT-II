import src.extracting as extracting
import src.Cleaning_transforming as clean
import src.visualization as visualization
import pandas as pd
import os

import warnings
warnings.filterwarnings("ignore")


url = "https://www.metal.com/Rare-Earth-Oxides"


rare_earth_df = extracting.html_extracting (url)
#os.system("data/test.csv")
#print(Rare_earth_df.head())

df_re = extracting.csv_extracting("mining_projects.csv")
#print(df_re.head())

df_re = clean.column_names_cosistent(df_re)
#print(df_re.head())

df_re= clean.drop_col(df_re)

rare_earth_df = clean.drop_unn_pricerange(rare_earth_df)
print("RAAAAAAAAAAARE: ", rare_earth_df.head())

rare_earth_df = clean.into_num_1(rare_earth_df)
print(rare_earth_df)

rare_earth_df= clean.prices_mt(rare_earth_df)
print(rare_earth_df)

visualization.REO_price_plot(rare_earth_df)

visualization.num_proj_cont(df_re)

print("DF_REEEEEE: ", df_re.head())
