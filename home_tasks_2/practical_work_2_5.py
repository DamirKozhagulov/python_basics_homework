# 5.
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

print('У людей дома узнал любимый день в неделе. '
      'Дни недели соответствуют порядковым номерам принятым в нашей стране')
entered_numbers = [5, 3, 6, 1, 6, 7, 5]

while True:

    print(entered_numbers)
    enter_number = int(input('Введите любимый день недели от 1 до 7(от понедельника до восресенья): '))
    entered_numbers.sort(reverse=True)
    for i in range(len(entered_numbers)):
        if enter_number > entered_numbers[i]:
            entered_numbers.insert(i, enter_number)
            break
    else:
        entered_numbers.append(enter_number)






