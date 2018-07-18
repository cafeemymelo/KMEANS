from kmeans import Kmeans as k
import matplotlib.pyplot as plt
import clusterCreator as cc
import kmeansMethod as km


###################################################################################################
# trecho funcionando

###################################################################################################

x,y,label,total = cc.create_clusters(4)

plt.scatter(x,y, c=label, cmap = 'rainbow')
plt.grid(True)
plt.show()

km.ComputeKmeans(x,y,label,total,num_centroids=4)
#matrix, centroids, data = k.ComputeKmeans(f,x,y,label,total,num_centroids=4)
