# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:34:55 2022

@author: sr86671
"""


import pickle
import pandas as pd

# with open(r'C:\Users\sr86671\Documents\01_Data_scraping\saved_variables\pkw_df_all.pkl', 'wb') as f:
#     pickle.dump(df_final, f)

with open(r'C:\Users\sr86671\Documents\01_Data_scraping\saved_variables\pkw_df_all.pkl', 'rb') as f:
    a = pickle.load(f)


a.to_excel(r"C:\Users\sr86671\Documents\01_Data_scraping\01_pkw_teile_scraping\pkw_scrape.xlsx", index=False)
