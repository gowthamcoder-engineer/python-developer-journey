# # a=int(input("enter the age of ur father "))
# # b=int(input("enter the ue=r current age "))
# # diff=a-b
# # print("age gap is= ",diff)
# # print("My name is Gowtham m \n My age is 21 \n and college is ksit")
# # a=int(input("enter the first number:"))
# # b=int(input("enter the second number:"))
# # sum=a+b
# # print("sum of two numbers is=",sum)
# for i in range(5):
#     print("gowtham m")
# for i in range(1,6,2):
#     print(i)
# i=1
# while i<=5:
#     print(i)
#     i+=1
# for i in range (1,10):
#     if i==5:
#        continue
#     print(i)
import random

# Computer picks a random number between 1 and 50
secret_number = random.randint(1, 50)

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")

# Counter to track attempts
# attempts = 0

# while True:
#     guess = int(input("Enter your guess: "))
#     attempts += 1

#     if guess == secret_number:
#         print(f"🎉 Congratulations! You guessed it right in {attempts} attempts.")
#         break
#     elif guess < secret_number:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
CONDIIONAL STATEMENTS 

number=int(input("enter the number:"))
if(number%2==0):
    print("entered nuber is even")
else:
    print("entered number is odd")
first=int(input("enter the first number :"))
second=int(input("enter the second number:"))
third=int(input("enter the third number:"))
if(first>second and first>third ):
    print("first number is greater ")
elif(first<second and third<second ):
     print("second number is greater ")
else:
     print("third number is greater ")
x=int(input("enter the x numbe"))
if(x%7==0):
    print("multiple of 7")
else:
    print("entered nuber is not multiple of 7")

# lists are used to store data inthe square bracket 
marks=[32,34,45,46,56,43,22,45,66,77,784,34,2345,65631,]
# print(marks[1])
first=float(input("enter the first number"))
sec=float(input("enter the second number"))
avg=(first+sec)/2
print("average of two floating numbers",avg)
a=int(input("enter the number"))
b=int(input("enter the number"))
if(a>=b):
    print("True")
else:
    print("false")
str1="this is string"
str2='iam gowtham'
str3='''this is string'''
str="iam gowtham"
print(str[4])\
str="iam gowtham"

print(str[4:len(str)])
str="apple"
print(str[-3:-1])
str="$$$$4iam gowtham"
print(str.count("$"))
num=int(input("enter the number"))
if(num%2==0):
    print("entered number is even")
else:
  input()  print("entered num is odd")
x=int(input("enter the number"))
if (x%7==0):
    print("multiple of 7")
else:
    print("it tis not multiple of 7")
movies=[]
mov1=input("enter the first movie ")
mov2=input("enter the 2 movie ")
mov3=input("enter the 3 movie ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
loops
count=1
while count<=5:
    print("hello")
    count+=1
i=1
while i<=1000:
    print("iam gowtham")
    <=100+=1
i=1
while i<=100:
    print(i)
    i+=1
n=int(input("enter the number "))
i=1
while i<=10:
    print(n*i)
    i+=1
for i in range(0,101,2):
    print(i)
n=int(input("enter the first 10 natural numbers "))
sum=0
for i in range (1,n+1):
    sum=sum+i
print(sum)
n=int(input())
for i in range (1,11):
    print(n,"*",i, "=" , n*i)
class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add(self, id, name):
        new = Node(id, name)
        new.next = self.head
        self.head = new

    def search(self, id):
        temp = self.head
        while temp:
            if temp.id == id:
                return temp.name
            temp = temp.next
        return "Not Found"

    def display(self):
        temp = self.head
        while temp:
            print(temp.id, temp.name)
            temp = temp.next

s = StudentList()
s.add(101, "Gowtham")
s.add(102, "Rahul")
s.display()
print(s.search(101))
how to define a function in python
def add(a,b):
    result=a+b
    return result
print(add(10,20))
def greet():
    print("hello gowtham welcome to pyhton")

list=[1,2,3,4,5,6,7]
for val in list:
    print(val)
list=[1,4,9,16,25,36,49,64,81,100]
x=49
idx=0
for el in list:
    if(el==x):
        print("number found at idx",idx)
    idx+=1
n=int(input("enter the number:"))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("sum of n numbers:",sum)
n=int(input("enter the number"))
fact=1
for i in range(n,1,-1):
    fact=fact*i
print("factorial of a number is :",fact)

 


# revison for the python from the basics 
variables how to declare variables in python in python it will asign the variabl type automatically
for example 
x=10
name="gowtham"
price=68.8
weight=74.456
is_active=True
print(type(x))
print(type(name))
print(type(price))
print(type(weight))
how the input and the output will works in the python is 
for input we ahve to mention the keyword input and we acan get the input from the  user ok.. for out we just want to use the print key word that is more than enuogh for the out put..
name=input("Enter the name:")
print("hello",name)
what is type casting 
practice progrms
swap two number usin temp
# even or odd one thing keep in my that if anything know program is came than use the tricks and thalogic it will easy u to to remember..
num=int(input("enter the number:"))
if num%2==0:
    print("the number is even")
else:
    print("number is odd")
a=int(input("enter first num:"))
b=int(input("enter the second num:"))
print("1. Add")
print("2. sub")
print("3. mul")
print("4. div")
choice=int(input("enter the choice:"))

if choice==1:
    print("result=",a+b)
elif choice==2:
    print("result=",a-b)
elif choice==3:
    print("result=",a*b)
elif choice==4:
    if b!=0:
       print("result=",a/b)
    else:
        print("can not devide by zero")

else:
    print("Invalid choice")
#FIND THE LARGEST OF THE TWO NUBERS 
a=int(input("enter the first number:"))
b=int(input("enter the second number "))
if a>b:
    print(" a is greater than b")
else:
    print("b is greater than a")

 temperature converter
celsius=float(input("enter temperature: "))
fahrenheit=(celsius*9/5)+32
print("Temperature in fahrenheit :",fahrenheit)

print("1. fahrenheit to celsius")
print("2. celsius to fahrenheit")
choice=int(input("enter the choice:"))
if choice==1:
    f=float(input("enter the fahrenheit :"))
    c=(f-32)*5/9
    print("celsius is :",c)
elif choice==2:
    c=float(input("enter the celsius:"))
    f=(c*9/5)+32
    print("fahrenheit is :",f)
else:
    print(" Invalid choice")
a=int(input("enter the first num:"))
b=int(input("enter the second num:"))
a,b=b,a
print("a=",a)
print("b=",b)
FACTORIAL OF A NUM
n=int(input("enter the number:"))
fact=1
for i in range( 1,n+1):
    fact=fact*i
print("factorial of a number is:", fact)

## CONDITIONAL STATEMENTS AND THE LOOPS 
SYNTAX FOR THE CONDITIONAL STATEMEENT IS 
IF CONDITION:
    CODE
ELIF CONDITION :
    CODE 
ELSE :
   CODE
NESTED IF 
num=int(input("enter the number:"))
if num>0:
    if num%2==0:
        print(" the number is positive even number")
    else:
        print("The number is nagative odd number or else")

