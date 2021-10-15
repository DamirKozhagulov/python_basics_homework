import random
def game():

    number = random.randint(1, 100)
    # print(number)

    userNumber = None
    count = 0
    levels = {1: 10,
              2: 5,
              3: 3}
    level = int(input("Выберите уровень сложности(1, 2 или 3) : "))
    max_count = levels[level]

    userCount = int(input('Введите количество игроков: '))
    users = []
    for i in range(userCount):
        userName = input(f'Введите Имя пользователя {i + 1}: ')
        users.append(userName)
        i += 1
    print(users)
    is_winner = False
    winnerName = None
    while not is_winner:
        count += 1
        if count > max_count:
            print('Все пользователи проиграли!')
            print(f'Правильный ответ {number}')
            break
        print(f'Попытка номер {count}')
        for user in users:
            print(f'Ход пользователя {user}')
            userNumber = int(input('Введите число от 1 до 100: '))
            if userNumber == number:
                is_winner = True
                winnerName = user
                break
            elif userNumber < number:
                print('Вы ошиблишсь! Вы ввели число меньше загаданного')
            else:  # userNumber > number:
                print('Ваше число больше загаданного')
    else:
        print(f'Победа игрока {winnerName}!')
