import numpy as np
import matplotlib.pyplot as plt
import numpy_indexed as npi
import time
import os
def ComputeKmeans(x, y, label, total_data, num_centroids=None):
    """
    Cluster a dataset using Kmeans Method
    :param x:
    :param y:
    :param label:
    :param total_data:
    :param num_centroids:
    :return:
    """
    matrix = np.column_stack((x, y))
    data = np.zeros((total_data, 3))
    data[:, :2] = matrix
    s = False
    while (not s):
        try:
            c_test = num_centroids  # number of centroids guessed
            centroidx = []
            centroidy = []
            flag = False
            centroidupx = np.zeros(c_test)
            centroidupy = np.zeros(c_test)
            comp = np.zeros(int(c_data))
            for i in xrange(c_test):
                if ((comp.sum() == c_data) and (i < c_test)):
                    comp = np.zeros(int(c_data))
                while (not flag):
                    j = np.random.randint(0, int(c_data))
                    if comp[j] == 0:
                        comp[j] = 1
                        flag = True
                centroidx = np.append(centroidx, np.random.normal(centerx[j], np.random.randint(5, 10), 1))
                centroidy = np.append(centroidy, np.random.normal(centery[j], np.random.randint(5, 10), 1))
                flag = False
            centroids = np.column_stack((centroidx, centroidy))
            new_label_new = np.zeros(matrix[:, 0].size)
            new_label_old = np.ones(matrix[:, 0].size)
            dist = np.zeros(centroids[:, 0].size)
            iter = 0
            # looping until no data point were reassingned
            while (iter < 50):
                a = np.zeros((c_test, 1))
                for i in xrange(matrix[:, 0].size):
                    for j in xrange(centroids[:, 0].size):
                        dist[j] = np.sqrt(sum((matrix[i, :] - centroids[j, :]) ** 2))
                    new_label_new[i], = np.where(dist == dist.min())
                if (np.array_equal(new_label_new, new_label_old)):
                    break;
                    s = True
                else:
                    new_label_old = np.copy(new_label_new)
                    unique = np.unique(new_label_new)
                    data[:, 2] = new_label_new
                    for i in xrange(new_label_new.size):
                        for j in xrange(unique.size):
                            if (new_label_old[i] == unique[j]):
                                a[j] = a[j] + 1

                    centroidup = npi.GroupBy(data[:, 2]).sum(data)[1]
                    centroidup = centroidup[:, :2]
                    centroids = centroidup / a
                    centroidupx = centroids[:, 0]
                    centroidupy = centroids[:, 1]
                    s = True

                plt.scatter(x, y, c=new_label_new, cmap='rainbow')
                plt.scatter(centroidx, centroidy, c='green', marker='8')
                plt.scatter(centroidupx, centroidupy, c='black')
                plt.grid(True)
                plt.show()
                iter = iter + 1

        except Exception as e:
            print (str(e))
    return matrix, centroids, data