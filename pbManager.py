phoneBook = []
path = 'phonebook.txt'

def open_file():
    global phoneBook
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_phonebook = {'name': new[0], 'phone': new[1], 'comment': new[2]}
            # new_phonebook = {}
            # new_phonebook['name'] = new[0]
            # new_phonebook['phone'] = new[1]
            # new_phonebook['comment'] = new[2]
            phoneBook.append(new_phonebook)
        print('Файл открыт.')

def get():
    global phoneBook
    return phoneBook

def add(new_contact: dict):
    global phoneBook
    phoneBook.append(new_contact)
    print('Контакт успешно добавлен.')

def save_file():
    global phoneBook
    global path
    data = []
    for contact in phoneBook:
        new = ';'.join(contact.values())
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print('Изменения успешно сохранены в файле.')

def find(find_option: str):
    global phoneBook
    all_find = []
    for contact in phoneBook:
        for element in contact.values():
            if find_option in element:
                all_find.append(contact)
    return all_find

def change_contact(index: int, contact: dict):
    global phoneBook
    phoneBook.pop(index - 1)
    phoneBook.insert(index - 1, contact)
    print('Контакт успешно изменён.')

def delete_contact(index: int):
    global phoneBook
    phoneBook.pop(index - 1)
    print('Контакт успешно удален.')
