math =50

chem =50

print(id(math))

print(id(chem))











2.math =50

chem =50

phy = 50

english = 60

print(id(math))

print(id(chem))

print(id(phy))

print(id(english))

&#x20;





3.print(2+2) #4

print("2"+"2") #22

val1 =input("Enter first value:") #22

val2 =input("Enter second value:") #22

peint(val1+val2)







4\.

\#print(int(3.14))

\#print(int(10+5j))

print(int(True)) #=1

print(int(False)) #=0

\#print(int("4.22"))

print(int("4"))

print(int("bhavani"))



(bhavani is not integer so we have error)













5.#print(float(3)) #3.0

\#print(float(50+2j))

print(float(True)) #=1

print(float(False)) #=0

\#print(float("4.22"))

print(float("4"))



(cnte+/......>comment entire code



6\.

print(bool(0))

print(bool(15))

print(bool(3.14))

print(bool(0.0))

print(bool(1+2i))

print(bool(0+0j))

print(bool(-1))

print(bool(False))

print(bool(True))

print(bool(" "))



7]

(this program is not executed so try again)(2i=2j)



\#decision making statement(conditional statement



n=int(input("Enter any single digit:")) #6

if n>0:

&#x20;   print("Positive number")

if n<0:

&#x20;   print("Negative number")

if n==0:

&#x20;   print("Zero")









8\.



n1 = int(input("Enter value of n1:"))

n2 = int(input("Enter value of n2:"))

n3 = int(input("Enter value of n3:"))

n4 = int(input("Enter value of n4:"))

n5 = int(input("Enter value of n5:"))



if n1>n2 and n1>n3 and n1>n4 and n1>n5:

&#x20;   print("N1 is max value")

if n2>n1 and n2>n3 and n2>n4 and n2>n5:

&#x20;   print("N2 is max value")

if n3>n1 and n3>n3 and n3>n4 and n3>n5:

&#x20;   print("N3 is max value")

if n4>n1 and n4>n3 and n4>n4 and n4>n5:

&#x20;   print("N4 is max value")

if n5>n1 and n5>n3 and n5>n4 and n5>n5:

&#x20;   print("N5 is max value")







9\.

n1 = int(input("Enter value of n1:"))

n2 = int(input("Enter value of n2:"))

n3 = int(input("Enter value of n3:"))

n4 = int(input("Enter value of n4:"))

n5 = int(input("Enter value of n5:"))



if n1>n2 and n1>n3 and n1>n4 and n1>n5:

&#x20;   print("N1 is max value")

if n2>n1 and n2>n3 and n2>n4 and n2>n5:

&#x20;   print("N2 is max value")

if n3>n1 and n3>n3 and n3>n4 and n3>n5:

&#x20;   print("N3 is max value")

if n4>n1 and n4>n3 and n4>n4 and n4>n5:

&#x20;   print("N4 is max value")

if n5>n1 and n5>n3 and n5>n4 and n5>n5:

&#x20;   print("N5 is max value")



(program is not complited)





10.wap to calculate simple interst



pa=int(input("enter principal amount:"))

roi=int(input("enter rate of interst:"))

time=int(input("enter the loan amount duration:"))



si=pa\*roi\*time/100

print("simple interst=",si)





11\. wap inch to cm



h=float(input("enter height in feet"))

inch=h\*12

cm=inch\*2.54

print("Hight in inches:",inch)

print("Hight in centimers:",cm)





12\.

name =      "bhavaniraksh"

\#indexing =  012345678910

print(name\[0])

print(name\[1])

print(name\[-1])

\#print(name\[15])Error string index out of range

print(name\[0:5])

print(name\[1:])

print(name\[:5])

print(name\[:])

print(name\[1:8:2])

print(name\[::-1])



13\. s = "hel4code is a best platform for practicing programming"

print(s.find("help4code"))

print(s.find("python"))

print(s.find("programming"))





14\.

s = "bhavani","charan","mangasuli"

m = '|'.join(s)

print(m)



13\.

s="Python is High Level Programming Language"

print(s.lower())

print(s.upper())

print(s.swapcase())

print(s.title())

print(s.capitalize())





15\.

phy = 50

chem = 60

math = 70

print("phy ={} chem = {} math={}".format(phy,chem,math))

print("phy ={0} chem = {1} math={2}".format(phy,chem,math))

print("phy ={x} chem = {y} math={z}".format(x=phy,y=chem,z=math))

total = phy+chem+math

print("total marks",f"{total}")

print("roll no","7".zfill(4))





16\. (BODMAS)

a=50

b=30

c=20

d=10

print((a+b)\*c/d)

print((a-b)\*c/d)

print(a+(b\*c)/d)









collection datatype :



1.list

&#x09;\* mutable

&#x09;. list replace by \[] brackets

&#x09;wha





1]

mylist = \["bhavani","magadum","rakshita","bedage","bhavani",77,"hit",60.52,"ece"]

print(mylist)

print(type(mylist))

print(mylist\[0])

print(mylist\[1])

print(mylist\[2])

print(mylist\[-1])

print(mylist\[2:5])

print(mylist\[:5])

print(mylist\[1:8:2])

print(mylist\[:])

print(mylist\[::-1])









**2.**

**mylist = \["bhavani","rakshita","poorva",77,"hit","ece",77.07]**

**print(mylist)**

**if "poorva" in mylist:**

&#x20;  **print("yes poorva is avilable")**

**else:**

&#x20; **print("not avilable")**



**3]**

**mylist = \["bhavani","rakshita","poorva",77,"hit","ece",77.07]**

**print(mylist)**



**#mylist.append('bhakti')**

**#mylist.append('sanjana')**

**#print(mylist)**



**#mylist.insert(1,"magadum")**

**#print(mylist)**



**mylist.remove("hit")**

**print(mylist)**



**newlist=mylist.copy()**

**print(mylist)**

**print(newlist)**



**4]**

**mylist = \["bhavani","rakshita","poorva",77,"hit","ece",77.07]**

**print(mylist)**



**print(mylist)**

**#print(mylist\[row]\[col])**

**print(mylist\[0]\[0])**

**print(mylist\[0]\[1])**

**print(mylist\[1]\[0])**

**print(mylist\[2]\[0])**

**print(mylist\[2]\[1])**





**5]**

**mlist =\[ \["bhavani","rakshita"],\["poorva",77,"hit"],"ece","yyy"]**

**print("example of multidimentional list:")**



**print(mlist)**

**#print(mylist\[row]\[col])**

**print(mlist\[0]\[0])**

**print(mlist\[0]\[1])**

**print(mlist\[1]\[0])**

**print(mlist\[2]\[0])**

**print(mlist\[2]\[1])**

&#x20;



**6]**

**#mlist =\[ \["bhavani","rakshita"],\["poorva",77,"hit"],"ece","yyy"]**

**#print("example of multidimentional list:")**



**#print(mlist)**

**#print(mylist\[row]\[col])**

**#print(mlist\[0]\[0])**

**#print(mlist\[0]\[1])**

**#print(mlist\[1]\[0])**

**#print(mlist\[2]\[0])**

**#print(mlist\[2]\[1])**



**list = \["bhavani","rakshita"]**

**print(list\*2)**



&#x20;

&#x20;

**7.**



**list1 = \["bhavani","rakshita"]**

**#print(list\*2)**



**list2=\[50,25,50]**

**print(list1 + list2)**

&#x20;

&#x20;

**8] list constructor:**





**name = "bhavani"**

**print(name)**

**myname = list(name)**

**print(myname)**

&#x20;

&#x20;



**9]**



&#x20;

&#x20;**mylist = \[40,30,20,11]**

&#x20;**mylist.reverse()**

&#x20;**print(mylist)**

&#x20;

**10.**

&#x20;

**mylist=\[44,22,77,0,9,88]**

**newlist=mylist #both the list having same assress**

**print(id(mylist))**

**print(id(newlist))**







11\.

mytuple = ("rakshita","bhavi","vasu","poori","sanji","shraddha",23,3,15,77,"vasu")

\#print(tuple)

\#print(type(mytuple)

print(mytuple)

print(type(mytuple))





12\.



\#membership operator

2type

\#1. in

\#2.not in



print('z'in "rakshita"

print('z' not in "rakshita")

mylist=\[3,5,2,8,9]

print(3 in mylist)





13\.

identity operator

2 type

1.is

2.is not

for eg:

&#x20;    a=10

&#x20;    b=10

a=10

b=10

print(id(a))

print(id(b))



print(a is b) #true

print(a is not b) #false





14\.

&#x20;set datatype

&#x20;a.

myset={2,3,4,"rash",7,8}

print(myset)

\#print(type(myset))



myset.discard(3)

print(myset)





b.

myset={2,3,4,"rash",7,8}

print(myset)

\#print(type(myset))



myset.remove(3)

print(myset)













15\.

myset={10,20,30,40}

yorset={"rakshita","bedage"}

newset=myset.union(yorset)

print(newset)





16\.

myset={10,20,30,40}

yorset={10,50,60,30}

print(myset.intersection(yorset))





17\.

clear () we can use

myset={10,20,30,40}

print(myset.pop())







18\.

nested if else

if condition-1

&#x20;    if condition-2:

&#x20;         #staement

&#x20;    else:

&#x20;        #staement

else:

&#x20;     if condition-3:

&#x20;         #staement

&#x20;    else:

\#staement



program:

1\.



a=int(input("enter the value of a:"))#5

b=int(input("enter the value of b:"))#10

c=int(input("enter the value of c:"))#20

if a>b:

&#x20;   if a>c:

&#x20;       print("A is greater")

&#x20;   else:

&#x20;       print("c is greater")

else:

&#x20;   if b>c:

&#x20;       print("b is greater")

&#x20;   else:

&#x20;       print("c is greater")

2\.

a=int(input("enter the value of a:"))

b=int(input("enter the value of b:"))

c=int(input("enter the value of c:"))

if a>b:

&#x20;   if a>c:

&#x20;       print("A is minimum")

&#x20;   else:

&#x20;       print("c is minimum")

else:

&#x20;   if b>c:

&#x20;       print("b is minimum")

&#x20;   else:

&#x20;       print("c is minimum")



19\.

mylist=\[3,2,4,7,8]

for i in mylist:

&#x20;   print (i)





20\.

\#for (initialization: condition; inc/dec)

a.



for i in range(5):#i=5

&#x20;   print(i)



b.



for i in range(1,5):#i=1

&#x20;   print(i)

&#x20;

c.

for i in range(1,11,2):#i=1

&#x20;   print(i)

&#x20;

d.

for i in range(1,11,):#i=3

&#x20;   print(i)

&#x20;



e.



for i in range(1,11):#i=3

&#x20;   print(i\*2,"",i\*3,"",i\*4)







21\.



username=input("enter username:")

password=input("enter password:")

if username==password:

&#x20;   print("login successful")

else:

&#x20;   print("Invalid login")





22]

brand=input("Enter your coldrink name either in upper case or in lower case:")

if brand == "pepsi"or brand == "PEPSI":

&#x20;   print("swag")

elif brand == "dew" or brand == "DEW":

&#x20;   print("dag age jeet hai")

elif brand == 'thumsup' or brand =='THUMSUP':

&#x20;   print ('taste the thunder')

else:

&#x20;   print('go with your brand')

&#x20;



23]

n1=int(input("Enter First Number:"))

n2=int(input("Enter Second Number:"))

n3=int(input("Enter Third Number:"))

if n1>n2 and n1>n3:

&#x20;   print("Biggest Number is :",n1)

elif n2>n3:

&#x20;   print("Biggest Number is :",n2)

else:

&#x20;   print("Biggest Number is :",n3)









24]

count=0

for i in range(9):

&#x20;   if i%2 == 0:

&#x20;       print(i)

&#x20;   else:

&#x20;   print(i)

&#x20;   count+=1

&#x20;   print("count =",count)



25\.



list = \[7,3,9,2,8]

list.sort()

print(list)

print(list\[-2])







26



list =\[0,1,0,3,12]

for i in list:#i=0:0

&#x20; if i==0:

&#x20;     list.remove(i)

&#x20;     list.append(i)

print(list)



27\.

\#a



A=\[1,2,3]

B=\[2,3,4]

C=\[3,4,5]

result=list(set(A)\&set(B)\&set(C))

print(result)

\#for loop perfrom iteration

\# take first element form A

\#and check it present in B and C using





\#b



A=\[1,2,3]

B=\[2,3,4]

C=\[3,4,5]

\# result=list(set(A)\&set(B)\&set(C))

\# print(result)

for i in A:#i=

&#x20; if i in B and i in C:

&#x20;     print(i)



28



\#while loop syntax:

i=1 #i=2

while i<=5:

&#x20;   print(i)

&#x20;   i=i+1



29



even=0 #2

odd=0 #2

i=1 #i=1

while i<=10:

&#x20;   if i%2==0:

&#x20;       even=even+1

&#x20;   else:

&#x20;       odd=odd+1

&#x20;   i=i+1

print("Even=",even)

print("odd=",odd)





30\.





\#1+2+3+4+5+6+7+8+9+10=55

\#WAP for this using while loop

list=\[1,2,3,4,5,6,7,8,9,10]

i=1

sum=0

while i<=10:

&#x20;   sum=sum+i

&#x20;   i=i+1

&#x20;   print("sum=",sum)



31\.

for i,j in zip(range(1,6),range(5,0,-1)):#i=6,j=0

&#x20;   if i == 3 and j == 3:

&#x20;         continue

&#x20;   print(i,"",j)





32\.



&#x20;   1  2   3

1   1  1   1

2   2  2   2

3   3  3   3



\#(i,j)=(1,1)

for i in range(1,4): #outer loop==>row's

&#x20;   for j in range (1,4):#inner loop==>col's

&#x20;           print(i,end="")

&#x20;   print()



33\.



\#chr()function typecast integer value in charecter

n=int(input("Enter the number of row:"))#n=5

for i in range(1,n+1):#i=1,n=6

&#x20;   for j in range(1,n+1): #j=1

&#x20;       print(i,end=" ")

&#x20;   print()



34\.



\#chr()function typecast integer value in charecter

n=int(input("Enter the number of row:"))#n=5

for i in range(1,n+1):#i=1,n=6

&#x20;   for j in range(1,n+1): #j=1

&#x20;       print(n+1-i,end=" ")

&#x20;   print()



35\.



\#chr()function typecast integer value in charecter

n=int(input("Enter the number of row:"))

for i in range(1,n+1):

&#x20;   for j in range(1,1+1):

&#x20;       print(i,end=" ")

&#x20;   print()





##### **#two type of functions**

###### 

**#built in function**

**#user define function**



###### 

**#built in function**

&#x20;**#eg: type() ,id(),**



**#user define function**

&#x20;**#accoding to program requirement programmer can developed the function is called user function**



**36.**

**def msg():#called function**

&#x20;   **print("hello world")**

**msg()#calling function**

**msg()#calling function**

**msg()#calling function**





**37.**



&#x20;

**def login():#call function**

&#x20;   **username=input("enter username")**

&#x20;   **password=input("enter password")**

&#x20;   **if username==password:**

&#x20;       **print("login successful")**

&#x20;   **else:**

&#x20;       **print("invalid credential")**

**login()#calling function**





##### **#how many type of argument we can pass in function**



**#1.position argument**

**#2.key argument**

**#3.default argument**

**#4.variable length argument**



**38.**

**#position argument**

**def add(x,y):**

&#x20;   **print("Add=",x+y)**

&#x20;

**add(2,3)#calling function**



**39.**



**#position argument**

**def add(x,y):**

&#x20;   **print("Add=",x+y)**

&#x20;

**a=int(input("enter the value of A:"))**

**b=int(input("enter the value of A:"))**

**add(a,b)#calling function**



**40.**



**#position argument**

**def add(x,y):**

&#x20;   **return x+y**

&#x20;

&#x20;

**a=int(input("enter the value of A:"))**

**b=int(input("enter the value of A:"))**

**#print(add(a,b))**

**result=add(a,b)**

**print("add=",result)**





**41.**



**#position argument**

**def add(x,y):**

&#x20;   **add=x+y**

&#x20;   **sub=x-y**

&#x20;   **mul=x\*y**

&#x20;   **div=x/y**

&#x20;   **return add,sub,mul,div#in tuple**

&#x20;

&#x20;

**a=int(input("enter the value of A:"))**

**b=int(input("enter the value of A:"))**

**#print(add(a,b))**

**result=add(a,b)**

**print("add=",result)**

**add(a,b)#calling function**



**42.**



**#variable length aergument/variable number of argument**

**def cityName(city="yadur"):**

&#x20;   **print("city Name=",city)**

**cityName("Pune")**

**cityName("kolapur")**

**cityName()#in this case default value will used**



**43.**



**def cityName(\*city):**

&#x20;   **print("city Name=",city)**



**cityName("Nidasoshi","Yadur","Chikkodi","Belagum")**



**44.**



**#nested  function**

**def outerFunction():**

&#x20;   **print("Outer Function")**

&#x20;   **def innerFunction():**

&#x20;       **print("innerFunction")**

&#x20;   **innerFunction()**

**outerFunction()**



##### **#TYPE OF error**



**#1.syntax error**

&#x20;**# come when we do not follow porper syntactical rule means predefine grammatical rule of python language**

**#2. runtime error**

&#x20;**# come due to incorrect logic or wrong input give by end user and run time**





**45.**

a=int(input("enter any one number:"))

b=int(input("enter second number:"))

print(a/b)



##### Exception handling by try and except

&#x20;exception:it is just handling the error or ensures the if a runtime error occurs inany part of the code



try

&#x20;   --------------------------

&#x20;   --------------------------

&#x20;   --------------------------

except xyz

&#x20;   --------------------------

&#x20;   --------------------------

&#x20;   --------------------------

46\.



a=int(input("enter any one number:"))

b=int(input("enter second number:"))

try:

&#x20;    print(a/b)

except:

&#x20;   print("can't divide by zero")



47\.



try:

&#x20;   a=int(input("enter any one number:"))

&#x20;   b=int(input("enter second number:"))

except(zeroDivisionError):

&#x20;   print("can't devide by zero")

except(ValueError):

&#x20;    print("enter only integer number")



48\.



a=int(input("enter any one number:"))

b=int(input("enter second number:"))

try:

&#x20;   print(a/b)

except zERODivisionError as message:

&#x20;   print("The description of exception:",message)





49\.



try:

&#x20;   a=int(input("enter any one number:"))

&#x20;   b=int(input("enter second number:"))

&#x20;   print(a/b)

except (ValueError,zERODivisionError) as message:

&#x20;   print(message)



50\.





try:

&#x20;   a=int(input("enter any one number:"))

&#x20;   b=int(input("enter second number:"))

&#x20;   print(a/b)

except (ValueError,zERODivisionError) as message:

&#x20;   print("enter correct number:",message)

except:

&#x20;   print("This is default part of except block")



51\.



try:

&#x20;   a=int(input("enter any one number:"))

&#x20;   b=int(input("enter second number:"))

&#x20;   print(a/b)

except (ValueError,zERODivisionError) as message:

&#x20;   print("enter correct number:",message)

except:

&#x20;   print("This is default part of except block")



52\.



\#finally block will always executed whether try block genrate error or not



try:

&#x20;    a=int(input("enter any one number:"))

&#x20;    b=int(input("enter second number:"))

&#x20;    print(a/b)

except (ValueError,zERODivisionError) as message:

&#x20;    print("enter correct number:",message)

finally:

&#x20;   print("I will always executed")



53\.



&#x20;#nested try except block

try:

&#x20;

&#x20;   a=int(input("enter any one number:"))

&#x20;   b=int(input("enter second number:"))

&#x20;   try:

&#x20;       print(a/b)

&#x20;   except (ValueError,zERODivisionError) as message:

&#x20;       print(msg)

except ValueError as msg:

&#x20;       print(msg)



54\.



try:

&#x20;

&#x20;   a=int(input("enter any one number:"))

&#x20;   b=int(input("enter second number:"))

&#x20;   print(a/b)

except (ValueError,zERODivisionError) as message:

&#x20;   print(msg)

else:

&#x20;   print("there are not error in try block")

finally:

&#x20;   print("i am finally block i always execute weather error raise or not")





55\.

bank\_bal=500

if bank\_bal<2000:

&#x20;   raise Exception("your account balance is below a accessing limit")

&#x20;else:

&#x20;    print("your amount has withrawal")







56\.

modules in python

every.py file act as a python module because it contain everything



57\.

import math

print(math.sqrt(16))

print(math.pi)



58]

import math as m

print(m.sqrt(4))

print(m.pi)



59]

\#to generate random integer between two given

\#numbers(includes)

from random import\*

for i in range(5):#0-4

&#x20;print(randint(1,100000))



60]

choice() function:

&#x20;   It wont return random number.

&#x20;   It will return random object from given list on tuple.

&#x20;

&#x20;   from random import\*

&#x20;   list=\["bhavani","magadum","rakshi","bedage","hit"]

&#x20;   for i range





61>

module1

&#x20;

&#x20;   def welcome(fname,lname):

&#x20;       print("Hello  ",+fname)

&#x20;       print("Hello  ",+lname)

&#x20;

&#x20;       def login(username,password):

&#x20;           if username==password:

&#x20;               print("you have login successfully")

&#x20;           else:

&#x20;               print("you have entered wrong username and password")

&#x20;

&#x20;   def square(num):

&#x20;       print("square of two no=",num\*num)

&#x20;   pi=3.141592653589793



module2



import module1

module.square(4)

module.login("admin","admin")

print(module1.pi)



def add():

&#x20;   a=int(input("enter value of A:"))

&#x20;   b=int(input("enter value of B:"))

&#x20;   print("add="a+b)

def sub():

&#x20;   a=int(input("enter value of A:"))

&#x20;   b=int(input("enter value of B:"))

&#x20;   print("sub="a-b)

def mul():

&#x20;   a=int(input("enter value of A:"))

&#x20;   b=int(input("enter value of B:"))

&#x20;   print("mul="a\*b)

def div():

&#x20;   a=int(input("enter value of A:"))

&#x20;   b=int(input("enter value of B:"))

&#x20;   print("div="a/b)

&#x20;   while True:

&#x20;   print("1. Add:")

&#x20;   print("2. Sub:")

&#x20;   print("3. Mul:")

&#x20;   print("4. div:")

&#x20;   choice=int(input("enter your choice"))

&#x20;   if



1]



a=\[1,2,3,4,5,6,7,8,9]

a\[::2]=10,20,30,40,50

print(a)



2]

a=\[1,2,3,4]

print(a\[3:0:-1])



3]

def f(i,value = \[]):

&#x20;   values.append(i)

&#x20;   print(value)

&#x20;   #return value

f(1)

f(2)

f(3)



1\.



\#polymorphism implemented here

\#overloading

\#in python method overloding is not possible

\# if we are trying to declare multiple methodnwith same name and

\#diferent number of argument then python will always consider only last method.

class Arithmatic:

&#x20;   def add(self,a):

&#x20;       print(a)

&#x20;   def add(self,a,b):

&#x20;       print(a+b)

&#x20;   def add(self,a,b,c):

&#x20;       print(a+b+c)

obj=Arithmatic()

obj.add(10)

obj.add(10,20)

obj.add(1,2,3)



2\.



To handle overloaded method in python if method with variable number of arguments required then we can handle with default arguments





class Arithmatic:

&#x20;   def add(self,a=None,b=None,c=None):

&#x20;       if a!=None and b!=None:

&#x20;           print(a+b)

&#x20;       elif a!=None and b!=None and c!=None:

&#x20;           print(a+b+c)

&#x20;       else:

&#x20;           print("enter atleast two argument")

obj = Arithmatic()

obj.add(10)

obj.add(10,20)

obj.add(1,2,3)





3\.



class Deposit:

&#x20;   def \_\_init\_\_(self,cash):

&#x20;       self.cash = cash

&#x20;   def \_\_add\_\_(self,other):

&#x20;       return self.cash + other.cash

d1=Deposit(1000)

d2=Deposit(2000)

print("total cash deposite amuont=",d1+d2)





4\.



class Rbi:

&#x20;   def homeLoan\_ROI(Self):

&#x20;       print("Home Loan Rate of interest =7.5%")

&#x20;

&#x20;   def carLoan(self):

&#x20;       print("Car loan Rate of intrest= 8%")



class Sbi(Rbi):

&#x20;   def homeLoa\_ROI(self):

&#x20;       print("Home Loan Rate of intrest=6.5%")

&#x20;

obj=Sbi()

obj.homeLoan\_ROI()

obj.carLoan()





5\.





\#c0nstructor overriding

class Father:

&#x20;   def \_\_init\_\_(self):

&#x20;       print("Father:=i am allready at breafast table")

class Child(Father):

&#x20;   def \_\_init\_\_(self):

&#x20;       print("Child:= i will be late for breakfast")

obj = Child()





ABSTRACT CLASS:  Read about these topic for intervive





6.]



from abc import ABC, abstractmethod

class Help4code(ABC): # abstract class

&#x20;   @abstractmethod # decorator

&#x20;   def training(self):# abstract method

&#x20;       pass

&#x20;

&#x20;   @abstractmethod   # abstract method

&#x20;   def placement(self):

&#x20;       pass

&#x20;

class Ashish(Help4code):

&#x20;   def training(self):

&#x20;       print('C , C++ , Java')

&#x20;   def placement(self):

&#x20;       print("Java placement")

&#x20;

class Ankush(Help4code):

&#x20;   def training(self):

&#x20;       print("Python | Django")

&#x20;   def placement(self):

&#x20;       print("Python placement students")

&#x20;

class Prashant(Help4code):

&#x20;   def training(self):

&#x20;       print("Machine learning")

&#x20;   def placement(self):

&#x20;       print("Data science placement")

&#x20;

obj1 = Ashish()

obj1.training()

obj1.placement()

&#x20;

obj2 = Ankush()

obj2.training()

obj2.placement()

&#x20;

obj3 = Prashant()

obj3.training()

obj3.placement()





6]



from abc import ABC, abstractmethod

class Help4code(ABC): # abstract class

&#x20;   @abstractmethod # decorator

&#x20;   def training(self):# abstract method

&#x20;       pass

&#x20;

&#x20;   @abstractmethod   # abstract method

&#x20;   def placement(self):

&#x20;       pass

&#x20;

class Ashish(Help4code):

&#x20;   def training(self):

&#x20;       print('C , C++ , Java')

&#x20;   def placement(self):

&#x20;       print("Java placement")

&#x20;

class Ankush(Help4code):

&#x20;   def training(self):

&#x20;       print("Python | Django")

&#x20;   def placement(self):

&#x20;       print("Python placement students")

&#x20;

class Prashant(Help4code):

&#x20;   def training(self):

&#x20;       print("Machine learning")

&#x20;   def placement(self):

&#x20;       print("Data science placement")

&#x20;

obj1 = Ashish()

obj1.training()

obj1.placement()

&#x20;

obj2 = Ankush()

obj2.training()

obj2.placement()

&#x20;

obj3 = Prashant()

obj3.training()

obj3.placement()



7\.



\#naming convention rule=classnamestarts with capital letter

class Student:

&#x20;   #data member

&#x20;   a=10

&#x20;   b=20

&#x20;   #self is default argument

&#x20;   def add(self):

&#x20;       print(self.a+self.b)

\#object creation

obj=Student()

obj.add()

print(obj.a)#to call method we use calling function with .(dot)#by default everything in class is public







8\.



\#default constructor incomplete

&#x20;class NewClass:

&#x20;       def \_init\_(self):

&#x20;         print("constructor always execute first")

&#x20;        defshow(self)



9\.

\# class Hod:

&#x20;    def \_init\_(self):#constructor

&#x20;        self.name='Nayan Bongale'

&#x20;        self.age=20

&#x20;        self.empid=1001

&#x20;    def info(self):#instance method

&#x20;        print("My name is:",self.name)

&#x20;        print("My age is:",self.age)

&#x20;        print("My emp id is:",self.empid)

&#x20;obj=Hod()#object create,always create object ourside the class 

&#x20;obj.info()



10\.



\#parameterize constructor  error

&#x20;class Hod:

&#x20;    def \_ini\_(self,name,age,rollno):

&#x20;        self.name=name

&#x20;        self.age=age

&#x20;        self.rollno=rollno

&#x20;    def show(self):

&#x20;        print('name=',self.name)

&#x20;        print('age=',self.age)

&#x20;        print('rollno=',self.rollno)



&#x20;obj=Hod('Nayan',20,101)

&#x20;obj.show()



11\.



\#How many types of variables we can declair inside class   1.instance Variable  2.static Variable   3.local Variable 

\#WE can declare variable using self 



\#declaring instance variable inside a instance method by using self variable.

&#x20;class Student:

&#x20;    def \_init\_(self):

&#x20;        self.s\_name="prashant"#instance variable

&#x20;        self.s\_rollno=101

&#x20;        self.s\_branch="EC"

&#x20;    def getdata(self):#instance method

&#x20;        self.s\_mb=2323232323   #instance variable



12\.

&#x20;obj=Student()

&#x20;obj.getdata()

&#x20;obj.s\_branch="EC"#outside class instance variable by using object

&#x20;print(obj.\_dict\_)

&#x20;print(obj.s\_mb)

&#x20;print(obj.s\_name)

&#x20;#for every object instance variable will create separate memory



13\.

&#x20;class New:

&#x20;    def \_init\_(self):

&#x20;        self.a=10



&#x20;Obj1=New()

&#x20;Obj2=New()

&#x20;Obj3=New()

&#x20;Obj1.a=20 #value of obj1 is chaned but it will not reflect in obj2,3  becoz there is separate memory for all three

&#x20;print(Obj1.a)

&#x20;print(Obj2.a)

&#x20;print(Obj3.a)





14\.



\#static variable:1static variable=1 memory ,

\# by using object or self we can access or read static v but cannot modify or delete if try to delete there will be error.

\# class New:

\#     a=10#static    does not depend on object n does not vary object to object

&#x20;    def \_init\_(self):

&#x20;        self.name="nayan"#instance



&#x20;Obj1=New()

&#x20;Obj2=New()

&#x20;Obj3=New()

&#x20;print(Obj1.a)  #10

&#x20;print(Obj2.a)  #10

&#x20;print(Obj3.a)   #10

&#x20;New.a=20#we are changing the value of static var using classname

&#x20;print(Obj1.a)   #20 print(Obj2.a)    #20

&#x20;print(Obj3.a)     #20   there cannot be diferent values for obj1,2,3 bcoz 1static var=1 memory





15\.



\#thre types of methods declaired inside the class  1.static 2.instance  3.class



\#instance method:if any instance we are implementing inside of any method thats instance method,should have self as parameter



&#x20;class Student:

&#x20;    def \_init\_(self,name,rollno,mob):

&#x20;        self.name=name

&#x20;        self.rollno=rollno

&#x20;        self.mob=mob

&#x20;    def display(self):

&#x20;        print(self.name," ",self.rollno," ",self.mob)



&#x20;stud=Student("prashant",1001,9898989898)

&#x20;stud.display()



16\.



\#static method :  @staticmethod 



&#x20;class Student:

&#x20;    #by using  class name we can access static method

&#x20;    @staticmethod#decorator

&#x20;    def get\_personal\_detail(firstname,lastname):

&#x20;        print("your personal detail=",firstname,lastname)

&#x20;    @staticmethod

&#x20;    def contact\_detail(mob\_no,rollno):

&#x20;        print("your contact detail=",mob\_no,rollno)



&#x20;Student.get\_personal\_detail("nayan","bongale")

&#x20;Student.contact\_detail(2323232323,1001)



17\.



\#INHERITANCE:extending the prop from 1class to another

\#singlr,multilevel,multiple

\#baseclass:which enherits the  itd prop to another(parent class another name)

\#derived class:in which prop r inheirted (child class)





\#class derived-class(base-class):

\# -------------------------------

\# -------------------------------



\#single level inheritance

&#x20;class College:

&#x20;    def college\_name(self):

&#x20;        print("HSIT")



&#x20;class Student(College):

&#x20;    def student\_info(self):

&#x20;        print("Name:  Nayan Bongale")

&#x20;        print("Branch:  ECE")



&#x20;obj=Student()#object create child class

&#x20;obj.college\_name()

&#x20;obj.student\_info()





\#MULTILEVELInheritance

\#class Grandfather:

\#-------------------

\#------------------

\#class Father(Grandfather):

\#---------------------------

\#----------------------------

\#class Child(Father):

\#--------------------

\#--------------------



\#single level inheritance

\# class College:#first class level

&#x20;    def college\_name(self):

&#x20;        print("HSIT")



&#x20;class Student(College):

&#x20;    def student\_info(self):

&#x20;        print("Name:  Nayan Bongale")

&#x20;        print("Branch:  ECE")



&#x20;class Exam(Student):

&#x20;   def subject(self):

&#x20;       print("Subject1:Signal Engineering")

&#x20;       print("Subject2:Math")

&#x20;       print("Subject3:C-Language")



&#x20;obj=Exam()

&#x20;obj.college\_name()

&#x20;obj.student\_info()

&#x20;obj.subject()







\#MULTIPLE Inheritance       

\#SYNTAX

\#Class Parent1:

\#--------------

\#Class Parent2:

\#-------------

\#Class ParentN:

\#--------------

\#class derived(Parent1,Parent2,........)

\#---------------------------------------





&#x20;class SubjectMarks:

&#x20;    math=int(input("enter the marks of math:"))

&#x20;    DE=int(input("enter the marks of design engineering:"))

&#x20;    C=int(input("enter the marks of c language:"))

&#x20;    english=int(input("enter the marks of english:"))





\# class PracticalMarks:

&#x20;        cpract=int(input("enter the marks of c practical:"))



&#x20;   

&#x20;class Result(SubjectMarks,PracticalMarks):

&#x20;      def total(self):

&#x20;        if self.math>=40 and self.DE>=40 and self.C>=40 and self.english>=40 and self.cpract>=20:

&#x20;            print("pass")

&#x20;        else:

&#x20;            print("fail")



&#x20;obj=Result()

&#x20;obj.total()



&#x20;               

&#x20;   



\#multiple hirarchial and hybrid

















\#polymorphism----having may forms---ability of a message to display in multiple form

\#1.compiletime-funcn-overloading 2.runtime-funcn overriding





&#x20;class Principal:

&#x20;    def role(self):

&#x20;        print("i am amanging all activity of college")

&#x20;class Dean:

&#x20;    def role(self):

&#x20;        print('Dean=i am decision taking person')

&#x20;class Hod:

&#x20;    def role(self):

&#x20;        print('Hod=I have responsibilities of teahcers and students')

&#x20;class Faculty:

&#x20;    def role(self):

&#x20;        print('Faculty:I have to complete the syllubus successfully')





&#x20;def func(obj):

&#x20;    obj.role()

&#x20;campus=\[Principal(),Dean(),Hod(),Faculty()]

&#x20;for obj in campus:

&#x20;    func(obj)



