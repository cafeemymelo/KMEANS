import numpy as np
import matplotlib.pyplot as plt
import numpy_indexed as npi
import time
import os
def ComputeElbow(self, num_centroids, matrix, centroids, data):
    """

    :param self:
    :param num_centroids:
    :param matrix:
    :param centroids:
    :param data:
    :return:
    """
    wcss = np.zeros(num_centroids * 2)
    w = 0
    while ((w < ((num_centroids * 2) - 1))):
        try:
            w = w + 1
            wcss_sum = np.zeros((matrix[:, 0].size, 2))
            for i in xrange(matrix[:, 0].size):
                wcss_sum[i] = (np.sqrt(sum((matrix[i, :] - centroids[int(data[i, 2:]), :]) ** 2))) ** 2
            wcss[w] = wcss_sum.sum()
            print w
        except Exception as e:
            w = w - 1
            print (str(e))