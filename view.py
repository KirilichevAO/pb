import text_filds

def main_menu() -> int: # меню
    print(text_filds.main_menu)
    lenght_menu = len(text_filds.main_menu.split('\n')) - 2
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= lenght_menu:
            return int(choice)
        else:
            print(f'Введите ЧИСЛО от 1 до {lenght_menu}')
