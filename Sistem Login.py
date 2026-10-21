username = 'Mozart'
password = 'user123'

var1 = input('Username: ')
var2 = input('Password: ')

if var1 == username and var2 == password:
    print('Login Berhasil!')
elif var1 == username and var2 != password:
    print('Password Salah!')
elif var1 != username and var2 == password:
    print('Username Salah!')
else:
    print('Password and Username Salah!')
