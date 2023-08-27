# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

num_dec = int(input("Введите число: "))
res = ''
DIVIDER = 16
print(hex(num_dec))
while num_dec > 0:
    add_num = str(num_dec % DIVIDER)
    if add_num == '10':
        add_num = 'a' 
    elif add_num == '11':
        add_num = 'b'
    elif add_num == '12':
        add_num = 'c'
    elif add_num == '13':
        add_num = 'd'
    elif add_num == '14':
        add_num = 'e'
    elif add_num == '15':
        add_num = 'f'
    res = add_num + res
    num_dec = num_dec // DIVIDER
print(res)