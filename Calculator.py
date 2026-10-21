num1 = float(input('Angka1: '))
operator = input('Masukkan Operator (+,-,/,*): ')
num2 = float(input('Angka2: '))

if operator == '+':
    hasil = num1 + num2
elif operator == '-':
    hasil = num1 - num2
elif operator == '/':
    hasil = num1 / num2
elif operator == '*':
    hasil = num1 * num2
else:
    print('Error: Tidak bisa dibagi nol')
    
print('Hasil: ', hasil)
