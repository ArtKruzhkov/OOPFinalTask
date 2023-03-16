
def menu():
    print('''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход''')
    choice = int(input('Выберите пункт из меню: '))
    return choice

def show_contacts(pb: list[dict]):
    if pb == []:
        print('Нет контактов в телефонной книге или файл не открыт!')
    else:
        print('Контакты: ')
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} {phone:<15} {comment:<20}')


def new_contact_input():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new_phonebook = {'name': name, 'phone': phone, 'comment': comment}
    return new_phonebook

def find_contact():
    find = input('Введите искомый элемент(фамилию и имя или телефон или комментарий): ')
    return find

def input_id():
    number = int(input('Введите id(номер по списку) контакта который хотите изменить: '))
    return number

def input_id2():
    number = int(input('Введите id(номер по списку) контакта который хотите удалить: '))
    return number