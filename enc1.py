import numpy as np
from numpy import array

import matplotlib.image as img

image = img.imread('work.jpeg')

f=open('code.txt','r')
code=f.read()

# print(image.flags)
image.setflags(write=1)
# print(image.flags)

print(image[0][0][0])
print(image[0][1][0])
print(image[0][2][0])

for i in range (780):
	for j in range (1040):
		image[i][j][0]=21

print(image[0][0][0])
print(image[0][1][0])
print(image[0][2][0])

print(image.shape)
img.imsave('name.png', image)

image = img.imread('name.png')

print(image[0][0])
print(image[0][1][0])
print(image[0][2][0])
