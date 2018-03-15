import numpy as np
from PIL import Image
import sys

sys.setrecursionlimit(50000)
img=Image.open('work.jpeg')
arr=np.array(img)
brr=[]
dict={}

# def evaluate(i,j,count):
# 	count+=1
# 	if (count>=26000):
# 		return
# 	# try:
# 	# 	y=str(i)+"-"+str(j)
# 	# 	var=dict[y]
# 	# 	print("here")
# 	# 	return
# 	# except:
# 	# 	print("there",count)
		

# 	a=check(i,j,i+1,j)
# 	b=check(i,j,i,j+1)
# 	c=check(i,j,i-1,j)
# 	d=check(i,j,i,j-1)
# 	# e=check(i,j,i+1,j+1)
# 	# f=check(i,j,i-1,j+1)
# 	# g=check(i,j,i-1,j-1)
# 	# h=check(i,j,i+1,j-1)

# 	if (a==1):
# 		x=str(i+1)+"-"+str(j)
# 		# print(1)
# 		try:
# 			var=dict[x]
			
# 		except:
# 			brr.append([i+1,j])
# 			dict[x]=1
		
# 			evaluate(i+1,j,count)

# 	if (b==1):
# 		# print(2)
# 		x=str(i)+"-"+str(j+1)
# 		try:
# 			var=dict[x]
			
# 		except:
# 			brr.append([i,j+1])
# 			dict[x]=1
# 			evaluate(i,j+1,count)

# 	if (c==1):
# 		# print(3)
# 		x=str(i-1)+"-"+str(j)
# 		try:
# 			var=dict[x]
			
# 		except:
# 			brr.append([i-1,j])
# 			dict[x]=1
# 			evaluate(i-1,j,count)

# 	if (d==1):
# 		# print(4)
# 		x=str(i)+"-"+str(j-1)
# 		try:
# 			var=dict[x]
			
# 		except:
# 			brr.append([i,j-1])
# 			dict[x]=1
# 			evaluate(i,j-1,count)


def check(i,j,a,b):
	if ((arr[i,j,0]-arr[a,b,0])<=50 and (arr[i,j,1]-arr[a,b,1])<=50 and (arr[i,j,2]-arr[a,b,2])<=50):
		return 1
	else:
		return 0

def eval(x,y):

	for i in range (740):
		for j in range (1040):
			if (i-1>=0 and i+1<740 and j-1>=0 and j+1<1040):
				a=check(i,j,i+1,j)
				b=check(i,j,i,j+1)
				c=check(i,j,i-1,j)
				d=check(i,j,i,j-1)
				# e=check(i,j,i+1,j+1)
				# f=check(i,j,i+1,j-1)
				# g=check(i,j,i-1,j+1)
				# h=check(i,j,i-1,j-1)

				if (a==1 and b==1 and c==1 and d==1):
					brr.append([i,j])





i=100
j=100
count=0
brr.append([i,j])
eval(i,j)
print(len(brr))
# print(brr)

for i in brr:
	arr[i[0],i[1],0]=10
	arr[i[0],i[1],1]=10
	arr[i[0],i[1],2]=10

im=Image.fromarray(arr,'RGB')
im.save('yes.jpeg')