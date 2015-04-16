def superpower(a,b):
	c=0
	r=1
	for c in range(b):
		c=c+1
		r=r*a
	return r

x=int(input("Give me the number: "))
y=int(input("Give me the power: "))
f= superpower(x,y)
print(f)
