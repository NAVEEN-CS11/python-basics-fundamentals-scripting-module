# Find  outputs (Home  work)
a = print('Hyd') , print('Sec') ,  print('Cyb')  # Hyd <next line> sec<next line> Cyb print always returns None but only one none
print(type(a)) #  < class 'tuple'>
print(a)  #  None
print(len(a)) #  3
#======================================================================================
#========================================================================================
#  Find  outputs
print({10 , 20}  |  {30 , 20}) # | its is used for only set  output is { 10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10:'Hyd', 20 : 'Sec',30 : 'Cyb' ,20 : 'Vja'}
print(range(4) | range(5)) # range cannot be add with | so it can be separate with ,
print([10 , 20]  |  [30 , 20])  # list cannot be | it error
#=============================================================================================
#============================================================================================
#  Relational  operators  demo  program (Home  work)
print(9 >= 5) #   True
print(9 >= 9)  #  True
print(9 >= 12)  #  False
print(6 <= 8)   # True
print(6 <= 6)   # True
print(6 <= 4)   # falsex
print(9 != 7)   # True
print(6 == 8)   # True
print(True  >  False) # True 
print(3 + 4j == 3 + 4j) # True
print(3 + 4j == 5 + 6j) # True
print(3 + 4j != 5 + 6j) # True
print(10 == 10.0) # True
print(3 + 4j >  3 + 4j)  # error
#=============================================================================================
#============================================================================================
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')      #  'm'  >  'j'  is  True
print('Rama'  <  'Sita')         #   'R' < 'S'  is  True
print('Hyd'  ==  'Hyd')          #     'H' == 'H' is True
print('Rama'  <=   'Ramana')     #  True
print('Rama  Rao'  >=  'Rama')   # True
print('Hyd'  != 'Sec')           # True
print('HYD'  <   'hyd')          # True
#=============================================================================================
#============================================================================================
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30) #   True
print(10 >= 20 < 30) #  False
print(10 < 20 > 30)  #  False
print(1 < 2 < 3 < 4)  # True
print(1 < 2 > 3 > 1)  # False 
print(4 > 3 >= 3 > 2)  #   True
#=============================================================================================
#============================================================================================
#  and  operator  demo  program
print(True  and  False)  #  False
print(False  and  True)  #  False
print(False  and   False) #  False
print(True  and  True)  #  True
print(10  and  20)  #   20
print(0  and  20)  #  0
print(-25  and  0)  # 0
print(''  and  25)  # 
print(6j  and  'Hyd') # Hyd  and operator opt 2 is 
print(0j  and  'Sec')  # 0j
print('Hyd'   and  10.8) #  10.8
print(10  and  20  and  30)  # 30
#=============================================================================================
#=============================================================================================
# or  operator  demo program
print(True  or  False)  #  True
print(False  or  True)  #  True
print(True  or  True)  #  True
print(False  or   False)  #  False
print(10  or  20)  #  10
print(0   or  20)  #  20
print(-25  or  0)  # -25
print(''  or  35)   # 35
print(6j  or  'Hyd') # 6j
print(0.0  or  3 + 4j) # (3+4j)
print('Hyd'   or   10.8) # 'Hyd'
#=============================================================================================
#=============================================================================================
# not  operator  demo  program
print(not  True)  #  False
print(not  False)  #  True
print(not  25) # False
print(not  0)  # True
print(not  'Hyd') # False
print(not  '') # True
print(not  -10) # False
print(not  not  'Hyd') # True


'''
not  operator
----------------
1) What  does  not  operator  do ?  ---> Complement  operation

2) Is  not  a  unary  operator  ?  ---> Yes  becoz  it  has  single  operand
    What  about  and ,  or ? --->  Binary  operators  becoz  they  have  two  operands

3) What  is  the  associativity  of  unary  operators ?  ---> Right  to  Left
    What  is  the  associativity  of  binary  operators ?  ---> Left  to  Right  except  for  **
'''
#=============================================================================================
#=============================================================================================
# Tricky  program
#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)  # True
print(not(6 < 4  or  9 >= 5  and  6 != 6))  # True
#=============================================================================================
#=============================================================================================
#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) # 25 assigning operator
b =  a  # here a is assign to b and reference of the a object is assign to b reference
print(b) # 25
print(a  is  b)  # True because both hold same reference same reference object
x = 4
y = 5
z = x + y * 6  # here do first high piority then 5*6 = 30 + 4  =  34
print(z)  # 34
#25 = a  here its is not possible because 25 is int value and object is right side but not on left side and imutable
#a + b = x + y # its not possible there is = is operator not ==
#=============================================================================================
#=============================================================================================
# Find outputs (Home work)
a = b = c = 25
print(id(a)) #  a refrence of object 25 int type is 2725698
print(id(b)) # b refrence of object 25 int type is 2725698
print(id(c)) # c refrence of object 25 int type is 2725698
print(a , b , c) # ( 25 25 25)
#=============================================================================================
#=============================================================================================
# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) # 25
print(y) # 10.8
print(z) # Hyd
#=============================================================================================
#=============================================================================================
# Find outputs (Home work)
a , b , c = 4 , 4 , 5
print(a , id(a))  # 3 id of reference is 1234
a *= b + c  # 36 And Id of reference is 123
print(a , id(a)) # # 36 And Id of reference is 
#=============================================================================================
#=============================================================================================
# Find outputs (Home work)
a = 20
print(a , id(a)) #  20 123
a %= 3 + 2 * 4 
print(a , id(a)) # here a = 20 and 3+2*4 = 11 so %= is 20 - 11 = 9 and reference is 124
# Find outputs (Home work)
a = 3
print(a , id(a)) # a = 3 and id (a ) is 12345
a **= 4   # a = 3 so power of 3^4 is 3*3*3*3
print(a , id(a)) # 81 Id(a) is 1234567
# Tricky  program
#  Find  outputs
a = [10 , 20 , 30]
b = [40 , 50 , 60]
print(a , id(a)) # a = [10 , 20 , 30] id(a) is 123432
a += b   # here[10, 20, 30, 40, 50, 60]
print(a , id(a)) # [10, 20, 30, 40, 50, 60] id(a) is 897566
#=============================================================================================
#=============================================================================================
#  Tricky  program
# Find  outputs
a = [10 , 20 , 30]
b = [40 , 50 , 60]
print(a , id(a)) # [10, 20, 30]   refre of a of object is 2742 
a = a +  b    #  additional operator
print(a , id(a)) #[10, 20, 30, 40, 50, 60] 27424
#  Tricky  program
# Find  outputs
a = (10 , 20 , 30)
b = (40 , 50 , 60)
print(a , id(a)) # (10, 20, 30) 274246373539264 its in tuple
a += b   # additon
print(a , id(a)) # (10, 20, 30, 40, 50, 60)  refrence of object  a tule 27424
#  Tricky  program
# Find  outputs
a = (10 , 20 , 30)
b = (40 , 50 , 60)
print(a , id(a))  (10, 20, 30, 40, 50, 60) 27424
a = a +  b # additonal
print(a , id(a)) # (10, 20, 30, 40, 50, 60) 2742463
#=============================================================================================
#=============================================================================================
# Identity operators demo program
a = 25
b = 25
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True
# Find outputs (Home work)
a = 25
b = 25.0
print(a is b) # False its a float and int type
print(a is not b) # True
print(a == b) #  True
# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # True
print(a  is  not  b) #  False
print(a == b) # True
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) # False
print(x  is  not  y) # True
print(x == y) # True
print() # empty
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) # True because its a tuple which can access same element
print(m  is  not  n) # false
print(m == n) # True
#=============================================================================================
#=============================================================================================
# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)   # False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) # True  
m = range(5)
n = range(5)
print(m == n) # True
# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  # False 
print(a  ==  b) # Here False because List(mutable) and Tuple(immutable)
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True 15 is present
print(19 in list) #  False 19 is not prsent
print(14 not in list) # True 
print(15 not in list) # False 
s = 'Hyd is green city'
print( 'is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) #True
print('gre' in s) #True
print('yd i' in s) # True
print('' in s) # True
print('' not in s) # False
#=============================================================================================
#=============================================================================================
#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a = +25  = 25
#print(a++)  #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1) = a + 1 = 25 + 1 = 26
print(--a)  # 25
#print(a--) # its an error in python there  is no decrement --
print(a--1) # 26
print(-a)  # -25
print(+-a)  # -25
print(-+a)  # -25
print()
#  Semicolon  demo  program
print('One'); # one
print('Two'); # Two
print('Three'); # Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb')  # Hyd < next line > Sec  < next line > Cyb
# pow()  function  demo  program
import  math
print(math . pow(2 , 3)) # its 2^3 = 8.0
print(math . pow(-2 , -3)) # its is -0.125
print(math . pow(10 , -2)) # 0.01
print(math . pow(4 , math . pow(3 , 2))) # 262144




'''
pow()  function
-----------------
1) What  does  pow(a , b)  do ?  ---> Returns  a ^ b

2) What  is  the  result  of  pow(5 , 2) ?  ---> 25.0  but  not  25

3) In  other  words,  pow()  function  returns  float  result

4) Where  is  pow()  function  defined ?  ---> In  math  module

5) What  are  the  two  ways  to  obtain  a ^ b ? --->  a ** b  and  pow(a , b)

6) How  to  call  function  of  a  module ?  --->  module . function(args)

7) Can  a  module  be  used  without  import ?  ---> No

8) What  is  the  pre-requisite  to  use  a  module ?  ---> It  needs  to  be  imported

9) pow(a , pow(b , c))
    What  is  a  nested  call ?  --->  A  function  call  inside  another  function  call					
    Which  call  is  executed  first ?  --->	Inner  call  is  executed  before  outer  call
    What  is  the  result  ?  ---> a ^ b ^ c	

10) math . pow(a , b , c)
      Is  it  valid ?  ---> No  becoz  pow()  function  expects  2-args  but  3-args  are  passed
'''
#============================================================================================================
#============================================================================================================
# sqrt()  function  demo  program
import  math
print(math . sqrt(25))  # 5.0
print(math . sqrt(10))  # 3.16
print(math . sqrt(6.25)) # 2.5  
print(math . sqrt(True))  #1.0
#print(math . sqrt(3+4j)) # must be real but not a complex numbers
print(math . sqrt(math . sqrt(256)))  # 4.0
print(math . sqrt(math . pow(3 , 4)))  # 9.0
#print(math . sqrt(-16)) its sqrt cannot be negative
#print(sqrt(49))   error brcause it does not a module to access its not defind
# fabs()  function  demo   program
import  math
print(math . fabs(-10))  # 10.0
print(math . fabs(-25.6))  #25.6
print(math . fabs(20))  # 20.0
print(math . fabs(35.8))   # 35.8
#print(fabs(-25)) its not defind the import floder
# floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10  floor means before value we have to enter
print(math . ceil(10.8))  #  11   ceil means after next value we have to enter
print(math . floor(25.0))  #25 
print(math . ceil(25.0))  #25 
print(math . floor(-3.5)) #-4
print(math . ceil(-3.5)) # -3
print(math . floor(-9.0)) # --9
print(math . ceil(-9.0)) # -9
print(math . floor(25.1)) #25
print(math . ceil(25.1)) # 26
print(floor(3.5)) # not defined the math. to access the floor
print(ceil(3.5))  ## not defined the math. to access the ceil
#=========================================================================================
#============================================================================================
import  math
print(math . exp(1))
print(math . exp(2))
print(math . exp(0))
print(math . exp(-2))














