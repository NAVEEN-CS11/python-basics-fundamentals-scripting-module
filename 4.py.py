#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a)) #  class list
print(id(a))   # 12345  address of the object list
print(len(a))   # length of the string is 8
a[2] = 'Sec'    #  Hyd is  Sec for index of 2   [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)  #  [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])#   ['Sec' , True , 3 + 4j]
#======================================================================================================
#======================================================================================================
# append()  and  remove()  methods  (Home  work)
a = [ ]  # its is an empty with no aruument
print(a)  #   its an reference towards reference of a
a . append(25)  # its add 25 to the a  reference object
a . append(10.8) #its add 10.8 to the a  reference object
a . append('Hyd') #its add Hyd to the a  reference object
a . append(True)  #its add  True to the a  reference object
print(a)  [ 25,10.8,'Hyd',True]
a . remove('Hyd')  # remove Hyd is [ 25, 10.8,True]
print(a)
#a . remove('25') # its element is not present 
print(a) # [ 25, 10.8,True]

#=========================================================================================================
#=========================================================================================================
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # [25 , 10.8 , 'Hyd']
print(id(a)) # address of list object  a
print(a * 3) # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2) #  [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1)  #[25 , 10.8 , 'Hyd']
print(a * 0)  # its an empty list with no argument 
print(a * -1) # its an empty list with no argument
print(a * 4.0)# list ct cannot having float type only int can access it
a = a * 3 # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a)
print(id(a)) # address of list object
a = [25] 
print(a , id(a)) #[25] 123894567
 #print(a * a) its not possible because non int cannot be a list
#===================================================================================================
#==================================================================================================
# list()  function  demo  program
a = list('Hyd')  # its a list and a reference to object
print(a) # ['H','y','d']
print(type(a))  # its a list type object
print(len(a))  # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10, 20, 15, 18]
print(list(range(5))) #[0, 1, 2, 3, 4, 5,]
print(list(25)) #  25 is not  present in the list


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  ---> Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  ---> No  becoz  list()  function  expects  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''
#===================================================================================================
#==================================================================================================

# Find  outputs
a = [ ]
print(type(a)) # its a list object 
print(a) # []
print(len(a)) # 0
b = list() 
print(b) # []
print(len(b)) # 0
#===================================================================================================
#==================================================================================================
# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # list[2:7:1] --->[(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ]) # list [0:8:1] ---->[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:])  #  list[0 : 8 : 1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # list[-1:-9:-1] ---> list from index -1 to -8 in steps of -1 ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  # list [0:8:2] ----> list from index 0 to 7 in steps of 2 is [25, (3+4j), True, 10.8]
print(list[1 : : 2])  # list [ 1: 8 : 2] ---> list from index  1 to 7 in steps of 2 is [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 : -9 : -2]  --->  List  from  indexes  -1   to  -8   in  steps  of  -2  i.e. ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])  # list [-2: -9 : -2] ----> list from index -2 to -8 in steps of  -2 is  [10.8, True, (3+4j), 25]
print(list[1 : 4]) # list[1:4:1] -----> List from index 1 to 3 in steps of 1 is [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) # list[-4:-1:1] ----> List from index -4 to -2 in steps of 1 is [Tru e, None, 10.8]
print(list[3 : -3])  # list [ 3:-3:1] ----> list from index 3 to -4  in steps of 1 is ['Hyd', True]
print(list[2 : -5])   # List[ 2: -5 :1] ----> List from index 2 to -6 in steps of 1 is [(3+4j)]
print(list[-1:-5])   # list[-1:-5:1] ----> list from index -1 to -6 in steps of 1 is [(3+4j)]
#===================================================================================================
#==================================================================================================
#  Find  outputs  (Home  work)
a =  [25]
#print(a[1])# here a[1] is outof index of list object its an error
print(a[1:]) # here list a[1:1:1] its an itself an empty set
#===================================================================================================
#==================================================================================================
#  Tricky  program
#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))  # [10, 20, 30, 40, 50] 256878276899712
a[1 : 4] = [60 , 70] # [10, 60, 70, 50] 256878276899712
print(a , id(a))   # [10, 60, 70, 50] 256878276899712
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) #[10, 60, 100, 200, 300] 256878276899712
#===================================================================================================
#=================================================================================================
# List  packing
a = 25
b = 10.8  #### here a b c d are alloacted in e arranged as a list  
c = 'Hyd'
d = True
e = [a , b , c , d]  # [ 25, 10.8, 'Hyd', True]
print(e) 
print(type(e))  # class List
#===================================================================================================
#=================================================================================================
#===================================================================================================
# List  unpacking
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d = list
print('a : ' , a)   # a : 25
print('b : ' , b)   # b : 10.8
print('c : ' , c)  #c : 'Hyd'
print('d : ' , d)  #d: True
 #x , y , z = *list   its an error list its already unpackinf
 #x , y , z = list  
 #a , b , c , d , e = list
#===================================================================================================
#=================================================================================================
#  Find  outputs  (Home  work)
#       0   1       2       3       4      5     6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)  # Hyd
print('y : ' , y)   # True
for  x  in  list[2 : 7]:
   print(x)
#===================================================================================================
#=================================================================================================
#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)  #  (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a)  #  25  10.8  'Hyd'  True  3+4j None 'Hyd'  25
print(type(a) # its an tuple class type object
print(len(a)) # 8
print(a[2 : 5]) #('Hyd' , True , 3+4j)
print(*a[2 : 5]) # Hyd True 3+4j
a[2] = 'Sec'      # 
a . append('Sec')
a . remove('Hyd')  #(25 , 10.8 , 'Sec' , True , 3+4j , None , 'Hyd' , 25)
a =  10 , 20 , 30
print(a)  # (10 , 20 , 30)
print(a * 2) # (10 , 20 , 30,10 , 20 , 30)  its allow duplicable
a = 40 , 50 , 60,
print(a) # (40 , 50 , 60,)
print(type(a)) # its a tuple class type data
#===================================================================================================
#=================================================================================================
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
#print(type(a))  # its is an  not a tuple class type  and its an int 
print(type(b))   #its is an tuple class type 
#print(type(c))   # its an int  class type
print(type(d))   #its is an tuple class type
print(a * 4)    # its an integer and get multiply 
print(b * 4)   #  tuple get repeaated is (25, 25, 25, 25)
print(c * 4)    # 100
print(d * 4)   # (25,25,25,25)
#===================================================================================================
#=================================================================================================
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)  # ('H', 'y', 'd')
print(type(a))  # its is a tuple class
print(len(a))   #  3
b = [10 , 20 , 15 , 18]
print(tuple(b))  # (10,20,15,18)
print(tuple(range(5)))  # ( 0,1,2,3, 4)
print(tuple(25))   # int is not convert to tuple  its not a sequence
#===================================================================================================
#=================================================================================================
# Find  outputs (Home  work)
a = ()
print(type(a))  #  its is a class tuple
print(a)  # ()
print(len(a)) # 0
b = tuple()
print(b) # ()
print(len(b)) #0
#===================================================================================================
#=================================================================================================
# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)#(10 , 20 , 30)
print(id(a)) # id of address of a
a = a * 2  #  Valid / Invalid
print(a) # (10 , 20 , 30, 10 , 20 , 30)
print(id(a)) #  address of  2 elements
#===================================================================================================
#=================================================================================================
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)  # (25,10.8,'Hyd',True)
print(type(x)) # class tuple
#===================================================================================================
#=================================================================================================
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , c , d = tpl
print(a) # 25
print(b) #  10.8
print(c) # Hyd
print(d) # True
#p , q , r , s = *tpl  # it cannot be starred expression used
#x , y , z = tpl  # expected 3  got 4
#m , n , o , p , r = tpl  # expected 4 and got 5
#===================================================================================================
#=================================================================================================
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {None, True, 'Hyd', 10.8, 25, (3+4j)}
print(type(a)) # <class 'set'>
print(len(a)) # 6
#print(a[2])  its  not allowed because mutable and set allowws only imutable
#print(a[1 : 4])  its does have ordering or indexing so we can find a correct indexing to extract the element  from list object
#a[2] = 'Sec'  # its not get a[2] index from the set because set  doesnot contaning any index 
#print(a * 2)  # duplicate not allowed
#print(a * a)  # set does not allow mutable mutable error operation error
#===================================================================================================
#=================================================================================================
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False ,'' }
print(len(a)) # 4
print(type(a)) # class set type
#===================================================================================================
#=================================================================================================
#  set()  function demo  program
a = set('Rama rAo')
print(a) #  {'A', 'a', 'R', 'r', ' ', 'o', 'm'}
print(len(a)) #7
print(set([10 , 20 , 15 , 20]))
print(set((25 , 10.8 , 'Hyd' , 10.8)))
print(set(range(10 , 20 , 3))) #{16, 10, 19, 13}
#print(set(25)) #  its not a sequence
#print(set([25 , 10.8 , [] , 'Hyd'])) # set does not allow mutable element in object allow sonly immutable to form a set
#===================================================================================================
#=================================================================================================
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # class list type
print(type(b)) # class tuple type
print(type(c)) # dictonary
print(type(d)) # class set
print(a) # []
print(b) # ()
print(c) #{}
print(d) #  set()
#===================================================================================================
#=================================================================================================
# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a) # {None, True, 'Hyd', 10.8, 25}
print(len(a)) #5
a . remove(25)
print(a)  # {None, True, 'Hyd', 10.8}
a . append(100) # error attribute is not coorect
a . add(set())  # error
a . add(())  # add because tuple is mutable and empty
 #a . add([]) # error only immutable can add in set
print(a)    # {None, True, 'Hyd', 10.8, ()}
a . add({})  # ERROR  we cannot add set in  nested set because in set allows only immutable object
#===================================================================================================
#=================================================================================================
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
#print('set  with  print  function')
print(???) # print(set(a))  ---->{25 , True , 'Hyd' , 10.8}
#print('Iterate  thru  set  with  for  loop')
#How  to  iterate  thru  set  with  for  loop
for x in set(a):
 print(x)
#===================================================================================================
#=================================================================================================
#  Find  outputs
print((32 , 40.6 , [39 , 54.8] , 'Hyd'))  # (32 , 40.6 , [39 , 54.8] , 'Hyd') in tuple there will be list element 
#print({(32 , 40.6 , [39 , 54.8] , 'Hyd')}) # error list elememt are mutable
#===================================================================================================
#=================================================================================================
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)  # {True, 25, 'Hyd'}
print(len(s)) # 3
print(type(s)) # <class 'set'>
#===================================================================================================
#===================================================================================================
{25, 10.8, 'Hyd', True}
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 10.8, 'Hyd', True}
a , b , c , d = s
print(a) # 25
print(b) # 10.8
print(c) # Hyd
print(d) # True
#===================================================================================================
#===================================================================================================
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
 print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} 
 print(type(a))  # ---> set class type
 #print(How  to  print  value  key  10) # print([10])
print(How  to  print  value  key  20) # print([20])
print(How  to  print  value  key  15) # print([15])
print(How  to  print  value  key  18) # print([18]
print(a[19]) # its error keys are not present out of bonu
print(a[0]) #  its error keys are not present out of bonu
print(a['Amar'])How  to  moify  value  of   key  15  to  'Krishna'  # print(a[15] : 'k'])
How  to  remove  20 :  'Kiran'  from  dict  'a'
How  to  append  25 : 'Vamsi'  to  dict  'a'
print(a)
print(len(a))
print(a * 2)









































































a = 40 , 50 , 60,
print(a)
print(type(a))