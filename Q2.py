def triangulo(size):
	c=1
	c2=0
	while(c<=size):
		t="T"
		t=t*c
		print(t)
		c=c+1
		c2=c2+1
	if(c2==size):
		c2=x
		c1=0
		for c1 in range(size):
			t="T"
			c1=c1+1
			t=t*c2
			c2=c2-1
			print(t)

x=int(input("Give me the size: "))
r= triangulo(x)
