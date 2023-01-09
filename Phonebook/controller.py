import database
import view

def open_book():
    get_row = database.get_all()
    view.print_search(get_row)    

def new_contact():
    first_name = view.type_data('Введите Имя: ')
    last_name = view.type_data('Введите Фамилию: ')
    tel = view.type_data('Введите телефон: ')
    database.write_to_db(first_name, last_name, tel)


def search():
    input_data = view.type_data('Введите имя или фамилию: ')
    get_row = database.search_data(input_data)
    view.print_search(get_row)


def edit_contact():
    edit_id = 1
    input_data = view.type_data('Введите имя или фамилию: ')
    get_rows = database.search_data(input_data)
    view.print_search(get_rows)
    if len(get_rows) > 1: 
        edit_id = int(view.type_data('Введите номер контакта для редактирования '))
        view.print_card(get_rows[edit_id - 1])
    new_line = view.type_data('Внесите изменения через пробел --> ')
    database.edit_card(get_rows[edit_id - 1], new_line)


def start():
    view.launch()
    go_button = view.type_data('')
    match go_button:
        case '1':
            open_book()
        case '2':
            new_contact()
        case '3':
            search()
        case '4':
            edit_contact()
        case _:
            print('Попробуйте еще')
            start() 
