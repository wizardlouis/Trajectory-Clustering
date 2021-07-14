import numpy as np
data = np.load(r'C:\Users\86188\Desktop\寒假新冠本研\1\git\Trajectory-Clustering\2dmatrix.npy')
print(data.shape)
print(data[:,0])
print(type(data[:,0]))
a=data.tolist()
head = [i[0] for i in a]
nn=0
for i in head:
    if i==1.0:
        nn+=1
print(nn)
print(51+67+15+19)
#51 67 15 19