# 4)
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые десять букв в слове

beg_list = input("Введите строку из нескольких слов, разделённых пробелами: ")
sec_list = beg_list.split(' ')
for i in range(len(sec_list)):
    if len(sec_list[i]) > 10:
        print(f'{i+1}) {sec_list[i][:11]}')
    else:
        print(f'{i+1}) {sec_list[i]}')