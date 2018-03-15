import numpy as np
from PIL import Image

img=Image.open('work.jpeg')
ar=np.array(img)
arr=list(ar)

f=open('code.txt','r')
code=f.read()


def encrypt(pixel,ch):
	px=[0,0,0]
	su=[]

	gap=[8,8,4]
	asc=ord(ch)
	for i in range (3):
		su.append(asc%gap[i])
		asc=asc>>3

	for i in range (3):
		if (i!=2):
			px[i]=pixel[i]>>3
			px[i]=(px[i]<<3)+su[i];
		else:
			px[i]=pixel[i]>>2
			px[i]=(px[i]<<2)+su[i];
	return(px)


k=-1
flag=0

for i in range (780):
	for j in range (1040):
		# print(j,arr[i][j],end=" ")
		k+=1;
		if (k==len(code)):
			flag=1
			break
		px=encrypt(arr[i][j],code[k])

		arr[i][j][0]=px[0]
		arr[i][j][1]=px[1]
		arr[i][j][2]=px[2]

		# print(px,arr[i][j])
	if (flag==1):
		break

for i in range (20):
	print(arr[0][i][0],arr[0][i][1],arr[0][i][2])

im=Image.fromarray(arr)
im.save('yes1.jpeg')
print()
img=Image.open('yes1.jpeg')
print("fff")
brr=np.array(img)
for i in range (20):
	print(brr[0][i][0],brr[0][i][1],brr[0][i][2])
print(brr[2][2])