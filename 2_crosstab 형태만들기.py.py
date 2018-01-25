import numpy as np
import pandas as pd


data_set1 = pd.read_csv("C:/Users/Administrator/Desktop/analy/data_set1.csv")

cust_prod = pd.crosstab(data_set1["user_id"],data_set1["aisle_id"])
cust_prod.to_csv("C:\\Users\\Administrator\\Desktop\\analy\\crosstab.csv")
