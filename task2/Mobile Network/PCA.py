import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

# data: Input data with [N, D]
# n_dim: dimensions after reduction
def pca(data, n_dim) :
    N, D = np.shape(data)
    # decentralization
    data = data - np.mean(data, axis = 0, keepdims = True)
    # comptuing covariance matrix
    C = np.dot (data.T, data)/(N-1) #[D, D]

    #computing eigenvaules and eigenvectors
    eig_values, eig_vector = np.linalg.eig(C)
    # extract n_dim largest eigenvalues
    indexs_ = np.argsort(-eig_values) [:n_dim]
    # bulding transformation matrix for dimension reduction
    picked_eig_vector = eig_vector[:, indexs_]
    #data dimension reduction
    data_ndim = np.dot(data, picked_eig_vector)
    return data_ndim, picked_eig_vector

#绘图函数
def draw_pic(data, labs):
    plt.cla()
    unque_labs = np.unique(labs)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unque_labs))]
    p=[]
    legends =[]
    for i in range(len(unque_labs)):
        index = np.where(labs==unque_labs[i])
        pi = plt.scatter(data[index,0], data[index, 1], c=colors[i])
        p.append(pi)
        legends.append(unque_labs[i])

        plt.legend(p, legends)
        plt.show()

    #加载数据
    #data = np.loadtxt()
    #labs =
    #data_ndim, picked_eig_vector = pca(data, n_dim)
    #draw_pic(data_ndim, labs)
    #print(picked_eig_vector)
