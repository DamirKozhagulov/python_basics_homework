# 4)
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите целое положительное число: ')
print(len(number))
result = []
i = 0
while i < len(number):
    num = number[i]
    result.append(num)
    i += 1
number = sorted(result)
print(number)
print('Самая большая цифра ' + number[-1])
