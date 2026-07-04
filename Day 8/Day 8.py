# Type Conversion -- it is not a parmanent only when apply after that same value given before conversion

#two types -- 
# (1) implicit - automatically type conversion
# (2) explicit - manually

print(4+5.7)
print(2 + 4+5j)


#explicit function --
#int
print(int(9.5))

#float
print(float(4))

#str
print(str('999'))

#bool
print(bool(0))

#complex
print(complex(5))

#list
print(list('hello'))

#tuple
print(tuple('world'))

#set
print(set('hilux'))




first_num = input('Enter first number - ')
second_num = input('enter second number - ')
print(first_num)
print(second_num)

result = int(first_num)+int(second_num)
print(result)
