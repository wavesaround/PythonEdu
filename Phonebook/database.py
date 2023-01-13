from pathlib import Path
from view import alert_return

db_path = Path('database.csv')


def get_all():
    search_result = []
    with open(db_path, 'r', newline='') as db_main:
        for row in db_main:
            search_result.append(row)
        return search_result    

def write_to_db(f_name, l_name, tel):
    with open(db_path, 'a', newline='') as db_main:
        db_main.write('{};{};{}\n'
                      .format(f_name, l_name, tel))


def search_data(data: str) -> list:
    search_result = []
    new_data = data.replace(' ', ';').lower()
    with open(db_path, 'r', newline='') as db_main:
        for row in db_main:
            if new_data in row.lower():
                search_result.append(row)
        return search_result


def edit_card(str_target: str, str_new: str):
    str_new = str_new.replace(' ', ';').strip()
    with open(db_path, 'r') as db_read:
        lines = db_read.readlines()
    with open(db_path, 'w') as db_write:
        for line in lines:
            if line == str_target:
                db_write.write(f'{str_new}\n')
            else:
                db_write.write(line)
    alert_return(True)


def delete_card(str_target: str):
    with open(db_path, 'r') as db_read:
        lines = db_read.readlines()
    with open(db_path, 'w') as db_write:
        for line in lines:
            if line == str_target:
                pass
            else:
                db_write.write(line)
    alert_return(True)