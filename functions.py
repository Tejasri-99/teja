#1.
#2.python gives in built functions like print,you can make your own function also and these are called user defined functions
#3.function blocks begin with key word def followed by the function name and paranathesis


#function

'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)

def calculate(a,b):
    print("the divion is",a//b)
    print("the floor division is",a/b)
    print("the power is",a**b)
calculate(2,4)
calculate(10,2)
calculate(10,2)


def add(a,b):
    c=a+b
    print(c)
add(2,6)

while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    cal()


def data():
    fname=input("fname")
    lname=input("lname")
    print((fname+" "+lname).title())
    data()
data()


def div(a,b):
    print( a//b)
div(2,3)'''


#print v/s return
'''def mul(a,b):
    print(a*b)
mul(5,6)

def mul (a,b):
    return a*b
print(mul(4,5))'''


def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)


def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
    #return  c,d,e
print(cal(2,4))

def cal(a,b):
    a=int(input())
    b=int(input())
    
