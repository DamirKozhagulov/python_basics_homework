# 2)
# Для списка реализовать обмен значений соседних элементов, т.е
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Введите элементы списка по одному. После введения элемента нажмите Enter. Если элементов в списке достаточно '
      'введите "0000".')

main_list = []
while True:
    new_element = input('Введите елемент списка: ')
    if new_element == '0000':
        break
    else:
        main_list.append(new_element)

print(main_list)

result = []
for i in range(len(main_list)):
    new_list = main_list[:2]
    new_list = new_list[::-1]
    main_list = main_list[2:]
    result = result + new_list
print(result)
