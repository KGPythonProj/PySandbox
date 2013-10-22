def fib(n):		# produces fib sequence of length n
	if (n == 1) or n == 2:
		return 1
	else:
		return (fib(n-1) + fib(n-2))

def fibseq(n):		#returns fibonacci sequence of length n as list
	seq = []
	for i in range(1,n+1):
		seq.append(fib(i))
	return seq

def fibprint(n):
	seq = fibseq(n)
	for i in range(0,n):
		print "."*seq[i]

def fibrange(a,b):
	seq=[]
	if (b > a) and (type(a) == type(b) == int):
		for i in range(a, b+1):
			seq.append(fib(i))
	else:
		return -1
	return seq
