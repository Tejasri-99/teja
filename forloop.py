#for loop

'''a=[10,20,30,40,50]
 for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")
    print(type(a))
    print(type(i))'''

'''a=(4,5,6,7,8,9,10)
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={3,7,9,11,15}
for i in a:
    print(i)
    print(type(a))'''

'''a={"name":"teja","place":"vij"}
for i in a:
    print(i)
    print(type(a))'''

'''a={"name":"teja","place":"vij"}
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
    print(type(a))'''

'''fruits=["mango","apple","kiwi","banana"]
for i in fruits:
    print(i)'''

'''names=["ammu","savi","sruthi","vasavi","mahima"]
for i in names:
    print(i,end=" ")'''

#while loop

'''a=10
while a<1:
    print(a)'''

'''a=10
while a>5:
    print(a)
    a=a-1'''

'''count = 0
while count < 5:
    print(count)
    count+=1'''

#voting

'''while True:
    age=int(input("enter your age"))
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")'''

#even and odd

'''while True:
    num=int(input("enter the value"))
    if num%2==0:
        print("even number")
    else:
        print("odd number")'''

#guest

'''while True:
    a=str(input("enter the name"))
    if a=="ammu":
        print("welcome ammu")
    else:
        print("welcome guest")'''

#run time
#while True:
'''a=[1,2,3,4,5]
b=int(input())
for b in a:
    print("true")
else:
    print("false")'''

#start-stop-step

'''for i in range (5):
    print(i)

for i in range (7,15):
    print(i)'''

'''for i in range (5):
    print(i,end=" ")

for i in range (25,45):
    print(i,end=" ")'''


#start-stop-step

'''for i in range(0,20,2):
    print(i,end=" ")

for i in range(5,50,5):
    print(i)

for i in range(3,30,3):
    print(i)'''

#grade code

'''while True:
    grade=int(input("enter the students marks"))
    if grade in range(91,101):
        print("grade A")
    elif grade in range (81,91):
        print("grade B")
    elif grade in range (71,81):
        print("grade C")
    elif grade in range(50,71):
        print("grade D")
    elif grade in range (0,50):
        print("fail")'''


''' while True:
    grade=int(input("enter the students marks"))
    if grade in range(91,101):
        print("grade A")
    elif grade in range (81,91):
        print("grade B")
    elif grade in range (71,81):
        print("grade C")
    elif grade in range(50,71):
        print("grade D")
    else:
        print("fail")'''


'''for i in range (5):
    i+=1
    print(i)
    

i = 0
while i < 3:
       print(i)
       i += 1 
else:
      print(0)

#difference between break and continue,pass

the break stmt terminates the current loop or statements, the continue stmt skips the remaining code inside the loop for the current irteration only
and the pass stmt is a null stmt that does nothing


i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)

#break

a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break

#continue

a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        continue

     
a=10
while a>1:
    a=a-1
    if a==6:
        continue
    print(a)


i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i+=1'''

#vowels and constants

'''name=input()
vowels="aeiouAEIOU"
count=0
for i in name:
    if i in vowels:
        count+=1
print("no.of vowels",count)'''

#for loop break stmt
 
'''for i in range (10):
    if i==5:
        break
    print(i)'''

#for loop continue stmt

'''for i in range(15):
    if i==7:
        continue
    print(i,end=" ")'''

#pass

for i in range(9):
    if i==4:
        pass
    print(i)






    





