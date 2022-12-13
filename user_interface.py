import recorder as rec
import reader

def user_meet():
    print('Программа для записи и чтения телефонных номеров\n\
    Для добавления номера нажмите 1\n\
    Для чтения справочника нажмите 2\n\
    Для выхода из программы нажмите 0')


def start():
    user_meet()
    action = input()
    while action < '0' or action > '2':
        print('Для выбора действия введите 0, 1 или 2')
        action = input()
    while action != '0':
        if action == '1':
            add_subscriber()
        elif action == '2':
            print('Для вывода записей в столбик нажмите 1\n\
            Для вывода  каждой записи в одну строку нажмите 2')
            print_variant = input()
            while print_variant < '1' or print_variant > '2':
                print("Необходимо ввести 1 или 2 для выбора варианта вывода справочника")
                print_variant = input()
            if print_variant == '1':
                reader.reader_1()
            else:
                reader.reader_2()
        user_meet()
        action = input()

def add_subscriber():
    surname = input('Фамилия:\t')
    name = input('Имя:\t\t')
    number = input('Номер:\t\t')
    comment = input('Комментарий:\t')
    subscriber = [surname, name, number, comment]
    rec.record_1(subscriber)
    rec.record_2(subscriber)
