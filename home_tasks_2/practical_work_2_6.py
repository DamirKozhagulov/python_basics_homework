# 6)
# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})

# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]

i = 1
while True:
    product_name = input('название товара: ')
    if product_name == '0000':
        break
    else:
        price = input('введите цену товара: ')
        amount = input('введите количество товара: ')
        new_dict = {'название': product_name, 'цена': price, 'количество': amount, 'ед.': 'шт.'}
        print(new_dict)
        reg_tuple = (i, new_dict)
        i += 1
        print(reg_tuple)

# не разобрался