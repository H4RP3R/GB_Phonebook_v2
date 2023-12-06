from create_data import *


def get_contacts_list(data_file):
    with open(data_file, 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    if contacts_str:
        return contacts_str.rstrip().split('\n\n')
    else:
        return []


def create_contact():
    '''Add an entry'''
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def write_contact(data_file, contact, message):
    with open(data_file, 'a', encoding='utf-8') as file:
        file.write(contact)
        print(f'\n{message}\n')


def print_contacts():
    '''List all entries'''
    contacts_list = get_contacts_list('phonebook.txt')

    if not contacts_list:
        print('Телефонная книга пуста.\n')

    for nn, contact in enumerate(contacts_list, 1):
        print(f'{nn}. {contact}\n')


def search_contact(field=''):
    ''''''
    print(
        'Возможные варианты поиска:\n'
        '1. по фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по номеру\n'
        '5. по городу\n'
    )

    index_var = int(input('Введите вариант поиска: '))-1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = get_contacts_list('phonebook.txt')

    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')


def copy_contact():
    with open('contacts_copy.txt', 'a'):
        pass

    print_contacts()

    contacts_list = get_contacts_list('phonebook.txt')

    if not contacts_list:
        return

    contacts_list_copy = get_contacts_list('contacts_copy.txt')
    contact_num = None

    while contact_num not in range(len(contacts_list)):
        contact_num = int(input('Введите номер контакта для копирования: '))-1

    if contacts_list[contact_num] in contacts_list_copy:
        print('\nДанный контакт уже скопирован.\n')
    else:
        contact_str = contacts_list[contact_num] + '\n\n'
        write_contact('contacts_copy.txt', contact_str, 'Контакт скопирован!')
