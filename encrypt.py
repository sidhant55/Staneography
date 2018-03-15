import numpy as np
from numpy import array
from PIL import Image


file_data=Image.open('Images/work.png')
file_data=file_data.convert('RGB')
data=np.array(file_data)

f=open('code.txt','r')
code=f.read()


def find_bits(ch):
	bits=[]
	asc=ord(ch)
	temp=asc
	for i in range(3):
		bits.append(asc%8)
		asc=asc//8
	# print(bits, end=" ")
	return(bits)


def add_bits(px,bits):
	gap=[3,3,2]
	ans=[]
	for i in range(3):
		val=((px[i]>>gap[i])<<gap[i])+bits[i]
		ans.append(val)
	return ans

def encry(px,ch):

	bits=find_bits(ch)
	bits=add_bits(px,bits)
	return bits


k=0
for i in range (740):
	for j in range (1040):
		if (k==len(code)):
			flag=1
			break
		# print(data[i][j], end=" ")
		data[i][j]=encry(data[i][j],code[k])
		# print(data[i][j])
		k+=1
	if (flag==1):
		break;

im=Image.fromarray(data)
im.save('Images/encrypt.png')


# file_data=Image.open('encrypt.png')
# file_data=file_data.convert('RGB')
# data=np.array(file_data)

# k=0
# for i in range (740):
# 	for j in range (1040):
# 		if (k==len(code)):
# 			flag=1
# 			break
# 		print(data[i][j])
# 		k+=1
# 	if (flag==1):
# 		break;