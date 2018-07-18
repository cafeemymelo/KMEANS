import numpy as np
import matplotlib.pyplot as plt
import numpy_indexed as npi
import time
import os
def create_clusters(num_clusters):
    """
    Create n(num_clusters) clusters using normal distribution.
    :param num_clusters: number of cluster wanted
    :return:
        x:
        y:
        label:
        total_data:
    """
    c_data = num_clusters  # number  of centroids of the generated data
    quant = np.zeros(c_data)  # quantity of datapoints in each cluster
    centerx = np.zeros(c_data)  # mean of the normal distribuition of the cluster
    # center of the cluster
    centery = np.zeros(c_data)  # mean of the normal distribuition of the cluster
    # center of the cluster
    std = np.zeros(c_data)  # standard deviation of the cluster
    for i in xrange(c_data):
        quant[i] = np.random.randint(10, 40)
        centerx[i] = np.random.randint(10, 60)
        centery[i] = np.random.randint(10, 60)
        std[i] = np.random.randint(1, 5)

    total_data = int(quant.sum())
    x = []
    y = []
    label = []
    for i in xrange(c_data):
        x = np.append(x, np.random.normal(int(centerx[i]), int(std[i]), int(quant[i])))
        y = np.append(y, np.random.normal(int(centery[i]), int(std[i]), int(quant[i])))
        for j in xrange(int(quant[i])):
            label = np.append(label, i)

    return x, y, label, total_data