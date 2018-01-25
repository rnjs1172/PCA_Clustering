import numpy as np
import pandas as  pd

##### cf) pandas 이상없이 설치 되어 있다. (기본 모튤인듯)


#1. 파일 읽기(pandas 내장함수 이용)
orders = pd.read_csv("C:/Users/Kwon/Desktop/PCA/PCA_python/orders.csv")
prior = pd.read_csv("C:/Users/Kwon/Desktop/PCA/PCA_python/order_products__prior.csv")
train = pd.read_csv("C:/Users/Kwon/Desktop/PCA/PCA_python/order_products__train.csv")

## **오류 때문에 일단 prior 만으로 돌린다. r로 읽는거 자체가 불가능함
#1_2. 합치기
order_prior = pd.merge(prior,orders,on=['order_id','order_id'])#== orders.csv 와 prior.csv 합치기
order_prior = order_prior.sort
