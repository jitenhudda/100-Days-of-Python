# Operators - perform operation

# (1) Arithmetic 
x = 2
y = 4

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)  # power operator - 2 ki power 4 like that
print(x//y)  # integer division - quotient convert into integer

# (2) Camprision 

print(x<y)
print(x>y)
print(x>=y)
print(x<=y)
print(x==y)
print(x!=y)

# (3) Logical
a = True
b = False

print(a or b)  # if one true then true
print(a and b) # if both true then true
print(not a)  #change value of a

# (4) Bitwise - work with binary number -- use in image filteration
#ex-

d=2
e=3
print(d & e)  #output -- 2

# 2 - 010
# 3 - 110  Apply & (and)
#     010 -- this is for 2 answer - 2


# (5) Assignment 
a=3
print(a)

a+=3
print(a)

a-=3
a*=3
a/=3 #like that 

#but do not use increment or decrement operator 
#a++, ++a 


# (6) identity Operator -- check two variable is same memory location or not
a=5
b=5
print(a is b)

a='hello'
b='hello'
print(a is b)

a=[1,2,3]
b=[1,2,3]
print(a is b)  #false output because same dhikne vali chiize same memory location pe ho jaruri nhi


#(7) Membership 

a = 'delhi'
print('d' in a)

