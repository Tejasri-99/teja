a=["codegnan","python","course"]
b=str(a)
'''print(b.upper())

for i in a:
    print(i)

for i in a:
    print(i.upper(),end=" ")

#syntax list comprehension

#a=[expr for var in collection/range]
b=[i.upper() for i in a]
print(b) 

a=["python","java","ds"]
b=[i.title() for i in a]
print(b)'''


'''a=[1,2,4,6,8,12,13]
b=[i*i for i in a]
print(b)

b=[i**2 for i in a]
print(b)

b=[pow(i,2) for i in a]
print(b)

#if usage in list comprehension

a=[i for i in range(21) if i%2==0]
print(a)

a=[i for i in range(21) if i%2!=0]
print(a)

a=[i*i for i in range(21) if i%2==0]
print(a)

a=["apple","banana","grapes","Kiwi","dragon","blueberry"]
b=[i for i in a if "a" in i]
#b=[i for i in a if "a" not in i]
print(b)


#no-elif usage in list comprehension

a=[i*i if i%2==0 else i*5 for i in range(16)]
print(a)'''


a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range (len(a))]
c=[a[i]+b[i] for i in range(5)]
print(c)






