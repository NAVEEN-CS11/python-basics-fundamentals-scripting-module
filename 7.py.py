# Find  outputs
#How  to  import   kw  list ------> # from keyword import kwlist
#How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]------> # print(kwlist)
How  to  print  number  of  keywords  i.e.  35 #-----> print(len(kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'> #-----> print(type(kwlist))
print(keyword . kwlist)  # it is an error 
#  Find  outputs  (Home  work)
How  to  import   keyword  module  # import keyword
How  to  print  kwlist   # -----> print(keyword.kwlist)
How  to  print  number  of  keywords -----> print(len(keyword.kwlist))
How  to  print  type  of kwlist ------> print(type(keyword.kwlist))
print(kwlist) # its an error 
# How  to  read  float  input ?
x = float(input('Enter  float  number  :  ')) # 10.8
print(type(x))  # class float
print(x)  # 10.8
 




'''
Input     What  does  input()   read      What  does  float(input())  return
---------------------------------------------------------------------------------------
 10.8      '10.8'                              float('10.8') is 10.8
 25          25                                 float('25') is 25.0
 3+4j
 True
-----------------------------------------------------------------------------------------
'''
# Identify  the   issue ?
x = bool(input('Enter  Boolean  input  :  '))
print(type(x))
print(x)


'''
Input           input()  reads     bool(input())  returns
--------------------------------------------------------------------------
 True
 False
 <Enter key>
 25
 10.8
 Hyd
 <Space  bar>
-----------------------------------------------------------------------------------
'''
# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x))
print(x)


'''
Input       input() reads      complex(input())  returns
------------------------------------------------------------------------
3+4j
4j
j
25
10.8
True
Ten
3+j4
3+4i     
4j+3
---------------------------------------------------------------------------
'''
# Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))
hyd = 'Sec'
print(eval('hyd'))
sec = '25'
print(eval('sec'))
print(eval(sec))
cyb = 10.8
print(eval('cyb'))
print(eval(cyb))
#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))
#  Find  outputs  (Home  work)
print(bool('False'))
print(eval('False'))
print(bool(''))
print(eval('  ""  '))
print(eval(''))
print(eval('  " "   '))
print(eval(' '))
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))
print(x)


'''
Input                             input() reads                     eval(input())  returns
--------------------------------------------------------------------------------------
  25
  10.8
  3+4j
  False
  None
  Hyd
  'Hyd'  
  [25 , 10.8 , 'Hyd']
---------------------------------------------------------------------------------------------
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')  #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')
print(a , b , c , sep = '---')
print(a , b , c , sep = '\n')
print(a , b , c)
print(a , b , c , separator = ':')
# Find outputs  (Home  work)
print('Hyd')
print()
print('Sec')
print()
print('Cyb')
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)
#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)
print(type(b))
x = 10.8
y = '%i'  %x
print(y)
print(type(y))
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)
print(type(n))
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)
print('%10.3f'  %a)
print('%.2f'  %a)
print('%.6f'  %a)
print('%f'  %a)
print('%g'  %a)
# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)
print('%-7s'  %a)
print('%2s'  %a)
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print(a)
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print('%l'  %a)
print(a)
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))
print('%i    %g    %s'    %(a , b , c))
print('%s    %s    %s'  %(a , b , c))
print('%d    %g    %s'  , a , b , c)
print('%d    %g      %s'   a , b , c)
print('%d    %g    %s'  ,  %(a , b , c))
print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)
#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)
print(type(y))
x = 10.8
y = F'{x}'
print(y)
print(type(y))
x = [10,20,30,40]
y = F'{x}'
print(y)
print(type(y))
#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')
print(F'{x =}  \t   {y =}   \t  {z =}')
# Find  outputs
x = 9247
print(x)
print(F'{x}')
print(F'{x:7}')
print(F'{x:07}')
# Find  Outputs  (Home  work)
x = 123.9274
print(x)
print(F'{x:8.2f}')
print(F'{x:9.1f}')
print(F'{x:10.3f}')
print(F'{x:.2f}')
print(F'{x:.6f}')
print(F'{x}')
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')
print(F'{{x}}')
print(F'{{{x}}}')
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')