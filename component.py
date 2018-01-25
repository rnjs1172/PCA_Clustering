
import numpy as np
import pandas as pd
ps = pd.read_csv("C:/Users/Kwon/Desktop/PCA/PCA_python/ps_dataframe.csv")
cust_prod = pd.read_csv("C:/Users/Kwon/Desktop/PCA/PCA_python/crosstab.csv")

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


tocluster = pd.DataFrame(ps[[1,0]])
fig = pit.figure(figsize = (8,8))
plt.plot(tocluster[1], tocluster[0], "o", markersize = 2 , color = 'blue', alpha = 0.5, label = 'class1')
plt.xlabel('xvalues')
plt.ylabel('yvalues')
plt.legend()
plt.show()
