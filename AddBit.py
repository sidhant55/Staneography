import numpy as np
from PIL import Image

img=Image.open('yes1.jpeg')
arr=np.array(img)
msg=""

def decrypt(pix):
	print(pix)
	bits=[0,3,3]
	val=0
	for i in range (2,-1,-1):
		if (i==2):
			val+=(pix[i]%4)
		else:
			val+=(pix[i]%8)
		print(val, end=" ")
		if(i!=0):
			val=val<<3
		print(val)
	print(val)

print(arr[0][0][0],arr[0][0][1],arr[0][0][2])
for i in range (780):
	for j in range (1040):
		decrypt(arr[i][j])
		break
	break