def fibonacci(n):
	if(n==0 or n==1):
		return n
	if(n>1):
		return fibonacci(n-2)+fibonacci(n-1)

x=int(input("Give me the position: "))
r= fibonacci(x)
print(r)
