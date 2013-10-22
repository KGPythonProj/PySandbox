#buckets

a=7
b=11
goal=8
stepnum=0
#operations:
def AtoB(a,b):
	return [0,a+b]
def BtoA(a,b):
	return [a+b,0]
def fillA(a,b,n):
	return [n,b]
def fillB(a,b,n):
	return [a,n]
def emptyA(a,b):
	return [0,b]
def emptyB(a,b):
	return [a,0]

def poplist(lst):		#takes in list of x,y pairs, for each pairappend to 
	nlst=[]
	for i in range(0,len(lst)):
		nlst.append(AtoB(lst[i]))
		nlst.append(BtoA(lst[i]))
		nlst.append(fillA(lst[i]))
		nlst.append(fillB(lst[i]))
		nlst.append(emptyA(lst[i]))
		nlst.append(emptyB(lst[i]))
	return nlst

def test(buckets,goal):
	if buckets[0] == goal or buckets[1]== goal:
		return True

def bucketfill(a,b,goal):
	stepnum=0
	lst=[a,b]
	if goal in lst:
		return "poof"
	while test(lst,goal) == False or stepnum > 100:
		lst=poplist(lst)
		stepnum+=1
	print stepnum


"""
create list of possibilities (iterate over "moves", create new list)
check each possibility with "test"
"""
