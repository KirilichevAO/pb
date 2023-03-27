import phone_book
import view

pb = phone_book.PhoneBook('phone_book.txt')

while True:
    choice = view.main_menu()

    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите телефон: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input('Введите индекс контакта который необходимо изменить: '))
            name = input('Введите имя или (Enter - оставить без изменений): ')
            phone = input('Введите телефон (Enter - оставить без изменений): ')
            comment = input('Введите комментарий (Enter - оставить без изменений): ')
            pb.change(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input('Введите индекс контакта который хотите удалить: '))
            pb.delete(index-1)
        case 6:
            pb.save()
        case 7:
            break