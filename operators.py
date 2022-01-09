#arithmatic operators
x,y,z=5,10,20
print("\n 5+10",x+y)
print("\n 10-20",y-z)
print("\n 5*20",x*z)
print("\n 10/20",y/z)

#comparision operators
print("\n x>y",x>y)
print("\n x<y",x<y)
print("\n x==y",x==y)
print("\n x!=y",x!=y)


#logical operators
a=True
b=False
print("\n a and b is", a and b)
print("not b is",not b)


#membership opeators
g="hello"
k={1:'a',2: 'b'}
print("hello" in g)
print('h' not in g)
print(1 in k)
print('a' in k)


#assignment operators
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c)

c *= a
print ("Line 3 - Value of c is ", c)

c /= a 
print ("Line 4 - Value of c is ", c)


#identity operators
x = 20
y = 20
if ( x is y ): 
	print("x & y  SAME identity")
y=30
if ( x is not y ):
	print("x & y have DIFFERENT identity")