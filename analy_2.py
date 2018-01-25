import numpy as np
import pandas as pd


data_set1 = pd.read_csv("C:/Users/Administrator/Desktop/analy/data_set1.csv")
### pca 변수를 user id 와 aisle id 두개로 설정하고 분석을 시작
###     - pca 분석을 위하여 crosstab 형태로 변경한다.
cust_prod = pd.crosstab(data_set1["user_id"],data_set1["aisle_id"])
cust_prod.to_csv("C:\\Users\\Administrator\\Desktop\\analy\\crosstab.csv")

#### 본격적으로 pca 분석 시작
from sklearn.decomposition import PCA
pca = PCA(n_components = 6) ### 주성분의 수를 몇개로 두느냐도 중요한 변수
##### 내 생각에는 department 수로 나누는 것도 적절하다 생각이 들지만, 너무 복잡해져서 주성분의 의미가 없어진다.
