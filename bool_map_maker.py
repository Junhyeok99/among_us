import sys
import numpy as np
sys.stdout = open('map.data','w')

array=np.zeros((1000,1000))
for i in range(200):
    for j in range(200):
        array[100+i][100+j]=1
        array[500+i][100+j]=1
        array[100+i][500+j]=1
        array[500+i][500+j]=1
for i in range(200):
    for j in range(40):
        array[300+i][180+j]=1
        array[300+i][580+j]=1
        array[180+j][300+i]=1
        array[580+j][300+i]=1

for i in range(1000):
    for j in range(1000):
        print(str(int(array[i][j]))+" ")
