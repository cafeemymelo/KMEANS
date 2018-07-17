from kmeans import Kmeans as k
import matplotlib.pyplot as plt


###################################################################################################
# trecho funcionando

###################################################################################################
f = k()
x,y,label,total = k.createCluster(f,4)
plt.scatter(x,y, c=label, cmap = 'rainbow')
plt.grid(True)
plt.show()

#matrix, centroids, data = k.ComputeKmeans(f,x,y,label,total,num_centroids=4)
