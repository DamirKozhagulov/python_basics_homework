import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game_reverse import game_reverse
from game import game

save_info("Старт")
try:
    command = sys.argv[1]
except IndexError:
    print("Не введен один из параметров. help")
else:

    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print("Не введен один из параметров")
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не введен один из параметров')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не введен один из параметров')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Не введен один из параметров')
        else:
            copy_file(name, new_name)

    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не введен один из параметров')
        else:
            change_dir(name)

    elif command == 'help':
        print('list - список файлов и папок')
        print('create_files - создать файл')
        print('create_folder - создать папку')
        print('delete - удалить файл или папку')
        print('copy - копировать файл или папку')
        print('change_dir - смена директории')
        print('game - игра "угадайка"')
        print('game_reverse - игра "угадайка-наоборот"')

    elif command == 'game_reverse':
        game_reverse()
    elif command == 'game':
        game()

    save_info("the end")
