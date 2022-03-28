#1..to print two different strings in two different lines 
print("hello\nworld")
#2..to print two different string in one line
print("hello world")
print("hello","world",sep="\n")
#3..toinput two numbers and add them
a=int(input("enter first number"))
b=int(input("enter second number"))
print(a+b)
#4..to subtract
print(a-b)
#5..to multiply
print(a*b)
#6..exponential
print(a**b)
#7..to find area and perimeter of a rectangle
l=float(input("length"))
b=float(input("breadth"))
perimeter=2*(l+b)
area=l*b
print(perimeter,area)
#8..to find area and circumference of a circle
r=float(input("enter the radius of a circle"))
c=2*3.14*r
print(c)
area=3.14*r*r
print(area)
#9..program to find hypotenuse of a right angled triangle
from dataclasses import dataclass
from math import sqrt
from msilib.schema import tables
from re import A
a=int(input("first side"))
b=int(input("second side"))
c=sqrt(a**2 + b**2)
print(c)
#10..to swap two numbers
a=int(input("a"))
b=int(input("b"))
(a,b)=(b,a)
print(a,b)
#11..
notes = (2000,500,200,100,50,20,10,5,2,1)
amount = int(input("Enter Amount to be paid : "))
for C in notes:
    count = amount//C
    print("Note Value:", C,'\tnumber of notes ',count)
    amount = amount%C
#12..to find whether the triangle is scalene,isosceles,right angled or invalid 
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(inout("enter c:"))
if(a!=b!=c):
    print("scalene triangle")
elif(a==b!c or a==c! or b==c!a):
    print("isosceles triangle")
elif((a**2+b**2)**0.5=c or (b**2+c**2)**0.5=a or (c**2+a2)**0.5=b):
    print("right angled triangle")
else:
    print("'invalid")
#13..to find a simple interest and the total amount
p=int(input("enter principal value:"))
r=int(input("enter rate"))
t=int(input("enter time"))
simpleinterest=(p*r*t)/100
totalamount=p+((p*r*t)/100)
print("simpleinterest")
print("totalamount")
#14..to find compound interest 
compoundinterest=p*((1+r/100)**t)
print("compoundinterest")
#15..to calculate number of rectangular tiles required to cover a rectangular floor 


#16..to input number of overs in a cricket and output the maximum runs a player can score in match
overs=int(input("enter overs:"))
maxruns=((overs-1)*33)+36
print(maxruns)
# if else questions
#1..to find whether the number is odd or even
a=int(input("enter the value"))
if(a%2==0):
    print("even")
else:
    print("odd")
#2..to subtract smaller number from greater number
#3..to find maximum between two numbers
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
if(a>b):
    print("a is greater")
else:
    print("b is greater")
#4..to find maximum between three numbers
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c"))
if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")
#5..to check whether the number is positive negative or zero
a=int(input("enter value of a:"))
if(a<0):
    print("no. is positive")
elif(a==0):
    print("no. is zero")
else:
    print("no. is negative")
#6..to check whether the number is divisible by 5 and 11 or not
a=int(input("enter value of a:"))
if(a%5==0 or a%11==0):
    print("divisible by 5 and 11")
else:
    print("not divisible by 5 and 11")
#7..to check number is even or odd ----- same as ques. no. 1
#8..to check year is leap year or not
y=int(input("enter year"))
if(y%4==0 and y%100!=0):
    print("leap year")
elif(y%400==0):
    print("leap year")
else:
    print("not a leap year")
#9..to check whether a character is alphabet or not
ch=input("enter your character")
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print("character is alphabet")
else:
    print("character is not an alphabet")
#10..to check any alphabet is vowel or consonant
ch=input("enter your character")
if(ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' ch=='u'):
    print(ch,"is vowel")
else:
    print(ch,"is consonant")
#11..to input week number and print week days
weekday=int(input("enter weekday number"))
if(weekday==1):
    print("\nmonday")
elif(weekday==2):
    print("\ntuesday")
elif(weekday==3):
    print("\nwednesday")
elif(weekday==4):
    print("\nthursday")
elif(weekday==5):
    print("\nfriday")
elif(weekday==6):
    print("\nsaturday")
elif(weekday==7):
    print("\nsunday")
else:
    print("there are only only 7 days in a week")
#12..to input month number and print number of days in that month
month=int(input("enter month number"))
year=int(input("enter year"))
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    print("Number of days is 29");
elif(month==2) :
    print("Number of days is 28");
elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    print("Number of days is 31");
else :
    print("Number of days is 30");
 #13..to count total number of notes in given amount
 m=int(input("Enter your payroll : "))
n=[5000,2000,1000,500,100]
t={}
for i in n:
    x=m//i
    t[i]=x
    m=m-i*x
print(t)
#14..to input angles of a triangle and check whether the triangle is valid or not
a=int(input("enter first angle"))
b=int(input("enter second angle"))
c=int(input("enter third angle"))
if(a+b+c==180 and a!=0 and b!=0 and c!=0):
    print("triangle can be formed")
else:
    print("cannot form trianle")   
#15..to input all sides of triangle and check whether triangle is valid or not
a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if(a+b>c or b+c>a or c+a>b):
    print("triangle can be form")
else:
    print("triangle cannot be form")
#16..to check triangle is equilateral isosceles or scalene triangle
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if(a!=b!=c):
    print("scalene triangle")
elif(a==b !=c or a==c !=b or b==c !=a):
    print("isosceles triangle")
else:
    print("equilateral triangle")
#17..to print all roots of quadratic equation
print("Equation: ax^2 + bx + c ")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=b**2-4*a*c
d1=d**0.5
if(d<0):
    print("The roots are imaginary. ")
else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("The first root: ",round(r1,2))
    print("The second root: ",round(r2,2))
#18..program to calculate profit or loss
cp=float(input("Enter the Cost Price : "));
sp=float(input("Enter the Selling Price : "));
if cp==sp:
    print("No Profit No Loss")
else:
    if sp>cp:
        print("Profit of ",sp-cp)
    else:
        print("Loss of ",cp-sp)
#19..program to input marks of five subjects physics chemistry biology mathematics and computer calculate percentage and grade according to following
"""percentage >=90% :grade A
percentage >=80% :grade B
percentage >=70% :grade C
percentage >=60% :grade D
percentage >=40% :grade E
percentage < 40% :grade F"""
physics=int(input("enter marks of physics"))
chemistry=int(input("enter marks of chemistry"))
biology=int(input("enter marks of biology"))
maths=int(input("enter marks of maths"))
computer=int(input("enter marls of computer"))
totalmarksl=physics+chemistry+biology+maths+computer
percentage=(totalmarks*100)/500
print(percentage)
if(percentage>=90):
    print("grade A")
elif(percentage>=80):
    print("grade B")
elif(percentage>=70):
    print("grade C")
elif(percentage>=60):
    print("grade D")
elif(percentage>=40):
    print("grade E")
elif(percentage<40):
    print("grade F")    
#20..to input basic salary of an employee and calculate its gross salary according to following 
"""basic salary<=10000: HRA=20%,DA=80%
basic salary<=20000:HRA=25%,DA=90%
basic salary>20000:HRA=30%,DA=95%"""
basicpay=int(input("enter basic pay"))
if(basicpay<=10000):
    hr=(basicpay*20)/100
    da=(basicpay*80)/100
    ta=basicpay+hr+da 
    print(ta)
elif(basicpay<=20000):
    hr=(basicpay*25)/100
    da=(basicpay*90)/100
    ta=basicpay+hr+da 
    print(ta)
elif(basicpay>20000):
    hr=(basicpay*30)/100
    da=(basicpay*90)/100
    ta=basicpay+hr+da 
    print(ta)
#21..in input electricity unit charges and calculate total electricty bill according to the given condition:
"""for first 50 units rs. 0.50/unit
for next 100 units rs. 0.75/unit
for next 100 units rs. 1.20/unit
for unit above 250 rs. 1.50/unit
an additional surcharge of 20% is added to the bill"""
a=int(input("enter units"))
if(a<=50):
    u=a*0.5
elif(a<=150):
    u=50*0.5(a-50)*0.75
elif(a<=250):
    u=50*0.5+100*0.75+(a-150)*1.2
elif(a>250):
    u=50*0.5+100*0.75=100*1.2+(a-250)*1.5
c=(u*20)/100
ta=u+c 
print(ta)
#22..a man has certain apples
a=int(input("enter total number of apple"))
if(a%7==0 and a%6==1 and a%5==1 and a%4==1 and a%3==1 and a%2==1):
    print(a)
else:
    print("no of apples are wrong")
#23..an automobile
v=int(input("enter total no. of vehicles"))
w=int(input("enter total no. of wheels"))
tw=(2*v)-(w/2)
fw=(w/2)-v 
print("tw=",tw)
print("fw=",fw)