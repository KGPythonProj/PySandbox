#findprimes between a and b

"""
definition of prime: evenly divisible only by itself and 1
so we must be able to iterate over all numbers between 0 and n/2 (odds only) without finding one that divides into n evenly (n mod i > 0)
"""

def is_prime(n):			# returns True if integer is prime, False otherwise.
	if type(n)!=int:		# check for integer
		print "enter an int"
		return None
	if n%2 == 0:			# if n is even, don't even try
		return False
	max = int(n/2.0)+1		# numbers larger than n/2, +1 for end range index
	for i in range(3,max,2):	# begin at 3, increment by 2 until we check value of max
		if n%i == 0:	
			return False	# return False if ANY even divisors found (returning a value ceases this function)
	return True			# return True otherwise

def primes_between(a,b): 		#takes any posints, a and b, and returns list of primes between, inclusive.
	#validation:
	if not( 0 < a < b and type(a+b) == int ):
		return []
	hitlist=[]
	if a%2 == 0: 			#if a is even, start looking at (a + 1)
		a+=1
	if b%2 == 1: 			#if b is odd, put upper range index at b + 1 so we will check at b
		b+=1
	for i in range(a,b,2): 		#range from a (or a+1, whichever is ODD) to b (or b+1)
		if is_prime(i):
			hitlist.append(i)
	return hitlist

def printprimes():		# visual representation of prime numbers. Takes integer n, prints a "o" when prime found
	print "|",
	for i in range(1,101):
		if (i>1) and (i-1)%10==0:
			print "|\n|",
		if is_prime(i):
			print "o",
		else:
			print " ",
	print "|\n"
def printnum():			# visual representation of prime numbers. Takes integer a, prints a "o" when prime found
	for i in range(1,101):
		if (i-1)%10==0:
			print "\n"
		if is_prime(i):
			print i,
		else:
			print "x",

def printprimesquare(n):	# visual representation of prime numbers. Takes integer n, prints a "o" when prime found
	print "|",
	for i in range(1,n**2+1):
		if (i>1) and (i-1)%n==0:
			print "|\n|",
		if is_prime(i):
			print "o",
		else:
			print ".",
	print "|\n"

def primerect(x,y):
	primelist=[]
	for i in range(1,x*y+1):					#list of bools of primeness. (better to store every bool or just list of primes (int)?)
		primelist.append(is_prime(i))
	print "|",
	for i in range(1,x*y+1):
		if (i>1) and (i-1)%x == 0:
			print "|\n|",
		if primelist[i-1]:
			print "q",
		else: 
			print "p",
	print "|\n"
	



