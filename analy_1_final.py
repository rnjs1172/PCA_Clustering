import numpy as np
import pandas as import pd

orders = pd.read_csv("C:/Users/Administrator/Desktop/analy/orders.csv")
pri_tra_bin = pd.read_csv("C:/Users/Administrator/Desktop/analy/prior_train_rbind.csv")

order_prior = pd.merge(pri_tra_bin,orders,on=["order_id","order_id"])
order_prior = order_prior.sort_values(by =["user_id","order_id"])
order_prior.head()
