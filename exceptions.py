# Name error
a=10
b=7
try:
    print("Div",a+c)
except:
    print("Your program has thrown an Name Error Pls check variables ")



#Overflow error 
k = 256
try:
    (4./(8.*k+1.) - 2./(8.*k+4.) - 1./(8.*k+5.) - 1./(8.*k+6.)) / 16.**k
except:
    print("This is an Overflow error")    
#Type Error
a='2'
b=2
try:
    print("a+b",a+b)
except:
    print("This is an type error because we cant add string and int values")    
#Zerodivison error
a=10
b=0
try:
    print(a/b)
except:
    print("This is Zero divison error because we cant div zero with any number ")    

#syntax error
amount = 10000
try:
    if(amount > 2999)
    print("You are eligible to purchase gold")
except:
    print("This is syntax error")

#UnboundLocalError
x = 10
try:
    def bar():
        print(x)
        x=x+1
    bar()

except:
    print("this is UnboundLocalError:")

# value error
try:
    num=int("string")
    print(num)
except:
    print("This is an value error")