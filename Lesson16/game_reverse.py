import random
def game_reverse():
    true_number = int(input('Введите число которое должен угадать компьютер: '))
    print("Компьютер приступает к выявлению загаданного числа. Помогите ему, направляя его!")
    number = None
    more = "больше"
    less = "меньше"
    small = 1
    biggest = 100
    while number != true_number:
        number = random.randint(small, biggest)
        print(number)
        if number == true_number:
            print("победа!")
            break
        elif number < true_number:
            userAnswer = input(f'Надо {more} или {less}? ')
            if userAnswer == more:
                small = number - 1
                number = random.randint(number, biggest)

            elif not userAnswer != less:
                biggest = number + 1
                number = random.randint(small, number)
            else:
                print(f"напишите {more} или {less}")
        else:
            userAnswer = input(f'Введите {more} или {less}? ')
            if userAnswer == more:
                small = number - 1
                number = random.randint(number, biggest)

            elif userAnswer == less:
                biggest = number + 1
                number = random.randint(small, number)
            else:
                print(f"напишите {more} или {less}")


    print(f'Компьютер угадал загаданое число {number}')

if __name__ == '__main__':
    game_reverse()

