from logger import *


def interface():
    with open('phonebook.txt', 'a'):
        pass

    user_input = None
    while user_input != '5':
        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта\n'
            '4. Копировать контакт\n'
            '5. Выход из программы\n'
        )

        user_input = input('Введите вариант: ')

        while user_input not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод.')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                contact = create_contact()
                write_contact('phonebook.txt', contact, 'Контакт записан!')
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contact()
