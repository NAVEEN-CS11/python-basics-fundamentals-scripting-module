('''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  ---> 2 * (length + breadth)
'''
length = float(input("enter the length of the rectangle "))
width = float(input("enter the width of the rectangle"))
areaR= length*width
perimeterR = (2,(length+width))
print('area of rectangle:',areaR:)
print('perimeter of rectangle:', perimeterR)
#====================================================================================
#==================================================================================
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
radius= float(input("enter the radius of the sphere"))
volume = (4 / 3) * math.pi * (radius ** 3)
print(f"volume:{volume:.2f}")
/*===================================================*/
enter the radius of the sphere 20
volume:33510.32
#==================================================================================================
#==================================================================================================
'''(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
import math
principle = float(input("eneter the principle amount= "))  
time = float(input("enter the time ="))
rate = float(input("enter the rate of interest="))
simple = (principle*time*rate)/100
compound = principle * (1  +  rate  /  100) ** time -  principle
print("simple interest: " ,simple)
print(" compound interest : ", compound)
#==================================================================================
eneter the principle amount= 20000
enter the time =3
enter the rate of interest=5
simple interest:  3000.0
 compound interest :  3152.500000000003
#===============================================================================
#==================================================================================
'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j

What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                          = (15 - 18j + 20j + 24)  / (25 + 36)											   
																          =  39 / 61 +  2j/61
'''
#==================================================================================================
first = complex(input("enter the complex number = "))
second = complex(input("enter the second complex number= "))
sum = first + second
difference = first - second
product = first* second
division = first/second
print("sum = " ,sum)
print("difference = ", difference)
print("product= ", product)
print("division= ", division)
#================ANSWER=======================
enter the complex number = 3+4j
enter the second complex number= 5+6j
sum =  (8+10j)
difference =  (-2-2j)
product=  (-9+38j)
division=  (0.6393442622950819+0.03278688524590165j)
#================================================
#======================================================
'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  ---> 17 
What  is  the  difference ?  ---> 3
What  is  the  product ?  --->  70
What  is  the  quotient ?  ---> 1.42
What  is  the  remainder ?  ---> 3
What  is  the  largest  number ?  ---> 10
What  is  the  smallest  number ?  ---> 7
What  is  the  sqrt  of  1st  input ?  --->  3.16
What  is  the  result  of  power?  --->  10 ^ 7 = 10000000
What  is  the  gcd  of  2  numbers ?  --->  1
What  is  the  factorial   of  1st  input ?  ---> 10!
'''
import math
a = int(input("enter the value of a = "))
b = int(input("enter the value of b  = "))
c = a+ b
d = a-b
e = a*b
g = a/b
f = a%b
print( f"{a} + {b} = {c}")
print( f"{a} - {b} = {d}")
print( f"{a} * {b} = {e}")
print( f"{a} / {b} = {g:.2f}")
print( f"{a} % {b} = {f}")
print(F"{max(a,b)}")
print(F"{min(a,b)}")
print(F"{math.sqrt(a):.2f}")
print(F"{a**b}")
print(F"{math.gcd(a,b)}")
print(F"{math.factorial(a)}")
#===========Answer==============
enter the value of a = 10
enter the value of b  = 7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.43
10 % 7 = 3
10
7
3.16
10000000
1
3628800
#=====================================================
#======================================================
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
x = (input("enter the number= "))
y = (input("enter the number= "))
z = x 
x = y 
y = z
print("x =", x)
print("y=", y)
#==============Answer======================================================
enter the number= 10
enter the number= hyd
x = hyd
y= 10
#===============================================================================
#====================================================================='''
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  reference

Hint: One  addition  and  two  subtractions

x = 25
y = 10
'''
x = int(input("enter the number= "))
y = int(input("enter the number= "))
x = x+y 
y = x-y 
x = x-y

print("x =", x)
print("y=", y)
#===========================================================================================
#====================================================================================
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   ---> 20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   ---> 'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''

import  math
a = eval(input("enter the number")
b = eval(input("Enter the number")
c = eval(input(" Enter the number")
x = a if a>b and a>c else b if b>c else c
print(F"{x= }")
#=========================================================================================
#======================================================================================
'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  ---> >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''

a = eval(input("enter the number"))
b = eval(input("Enter the number"))
x = a if a>=b else b
print(F"{x= }")
#======================================================================================
#======================================================================================
'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
x = eval(input("enter the number"))
a = 1
b = -1
c = 0
num = a if x>=a else b if b>=x else c
print(F"{num= }")
#======================================================================================================
#======================================================================================================
'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2

2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''
a = float(input("enter the number"))
if(a/2):
    {
        print("it is divisible")
    }
else:
   {
    print("its not divisible")
   }    
#======================================================================================================
#======================================================================================================
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
   0 - Zero
   1 - One
   2 - Two
   ....
   9 - Nine
   10 - Invalid'''
x = eval(input("enter a number"))
if(x==0):
    {print("zero")}
if(x==1):
 {
    print("one")
 }
if(x==2):
    {
        print("two")
    }
if(x==3)
     {
        print("Three")
     }
if(x==4)
      { 
         print("four")
      }
if(x==5
      {
        print("five)
      }
else:
    {print("its an invalid")}
#=================================================================================
#================================================================================
# Identify  error
else:
		print('else  suite')  # no without if statement wecannot write a else statement
print('Outside')
# Identify  error
if  9 > 5
	print('Hello')  # after writing of if comdition there should be end with :
print('Bye')
# Identify  error
if  9 > 12:
	print('Hyd')  # after writing of else statement there should be end with :
else
	print('Sec')
# Identify  error
if  (10,20,15):  # in if  should have condition there  is given tuple 
print('Hyd')
else:
print('Sec')
# Identify  error
if  ():
			print('Hyd')  # there is no condition for if condition to excute the statement
	else:
					print('Sec')
print('Bye')
# Identify  error
if  { }:                 #-------------> its an invalid syntax for if condition       
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
	print('Four')   # here indentation should be wrong expect if and else got else
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#===================================================================================================
#===================================================================================================
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
x = int(input("enter the number"))
if(x/2==0)
   {
     print("its an even number")
    }
else
    {
      print("Its an odd number")
    }
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')

#----------answer----------
x = input("enter the number = ")
if(x==x):
    {
        print('Hyd'),
        print('Sec'),
        print('Cyb')
    }
else:
    {
        print('One'),
        print('Two'),
        print('Three')
    }
print('Bye')
#======================================================================
#===============================================================================
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#===============================================================================
#====================================================================================
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
month  = int(input("enter the which month = ")
# Find outputs  (  calendar Home  work)
import calendar
#month = int(input("enter the number= "))
year = int(input("enter the number year="))
print(calendar.calendar( year))

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
   0 - Zero
   1 - One
   2 - Two
   ....
   9 - Nine
   10 - Invalid'''
x = eval(input("enter a number"))
if(x==0):
    {print("zero")}
if(x==1):
 {
    print("one")
 }
if(x==2):
    {
        print("two")
    }
if(x==3)
     {
        print("Three")
     }
if(x==4)
      { 
         print("four")
      }
if(x==5
      {
        print("five)
      }
else:
    {print("its an invalid")}
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? ---> Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  ---> Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
#===============================================================================================
#=====================================================================================================
'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
#==================================================================================================
#==============================================================================================

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? ---> 1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  ---> (temp - 32) / 1.8
'''
ch =int(input("press 1 in temperature in celsius or press 2 for  temperature in farenheit)
if ch==1
  c = float(input("enter the temperature celsius")
   print("farenheit:",1.8*c+32)
elif ch==2
  f = float(input("enter the temperature Farenheit")
    print(F"celsius{(f-32)/1.8:.2f}")
else:
    print("invallid input")
#==================================================================================================
#=================================================================================================
'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  ---> 'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  ---> Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  ---> 'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  ---> 'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif  .... else
'''

x,y= eval(input("enter the values of x= "))
#y= eval(input("enter the values of y= "))
if x>0 and y>0:
	print("its an first quardant")
elif x<0 and y>0:
	print("its an second Quardant")
elif x<0 and y<0:
	print("its an third Quardant")
elif x >0 and y<0:
	print("its an  fourth Quardant")
elif x!=0 and y==0:
	print("x axis")
elif x==0 and y!=0:
	print("y axis")
else:
	print("origin")
#==================================================================================================
#==================================================================================================
# Find outputs  (  calendar Home  work)
leap = int(input("enter the number= "))
if leap%4==0 and leap%100!=0 or leap%400==0:
    print("its an leap year")
else:
    print("its not a leap year")
#=======================================================================================================
#=======================================================================================================