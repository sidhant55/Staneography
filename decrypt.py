import numpy as np
from numpy import array
from PIL import Image


file_data=Image.open('Images/encrypt.png')
file_data=file_data.convert('RGB')
data=np.array(file_data)


f=open('code.txt','r')
code=f.read()
k=len(code)

def decrypt(px):
	sum=0
	bit=[8,8,4]
	shft=[0,3,6]
	for i in range (3):
		a=px[i]%bit[i]
		sum+=a<<shft[i]
	return sum


ans=""
for i in range (740):
	for j in range (1040):
		if (j==k):
			flag=1
			break
		ans+=chr(decrypt(data[i][j]))
	if (flag==1):
		break

print(ans)