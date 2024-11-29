#global and local variable
#A variable inside and tha side the function is called global and local variable
#a variable is defined above the function and is accessable to the entire global space is called a global variable
# a variable is inside the function is called  local variable

#first case of global variable
'''a=4
def check():
    print("inside the value is",a)
check()
print("outside the value is",a)


#second case of global variable

a=2
def check2():
    a=5 #creating a  variable
    a=a**2
    print("inside value is",a)
check2()
print("outside the value is",a)


#third case of bkoth global aand local variables
a=3
b=4
def check3():
    a=6
    print("inside the value",a)
    a=10
    print("updated value is",a)
    b=12
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",a)


#usage of global keyword
when user wants to access the global variable
inside the functiondirectly and carry forward the
updated value even outside the function then we need to use global keyword

a=4
b=5
def final():
    global a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
    #global b
    b=13 #local variable
    b=b+a
    print("b value is",b)
final()
print("a value is", a)
print("b value is",b)


#max(),min(),sum()

print(max(3,6,8,9,1,2,4,5))

print(min(3,6,8,9,1,2,4,5))

num=3,6,8,9,1,2,4,5
print(sum(num))

print(sum([3,6,8,9,1,2,4,5]))'''

a=(1,2,3)
b=(4,5,6)
print(sum(a+b))

a=(1,2,3)
b=(4,5,6) #concatenation
print(a+b)

