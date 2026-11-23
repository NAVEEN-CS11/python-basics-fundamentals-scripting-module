'''
Tricky  program
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units	(>= 700)		   	    Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
#==========================================================================================================
x = eval(input("enter the electricity cousumed by the household= "))
match x//100:
    case 0:
        cost= 100*3.00
    case 1:
        cost = 100*3.00+(x-100)*3.50
    case 2 | 3:
        cost = 100*3.00+100*3.50+(x-200)*4.00
    case 4|6:
        cost = 100*3.00+100*3.50+200*4.00+(x-500)*4.50
    case 7:
        cost = 100*3.00+100*3.50+200*4.00+500*4.50+(x-900)*5.00
    case _:
        cost = 100*3.00+100*3.50+200*4.00+500*4.50+x*5.00
print("cost",cost)
#================================================================================================================
'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  'x'  be   10
What  are  the  outputs  ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

1) What  is  the  formual  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formual  for  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
#=============================================================================================================
# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop
#=============================================================================================================
# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x , end = '\t')
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x , end = '\t')
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x , end = '\t')
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , end = '\t')
print()
#================================================================================================================
# Find outputs  (Home  work)
a = {'AB' : 20 , 'CD' : 40 ,  'EF' : 60}
for  x , y  in   a . items(): 
	print(x , y , sep = '...') 
print()	
for  x ,  y  in   a:    
	print(x , y , sep = '...') 
print()	
for  x , y  in  {'AB' : 20 ,  'CDE' : 40 ,  'FGHI' : 60}: 
	print(x , y , sep = '...') 
for  x , *y  in  {'AB' : 20 ,  'CDE' : 40 ,  'FGHI' : 60}:  
	print(x , y , sep = '...')
#================================================================================================================
# Identify  error  (Home  work)
for  x  in   123:  # error its an integer
        print(x)
#============================================================================================================
# Find  outputs  (Home  work)
for  x   in   ():
        print(x)
for  x   in  []:
        print(x)
for  x   in   {}:
        print(x)
for  x   in   set():
        print(x)
for  x   in   '':
        print(x)
'''for  x  in  range(10 , 10): #
	print(x)
for  x  in   range():
	print(x)
for  x  in   (25):
	print(x)'''   #error
#====================================================================================================================
'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  ---> 1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
'''
2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
'''
#=================================================================================================================
'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  ---> 1 , 3 , 5 , ....  39
2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
'''
  # x = int(input("enter the natural number start from 1 To..n = "))
for b in range(2,41,2):
    print(b,end = " ")
  

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
'''
#====================================================================================================================
'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n  #   x = int(input("enter the natural number start from 1 To..n = "))
for b in range(1,x+1,2):
    print(b,end = " ")
  
'''
#======================================================================================================================
'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1
'''
for i in range(10, 0, -1):
    print(i, end=" ")
#========================================================================================================================
'''
Write  a  program  to  print  upper  and  lower  case  alphabets

1) What  is  chr(65)  ?  --->  A

2) What  is  chr(90)  ?  --->  Z
 
3) What  is  chr(97)  ?  --->  a

4) What  is  chr(122)  ?  --->  z
'''

for ch in range(65,91):
        print(chr(ch),end = " ")
for ch in range(97,123):
    print(chr(ch),end = " ")
 
#===========================================================================================================================
# Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
                print(i ,  j)  #1 1

1 1	
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye
	print('Hello')
print('Bye')
#========================================================================================================================
# Find  outputs
for i in range(3):
	for i in range(5): #0001020304||1011121314||2021222324 = 4 4 4 			
		pass
	print(i)
x = float(input("enter the value = "))
a =0
b =1
while x<=10:
    a =b
    b = a+b
    print(b)
print("bye")
