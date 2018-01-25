import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
cust_prod = pd.read_csv("C:/Users/Kwon/Desktop/PCA/PCA_python/crosstab.csv")

del cust_prod["24"]
del cust_prod["83"]
del cust_prod["120"]
del cust_prod["123"]



from sklearn.decomposition import PCA
pca = PCA(n_components = 6)
pca.fit(cust_prod)
pca_samples = pca.transform(cust_prod)
ps = pd.DataFrame(pca_samples)
tocluster = pd.DataFrame(ps[[5, 4]])
###### tocluster 로 dendrogram 그리기
####tocluster 을 linkage or distance matrix 로 변경!!
from scipy.cluster.hierarchy import dendrogram, linkage

tocluster_4 = tocluster[4].tolist()
tocluster_5 = tocluster[5].tolist()
array_1 = np.array([complex(tocluster_4,tocluster_5)])
##### anaconda prompt 에서 "pip install plotly" 명령어 입력!!! 해서 깔기



import plotly.plotly as py
import plotly.figure_factory as ff

dendro = ff.create_dendrogram(tocluster)
dendro['layout'].update({'width':800, 'height':500})
py.iplot(dendro, filename='simple_dendrogram')
