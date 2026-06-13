# if -else

#correct mail = jiten@gmail.com
#correct password = 1234


mail = input('enter you mail id')
password = input('enter your password')

if mail == 'jiten@gmail.com' and password == '1234':
    print('welcome')

elif mail == 'jiten@gmail.com' and password != '1234':
    print('password is wrong')

else:
    print("worng password")