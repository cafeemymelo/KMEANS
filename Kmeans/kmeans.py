import numpy as np
import matplotlib.pyplot as plt
import numpy_indexed as npi
import time
import os

class Kmeans:
    """

    """
    def __init__(self):
        #global variables
        self.total_data = 0
        self.x = []
        self.y = []
        self.label = []
        self.centroidx = []
        self.centroidy = []
    def createCluster(self, num_clusters):
        '''
        Create n(num_clusters) clusters using normal distribution.
        :param num_clusters: number of cluster wanted
        :return:
            x:
            y:
            label:
            total_data:
        '''
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

        self.total_data = int(quant.sum())
        self.x = []
        self.y = []
        self.label = []
        for i in xrange(c_data):
            self.x = np.append(self.x, np.random.normal(int(centerx[i]), int(std[i]), int(quant[i])))
            self.y = np.append(self.y, np.random.normal(int(centery[i]), int(std[i]), int(quant[i])))
            for j in xrange(int(quant[i])):
                self.label = np.append(self.label, i)

        return self.x,self.y,self.label,self.total_data

    def ComputeKmeans(self, x, y, label, total_data,num_centroids = None):
        '''
        Cluster a dataset using Kmeans Method
        :param x:
        :param y:
        :param label:
        :param total_data:
        :param num_centroids:
        :return:
        '''
        while (not s):
            try:
                c_test = num_centroids  # number of centroids guessed
                centroidx = []
                centroidy = []
                flag = False
                comp = np.zeros(int(quant.size))
                for i in xrange(c_test):
                    if ((comp.sum() == quant.size) and (i < c_test)):
                        comp = np.zeros(int(quant.size))
                    while (not flag):
                        j = np.random.randint(0, int(quant.size))
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

                    plt.scatter(x_dinamico, y_dinamico, c=new_label_new, cmap='rainbow')
                    plt.scatter(centroidx, centroidy, c='green', marker='8')
                    plt.scatter(centroidupx, centroidupy, c='black')
                    plt.grid(True)
                    plt.show()
                    iter = iter + 1

            except Exception as e:
                print (str(e))
        return 0

    def ComputeElbow(self, num_centroids):
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


        return 0