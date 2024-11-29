#kwargs(**)
#it stores in dictionaries

'''def details(**a):
    print(a)
    print(type(a))
details()
d={"idnos":[10,20,30],
   "names":["savi","teja","sruthi"],
   "status":["P","A","P"]}
details(**d)


def Data(**a):
    print(a)
    print(type(a))
Data()
b={"names":["jayachandra","rajendra","rajesh"],
   "places":["vija","hyd","vzg"]}
Data(**b)



def Data(**a):
    print(a)
    print(type(a))
    for i in a.keys():
    #for i in a:
              print(i) #it will return only keys
    #for i in a.values():
       # print(i)
Data()
b={"names":["jayachandra","rajendra","rajesh"],
   "places":["vija","hyd","vzg"]}
Data(**b)
        

def Data(**a):
    print(a)
    print(type(a))
    #for i in a.values():
    for i in a:
        print(a[i]) #only values will return
Data()
b={"names":["jayachandra","rajendra","rajesh"],
   "places":["vija","hyd","vzg"]}
Data(**b)'''



def Data(**a):
    print(a)
    print(type(a))
    for i in a.items():
        print(i)
    #for i in a:
        #print(i,a[i]) #it will returns both keys and values
Data()
b={"names":["jayachandra","rajendra","rajesh"],
   "places":["vija","hyd","vzg"]}
Data(**b)


def final(*a,**b):
    d=2 #creating a variable
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+1
            print(d)
    for i,j in b.items():
        print("key is",i)
        print("values is",j)
final()
data=(2,4,3,5,4.2,5.3,"python",3+8j,True,False)
final(*data)
details={"names":["pooja","bhanu","divya"],
         "places":["vja","hyd","bng"]}
final(**details)
final(*data,**details)      




        
