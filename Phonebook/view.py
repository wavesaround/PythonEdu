from sys import exit

def launch():
    print('Привет. Это телефонная книга')
    print('Для продолжения введите цифру\n')
    print('1 - Открыть книгу\n2 - Добавить контакт\n3 - Найти контакт\n4 - Изменить контакт\n5 - Удалить контакт')


def type_data(message):
    return input(f'{message}')

def print_card(input_str: str):
    print(input_str.replace(';', ' ').strip())


def print_search(search_result: list):
    print('Результат поиска: \n')
    if len(search_result) == 1:
        print_card(*search_result)
    elif len(search_result) > 1:
        for row in range(len(search_result)):
            value = search_result[row].strip().split(';')
            print(f'{row + 1})', *value)
    else:
        print('Ничего не найдено \n')
        exit()


def sure(question):
    match question:
        case 'delete':
            type_que = ', что хотите удалить контакт'
        case _:
            type_que = '?'            
    user_type = input(f'Вы уверены{type_que}? Y / N: ').lower()
    if user_type == 'y':
        pass
    else:
        exit()


def alert_return(flag):
    match flag:
        case True:
            return print('Все получилось')
        case _:
            return print('Не получилось')
