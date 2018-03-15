import numpy as np
from numpy import array
from PIL import Image


file_data=Image.open('name.png')
file_data=file_data.convert('RGB')
data=np.array(file_data)

print(data[0][0][0])
print(data[0,1,0])
print(data[0,2,0])

for i in range (780):
	for j in range (1040):
		data[i][j][0]=j

print(data[0][0][0])
print(data[0,1,0])
print(data[0,2,0])

im=Image.fromarray(data)
im.save('name1.png')

file_data=Image.open('name1.png')
file_data=file_data.convert('RGB')
data=np.array(file_data)

for j in range (1039):
	if (data[0][j][0]+1==data[0][j+1][0]):
		continue
	else:
		print(data[0][j][0])

