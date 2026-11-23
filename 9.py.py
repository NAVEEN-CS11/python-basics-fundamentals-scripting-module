#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')  #  {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') #  {{X}}
print(F'{{{{{x}}}}}') #  {{25}}
print(F'{{{{{{x}}}}}}')  # {;{{X}}}
print(F'{{{{{{{x}}}}}}}')  # {{{x}}}
print(F'{{{{{{{{x}}}}}}}}')  # {{{{X}}}}


'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  ---> 'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  ---> Value   of  'x'

3) How  many  braces  are  printed  in  the  output ?  ---> Number  of  braces  //  2
'''
#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)                       # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b)                        # Hyd is 'green' city
c = 'Hyd  is  \'green\'  city'
print(c)                          # Hyd  is  'green'  city
print('Hyd  is  ' green  '  city')    # error

Write  a  program  to  determine  area  and  circumference  of  circle

1) What  is  the  input ?  ---> Radius  

2) What  are  the  outputs ? ---> Area  and  circumference

3) What  is  the  area  of  circle ?  ---> 3.14159 * r ^ 2

4) What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * r'''

import  math
try:
	r = float(input('Enter  radius  of  circle :  '))  #   Reads radius  to  object  'r'
	area = math . pi * r ** 2
	cir = 2 * math . pi * r
	print(F'Area :  {area:.2f}')
	print(F'Circumference :  {cir:.2f}')
except:
	print('Input  should  be float  (or)  integer')

