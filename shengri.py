def foo(n):
	nn = 1
	while n != 1:
		nn+=1
		if n%2 ==0:
			n = n/2
		else:
			n = 3*n+1
	return nn
		
maxn = 0
for i in range(900,1001):
	n = foo(i)
	if n > maxn:
		maxn = n

print maxn