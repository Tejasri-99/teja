 '''def cal():
    a=int(input())
    b=int(input())
    c=int(input(choose the option
             1.add
             2.sub
             3.multi))
    if c==1:
        print(a+b)
    elif c==2:
            print(a-b)
    elif c==3:
                print(a*b)
    else:
        print("invalid option")
        cal()
cal()


def add():
    s=a+b
    print(s)
def sub():
    s=a-b
    print(s)
def multi():
    s=a*b
    print(s)
while True:
    a=int(input("a value"))
    b=int(input("a value"))
    c=int(input(choose the option
                     1.add
                     2.sub
                     3.multi))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        multi()'''

def cal():
    total=int(input("total no.of friends"))
    amount=int(input("total amount"))
    print("each person",amount//total)
cal()

def cal():
    a=int(input("total no.of friends"))
    b=int(input("total amount"))
    c=b//a
    return c
print(cal())

def splitbill():
    a=int(input("total no.of friends"))
    b=int(input("total amount"))
    print("each person{}".format(b//a))
splitbill()


def splitbill():
    a=int(input("total no.of friends"))
    b=int(input("total amount"))
    #c=b//a
    #print(f"each person{c}")
    print(f"each person{b//a}")
splitbill()


    
