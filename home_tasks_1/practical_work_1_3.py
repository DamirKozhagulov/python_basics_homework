# 3)
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите произвольное число: ')

amount = int(number) + int(number + number) + int(number + number + number)
print(amount)

