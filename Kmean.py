#Python code for k-mean algorithm
number = 1
#function for calculating euclidean distance
def euclidean(p,q,cx,cy):
	temp1=((p-cx)**2+(q-cy)**2) **0.5
	
	return temp1
#function for clustering
def clustering(result1,result2,result3,x,y):
	#centroid of all data points
	allx=3
	ally=3
	data_point = 0
	#initial clusters
	c1=[]
	c2=[]
	c3=[]
	#new clusters
	cenx=[0,0,0]
	ceny=[0,0,0]
	#number for iteration count
	global number
	print "iteration %d"  %(number)
	number = number + 1
	#clustering based on distance of data point from each centroid
	for z in range(8):
		if result1[z]<=result2[z] and result1[z]<=result3[z]:
			#print "cluster1: %d" %(data_point)
			data_point = data_point+1
			c1.append(z)
		elif result2[z]<=result1[z] and result2[z]<=result3[z]:
			#print "cluster2: %d" %(data_point)
			data_point = data_point+1
			c2.append(z)
		else:
			#print "cluster3: %d" %(data_point)
			data_point = data_point+1
			c3.append(z)
	print "cluster1: ",c1
	print "cluster2: ",c2
	print "cluster3: ",c3
	#computing new centroid based on clusters formed
	for k in range(len(c1)):
		cenx[0]=cenx[0]+x[c1[k]]
		ceny[0]=ceny[0]+y[c1[k]]
	
	cenx[0]=float(cenx[0])/float(len(c1))
	
	ceny[0]=float(ceny[0])/float(len(c1))
	k=0
	for k in range(len(c2)):
		cenx[1]=cenx[1]+x[c2[k]]
		ceny[1]=ceny[1]+y[c2[k]]
	
	cenx[1]=float(cenx[1])/float(len(c2))
	ceny[1]=float(ceny[1])/float(len(c2))
	k=0
	for k in range(len(c3)):
		cenx[2]=cenx[2]+x[c3[k]]
		ceny[2]=ceny[2]+y[c3[k]]
	
	cenx[2]=float(cenx[2])/float(len(c3))
	ceny[2]=float(ceny[2])/float(len(c3))
	
	
	wss=0
	bss=0
	m=0
	#calculating wss and bss for each iteration
	
	#wss
	for m in range(len(c1)):
		wss=wss+(euclidean(x[c1[m]],y[c1[m]],cenx[0],ceny[0])) ** 2
	m=0
	for m in range(len(c2)):
		wss=wss+(euclidean(x[c2[m]],y[c2[m]],cenx[1],ceny[1])) ** 2
	m=0
	for m in range(len(c3)):
		wss=wss+(euclidean(x[c3[m]],y[c3[m]],cenx[2],ceny[2])) ** 2

	
	#bss
	bss=bss+len(c1)*((euclidean(allx,ally,cenx[0],ceny[0])) ** 2)
	
	bss=bss+len(c2)*((euclidean(allx,ally,cenx[1],ceny[1])) ** 2)
	
	bss=bss+len(c3)*((euclidean(allx,ally,cenx[2],ceny[2])) ** 2)

	
	print "wss= ", wss
	print "bss= ",bss
	return cenx,ceny
	
#distance lists
result1 = []
result2 = []
result3 = []
#initial centroids
oldcx=[2,3,5]
oldcy=[3,3,4]
#new centroids
newcx=[0,0,0]
newcy=[0,0,0]
test = 0
#while oldcx !=newcx and oldcy!=newcy:
#limiting while loop to avoid infinite loop 
while test<10:
	test = test+1
	iteration=0
	
	x=[1,1,2,2,3,4,5,6]
	y=[1,2,1,3,3,5,4,5]
	#calculating distance from each centroid for clustering
	for i in range(8):
		temp=euclidean(x[i],y[i],oldcx[0],oldcy[0])
		result1.append(temp)
		temp1=euclidean(x[i],y[i],oldcx[1],oldcy[1])
		result2.append(temp1)
		temp2=euclidean(x[i],y[i],oldcx[2],oldcy[2])
		result3.append(temp2)
	
	#computing new centroids
	cenx,ceny=clustering(result1,result2,result3,x,y)
	#flushing result arrays for recomputation
	result1[:]=[]
	result2[:]=[]
	result3[:]=[]
	
	newcx = cenx
	newcy = ceny
	print "new centroid ",newcx[0],newcy[0]
	print "new centroid ",newcx[1],newcy[1]
	print "new centroid ",newcx[2],newcy[2]
	#breaking the loop if we get similar centroid values in consecutive iterations
	if oldcx == newcx and oldcy == newcy:
		break
	#else updating centroid for next iteration
	else:
		oldcx=newcx
		oldcy=newcy
	
	

"""
OUTPUT:
iteration 1
cluster1:  [0, 1, 2, 3]
cluster2:  [4]
cluster3:  [5, 6, 7]
wss=  6.41666666667
bss=  35.5833333333
new centroid  1.5 1.75
new centroid  3.0 3.0
new centroid  5.0 4.66666666667
iteration 2
cluster1:  [0, 1, 2]
cluster2:  [3, 4]
cluster3:  [5, 6, 7]
wss=  4.5
bss=  37.5
new centroid  1.33333333333 1.33333333333
new centroid  2.5 3.0
new centroid  5.0 4.66666666667
iteration 3
cluster1:  [0, 1, 2]
cluster2:  [3, 4]
cluster3:  [5, 6, 7]
wss=  4.5
bss=  37.5
new centroid  1.33333333333 1.33333333333
new centroid  2.5 3.0
new centroid  5.0 4.66666666667
"""

