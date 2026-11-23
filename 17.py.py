'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  'n'  be  6

What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''

x = float(input("enter the number be n  = "))
a = 0
b = 0
while x<=n:
    a b = b ,a+b
    print(b)
print("enter the integer or float")
#================================================================================================
# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)  # for a  each  for loop we cannot write separate element and index in the loop 


a = eval(input("enter the elements = "))
i = 0
for x in range(a[i]):
    print( x,a[i])
    i = i+1
#===========================================================================================================================
#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

'
a = eval(input("enter the elements = "))
i = -1
for x in range(a[i]):
    print(x,a[i])
    i = i-1

#===============================================================================================================================
'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable) # not possiblr in with for each loop 
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
small = min(len(a),len(b))
for x in range(small):
    c.append(a[x]+b[x])
print(c)
#=================================================================================================================================
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

a = eval(input("enter the number of elements = "))
print("Indexed for loop")
for x in range(2,5,1):
    print(x)
#=======================================================================================================================================
#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):#a :   [11, 21, 16, 19] #b :   [10, 20, 15, 18]
        a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)
#=======================================================================================================================================
'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 +  .....

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n
'''

n = int(input("enter the number of n th term = "))
sum = 0.0
for i in range(1, n+1):
    sum =  sum + 1.1*i
print(f" sum ={sum:.2f}")

#========================================================================================================================================
'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0  + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20
'''

n = int(input("enter the sum of first 20 even number = "))
sum = 0
for x in range(1,n+1):
    sum = sum+2*x
    print(sum)m
#======================================================================================================================================
'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + 2 * 1 - 1 + 2 * 2 - 1 + 2 * 3 - 1 +  .... + 2 * 20 - 1

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20
'''

n = int(input("enter the sum of first 20 even number = "))
sum = 0
for x in range(1,n+1):
    sum = 2*x-1
    print(sum)
#=====================================================================================================================================
'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
'''
n = int(input("enter the sum of first 20 even number = "))
sum = 0
for x in range(1,n+1):
    sum = 2*x-1
    print(sum)
#=====================================================================================================================================
'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2  spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''

n = int(input("enter the how many lines you want = "))
s = n-1
for i in range(1,n+1):
    print(' '*s,end=' ')
    print('*' *(2*i-1))
    s = s-1

#========================================================================================================================================
''''
Write  a  program  to  evaluate  expression  like  calculator

Input :  3 + 4 * 5 - 6 / 2 =

What  is  the  output ? --->  14.5

Iteration         a          op        b        result
------------------------------------------------------
     1                 3           +         4           7
     
	 2                7           *         5           35
	 
	 3                35         -          6           29
	 
	 4                29         /          2           14.5
	 
	 5                14.5      =          ----         -----
--------------------------------------------------------
Hint1:  Use  while  loop

Hint2:  Read  whole  expression  as  a  string
'''
str = input('enter any expression terminated  by  =  :  ')  #  Reads  expression  into  a  str  object
a = eval(str[0]) # Operand1
op = str[1]  # Operator 
i = 2  #  Index  of  operand2
while  op  !=  '=':  #  Execute  loop  until  op  is  '='
	b = eval(str[i]) # Operand2
	match  op:  #  Executes  expression  based  on  op
		case '+':  
				a += b  
		case '-':  
				a -= b            
		case '*':  
				a *= b                           
		case '/':  
				a /= b;
	# End  of  match                    
	i += 1  #   Index  of  next   operator
	op = str[i] # Next  operator
	i += 1 # Index  of  next  operand
#  End  of  while  loop    
print('Result : ' , a)
#============================================================================================================================================
'''
There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

								n = 21
   Iteration     user         computer             n
-------------------------------------------------------------
        1               3                   2                   n = 21 - 5 = 16
        
		2               1                   4                   n = 16 - 5 = 11
		
		3               2                   3                   n = 11 - 5 = 6
		
		4               4                   1                   n = 6 - 5 = 1
---------------------------------------------------------------
Hint: Use while  loop
'''
n = 21
while  n > 1:  #  Execute  loop   until  'n'  becomes   1
	pick = int(input('How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  '))  
	while  pick < 1  or  pick > 4:  #  Execute  loop  until  user  input  is   valid
		pick = int(input('Input  can  not  be >  4  nor  <  1,  Reenter  :  '))		
	# End  of  inner  loop
	print(F'Computer  picks  {5 - pick}  matchsticks')
	n = n - 5  #  Modifies  value  of  'n'  to  avoid  infinite  loop
# End  of  while  loop	
print('You  have  lost  the  game  and  Computer  wins')

