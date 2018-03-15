import numpy as np
from PIL import Image

img=Image.open('work.jpeg')
arr=np.array(img)

f=open('code.txt','r')
code=f.read()
print(code)
print(type(arr[10,1000,0]))

k=0
for i in range (780):
	for j in range (1040):
		print(arr[i,j,0], end=" "),
	print()


		

# # print(arr[10,1000,0],arr[10,1000,1],arr[10,1000,2])
# # print(arr[50,900,0],arr[50,900,1],arr[50,900,2])
# im=Image.fromarray(arr,'RGB')
# im.save('yes.jpeg')

# img=img.convert('1')
# img.save('BandW.jpeg')
# print(arr.shape)