import src.extracting as extracting
import src.Cleaning_transforming as clean
import src.visualization as visualization
import pandas as pd
import os

import warnings
warnings.filterwarnings("ignore")
url = "https://www.metal.com/Rare-Earth-Oxides"
rare_earth_df = extracting.html_extracting (url)
df_re = extracting.csv_extracting("mining_projects.csv")
df_re = clean.column_names_cosistent(df_re)
df_re= clean.drop_col(df_re)
rare_earth_df = clean.drop_unn_pricerange(rare_earth_df)
rare_earth_df = clean.into_num_1(rare_earth_df)
rare_earth_df= clean.prices_mt(rare_earth_df)
visualization.REO_price_plot(rare_earth_df)
visualization.num_proj_cont(df_re)


#clean.dps_and_subs (df_re) 
#visualization.exp_reo_plot(df_re)


q3_1_subset = clean.exp_reo_plot_fer_for_subset(df_re)
q3_1_answer = clean.exp_reo_fer_for_answer(q3_1_subset)
visualization.exp_reo_plot_fer_for_plot (q3_1_subset)
